from Scripts import run
from Scripts import utils
import platform
import json

os_name = platform.system()

class WifiProfileExtractor:
    def __init__(self):
        self.run = run.Run().run
        self.utils = utils.Utils()

    def get_authentication_type(self, authentication_type):
        authentication_type = authentication_type.lower()

        open_types = ("none", "owe", "open")
        for open_type in open_types:
            if open_type in authentication_type:
                return "open"

        if "wep" in authentication_type or "shared" in authentication_type:
            return "wep"
        
        if "wpa" in authentication_type or "sae" in authentication_type:
            return "wpa"
        
        return None

    def validate_wifi_password(self, authentication_type=None, password=None):
        print("正在使用认证类型 {} 验证密码".format(authentication_type))

        if password is None:
            return None

        if authentication_type is None:
            return password

        if authentication_type == "open":
            return ""

        try:
            password.encode('ascii')
        except UnicodeEncodeError:
            return None
            
        if 8 <= len(password) <= 63 and all(32 <= ord(c) <= 126 for c in password):
            return password
                
        return None

    def get_wifi_password_macos(self, ssid):
        output = self.run({
            "args": ["security", "find-generic-password", "-wa", ssid]
        })

        if output[-1] != 0:
            return None
                
        try:
            ssid_info = json.loads(output[0].strip())
            password = ssid_info.get("password")
        except:
            password = output[0].strip() if output[0].strip() else None
            
        return self.validate_wifi_password("wpa", password)
        
    def get_wifi_password_windows(self, ssid):
        output = self.run({
            "args": ["netsh", "wlan", "show", "profile", ssid, "key=clear"]
        })

        if output[-1] != 0:
            return None

        authentication_type = None
        password = None

        for line in output[0].splitlines():
            if authentication_type is None and "Authentication" in line:
                authentication_type = self.get_authentication_type(line.split(":")[1].strip())
            elif "Key Content" in line:
                password = line.split(":")[1].strip()

        return self.validate_wifi_password(authentication_type, password)

    def get_wifi_password_linux(self, ssid):
        output = self.run({
            "args": ["nmcli", "--show-secrets", "connection", "show", ssid]
        })

        if output[-1] != 0:
            return None
        
        authentication_type = None
        password = None

        for line in output[0].splitlines():
            if "802-11-wireless-security.key-mgmt:" in line:
                authentication_type = self.get_authentication_type(line.split(":")[1].strip())
            elif "802-11-wireless-security.psk:" in line:
                password = line.split(":")[1].strip()

        return self.validate_wifi_password(authentication_type, password)

    def ask_network_count(self, total_networks):
        self.utils.head("WiFi 网络检索")
        print("")
        print("在此设备上找到 {} 个 WiFi 网络。".format(total_networks))
        print("")
        print("您想处理多少个网络？")
        print("  1-{} - 指定数量（默认：5）".format(total_networks))
        print("  A   - 所有可用网络")
        print("")
        
        num_choice = self.utils.request_input("输入您的选择：").strip().lower() or "5"
        
        if num_choice == "a":
            print("将处理所有可用网络。")
            return total_networks

        try:
            max_networks = min(int(num_choice), total_networks)
            print("将处理最多 {} 个网络。".format(max_networks))
            return max_networks
        except:
            max_networks = min(5, total_networks)
            print("选择无效。将处理最多 {} 个网络。".format(max_networks))
            return max_networks
            
    def process_networks(self, ssid_list, max_networks, get_password_func):
        networks = []
        processed_count = 0
        consecutive_failures = 0
        max_consecutive_failures = 3
        
        while len(networks) < max_networks and processed_count < len(ssid_list):
            ssid = ssid_list[processed_count]
            
            try:
                print("")
                print("正在处理 {}/{}: {}".format(processed_count + 1, len(ssid_list), ssid))
                if os_name == "Darwin":
                    print("请输入您的管理员用户名和密码，或点击"拒绝"跳过此网络。")
                
                password = get_password_func(ssid)
                if password is not None:
                    if (ssid, password) not in networks:
                        consecutive_failures = 0
                        networks.append((ssid, password))
                        print("成功检索密码。")
                        
                        if len(networks) == max_networks:
                            break
                else:
                    consecutive_failures += 1 if os_name == "Darwin" else 0
                    print("无法检索此网络的密码。")

                    if consecutive_failures >= max_consecutive_failures:
                        continue_input = self.utils.request_input("\n无法检索密码。继续尝试？(是/否): ").strip().lower() or "是"
                        
                        if continue_input != "yes":
                            break

                        consecutive_failures = 0
            except Exception as e:
                consecutive_failures += 1 if os_name == "Darwin" else 0
                print("处理网络 '{}' 时出错：{}".format(ssid, str(e)))

                if consecutive_failures >= max_consecutive_failures:
                    continue_input = self.utils.request_input("\n无法检索密码。要继续尝试吗？(是/否): ").strip().lower() or "是"

                    if continue_input not in ("是", "yes"):
                        break

                    consecutive_failures = 0
            finally:
                processed_count += 1
            
            if processed_count >= max_networks and len(networks) < max_networks and processed_count < len(ssid_list):
                continue_input = self.utils.request_input("\n仅检索到 {}/{} 个网络。要继续尝试更多以达到您的目标吗？(是/否): ".format(len(networks), max_networks)).strip().lower() or "是"
                
                if continue_input not in ("是", "yes"):
                    break

                consecutive_failures = 0
        
        return networks

    def get_preferred_networks_macos(self, interface):
        output = self.run({
            "args": ["networksetup", "-listpreferredwirelessnetworks", interface]
        })

        if output[-1] != 0 or "Preferred networks on" not in output[0]:
            return []
        
        ssid_list = [network.strip() for network in output[0].splitlines()[1:] if network.strip()]
        
        if not ssid_list:
            return []
            
        max_networks = self.ask_network_count(len(ssid_list))
        
        self.utils.head("需要管理员认证")
        print("")
        print("要从钥匙串检索 WiFi 密码，macOS 将为每个 WiFi 网络提示")
        print("您输入管理员凭据。")
        
        return self.process_networks(ssid_list, max_networks, self.get_wifi_password_macos)

    def get_preferred_networks_windows(self):
        output = self.run({
            "args": ["netsh", "wlan", "show", "profiles"]
        })

        if output[-1] != 0:
            return []
        
        ssid_list = []

        for line in output[0].splitlines():
            if "All User Profile" in line:
                try:
                    ssid = line.split(":")[1].strip()
                    if ssid:
                        ssid_list.append(ssid)
                except:
                    continue
        
        if not ssid_list:
            return []

        max_networks = len(ssid_list)
    
        self.utils.head("WiFi 配置文件提取器")
        print("")
        print("正在检索 {} 个网络的密码...".format(len(ssid_list)))
        
        return self.process_networks(ssid_list, max_networks, self.get_wifi_password_windows)

    def get_preferred_networks_linux(self):
        output = self.run({
            "args": ["nmcli", "-t", "-f", "NAME", "connection", "show"]
        })

        if output[-1] != 0:
            return []
        
        ssid_list = [network.strip() for network in output[0].splitlines() if network.strip()]
        
        if not ssid_list:
            return []
            
        max_networks = len(ssid_list)
    
        self.utils.head("WiFi 配置文件提取器")
        print("")
        print("正在检索 {} 个网络的密码...".format(len(ssid_list)))
        
        return self.process_networks(ssid_list, max_networks, self.get_wifi_password_linux)

    def get_wifi_interfaces(self):
        output = self.run({
            "args": ["networksetup", "-listallhardwareports"]
        })

        if output[-1] != 0:
            return []
        
        interfaces = []
        
        for interface_info in output[0].split("\n\n"):
            if "Device: en" in interface_info:
                try:
                    interface = "en{}".format(int(interface_info.split("Device: en")[1].split("\n")[0]))
                    
                    test_output = self.run({
                        "args": ["networksetup", "-listpreferredwirelessnetworks", interface]
                    })

                    if test_output[-1] == 0 and "Preferred networks on" in test_output[0]:
                        interfaces.append(interface)
                except:
                    continue

        return interfaces
    
    def get_profiles(self):
        os_name = platform.system()

        self.utils.head("WiFi 配置文件提取器")
        print("")
        print("\033[1;93m 注意：\033[0m")
        print("- 当使用 itlwm kext 时，WiFi 在 macOS 中显示为以太网")
        print("- 您需要 Heliport 应用程序来管理 macOS 中的 WiFi 连接")
        print("- 此步骤将启用启动时自动 WiFi 连接")
        print("  对于通过 Recovery OS 安装 macOS 的用户很有用")
        print("")
        
        while True:
            user_input = self.utils.request_input("您想扫描 WiFi 配置文件吗？(是/否): ").strip().lower()
            
            if user_input == "yes":
                break
            elif user_input == "no":
                return []
            else:
                print("\033[91m 选择无效，请重试。\033[0m\n\n")

        profiles = []
        self.utils.head("正在检测 WiFi 配置文件")
        print("")
        print("正在扫描 WiFi 配置文件...")
        
        if os_name == "Windows":
            profiles = self.get_preferred_networks_windows()
        elif os_name == "Linux":
            profiles = self.get_preferred_networks_linux()
        elif os_name == "Darwin":
            wifi_interfaces = self.get_wifi_interfaces()

            if wifi_interfaces:
                for interface in wifi_interfaces:
                    print("正在检查接口：{}".format(interface))
                    interface_profiles = self.get_preferred_networks_macos(interface)
                    if interface_profiles:
                        profiles = interface_profiles
                        break
            else:
                print("未检测到 WiFi 接口。")

        if not profiles:
            self.utils.head("WiFi 配置文件提取器")
            print("")
            print("未找到保存密码的 WiFi 配置文件。")
            self.utils.request_input()
        
        self.utils.head("WiFi 配置文件提取器")
        print("")
        print("找到以下保存密码的 WiFi 配置文件：")
        print("")
        print("索引  SSID                             密码")
        print("-------------------------------------------------------")
        for index, (ssid, password) in enumerate(profiles, start=1):
            print("{:<6} {:<32} {:<8}".format(index, ssid[:31] + "..." if len(ssid) > 31 else ssid, password[:12] + "..." if len(password) > 12 else password))
        print("")
        print("成功应用 {} 个 WiFi 配置文件。".format(len(profiles)))
        print("")
            
        self.utils.request_input()
        return profiles