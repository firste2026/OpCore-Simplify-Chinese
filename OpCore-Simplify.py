from Scripts.datasets import os_data
from Scripts.datasets import chipset_data
from Scripts import acpi_guru
from Scripts import compatibility_checker
from Scripts import config_prodigy
from Scripts import gathering_files
from Scripts import hardware_customizer
from Scripts import kext_maestro
from Scripts import report_validator
from Scripts import run
from Scripts import smbios
from Scripts import utils
import updater
import os
import sys
import re
import shutil
import traceback
import time

class OCPE:
    def __init__(self):
        self.u = utils.Utils("OpCore Simplify")
        self.u.clean_temporary_dir()
        self.ac = acpi_guru.ACPIGuru()
        self.c = compatibility_checker.CompatibilityChecker()
        self.co = config_prodigy.ConfigProdigy()
        self.o = gathering_files.gatheringFiles()
        self.h = hardware_customizer.HardwareCustomizer()
        self.k = kext_maestro.KextMaestro()
        self.s = smbios.SMBIOS()
        self.v = report_validator.ReportValidator()
        self.r = run.Run()
        self.result_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Results")

    def select_hardware_report(self):
        self.ac.dsdt = self.ac.acpi.acpi_tables = None

        while True:
            self.u.head("选择硬件报告")
            print("")
            if os.name == "nt":
                print("\033[1;93m注意:\033[0m")
                print("- 在生成硬件报告之前，请确保您使用的是最新版本的 Hardware Sniffer。")
                print("- Hardware Sniffer 在 Windows PE 中不会收集 GPU 的 Resizable BAR 选项（默认禁用）和显示器连接的相关信息。")
                print("")
                print("E. 导出硬件报告（推荐）")
                print("")
            print("Q. 退出")
            print("")
        
            user_input = self.u.request_input("拖放您的硬件报告至此 (.JSON){}: ".format(" 或输入 \"E\" 导出" if os.name == "nt" else ""))
            if user_input.lower() == "q":
                self.u.exit_program()
            if user_input.lower() == "e":
                hardware_sniffer = self.o.gather_hardware_sniffer()

                if not hardware_sniffer:
                    continue

                report_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "SysReport")

                self.u.head("正在导出硬件报告")
                print("")
                print("正在导出硬件报告到 {}...".format(report_dir))
                
                output = self.r.run({
                    "args":[hardware_sniffer, "-e", "-o", report_dir]
                })

                if output[-1] != 0:
                    error_code = output[-1]
                    if error_code == 3:
                        error_message = "收集硬件时出错。"
                    elif error_code == 4:
                        error_message = "生成硬件报告时出错。"
                    elif error_code == 5:
                        error_message = "转储 ACPI 表时出错。"
                    else:
                        error_message = "未知错误。"

                    print("")
                    print("无法导出硬件报告。{}".format(error_message))
                    print("请重试或手动使用 Hardware Sniffer。")
                    print("")
                    self.u.request_input()
                    continue
                else:
                    report_path = os.path.join(report_dir, "Report.json")
                    acpitables_dir = os.path.join(report_dir, "ACPI")

                    report_data = self.u.read_file(report_path)
                    self.ac.read_acpi_tables(acpitables_dir)
                    
                    return report_path, report_data
                
            path = self.u.normalize_path(user_input)
            
            is_valid, errors, warnings, data = self.v.validate_report(path)
            
            self.v.show_validation_report(path, is_valid, errors, warnings)
            if not is_valid or errors:
                print("")
                print("\033[32m建议:\033[0m 请重新导出硬件报告后重试。")
                print("")
                self.u.request_input("按回车键返回...")
            else:
                return path, data
            
    def show_oclp_warning(self):
        while True:
            self.u.head("OpenCore Legacy Patcher 警告")
            print("")
            print("1. OpenCore Legacy Patcher 是在更新版本的 macOS 中启用被放弃的 GPU 和 Broadcom WiFi")
            print("   支持的唯一解决方案，同时也可以为 macOS Tahoe 26 恢复 AppleHDA。")
            print("")
            print("2. OpenCore Legacy Patcher 会禁用 macOS 安全功能（包括 SIP 和 AMFI），这可能")
            print("   导致一些问题，例如更新时需要完整安装程序、应用程序崩溃和")
            print("   系统不稳定。")
            print("")
            print("3. OpenCore Legacy Patcher 未正式支持黑苹果社区。")
            print("")
            print("\033[1;91m重要提示:\033[0m")
            print("在继续之前，请仔细考虑这些风险。")
            print("")
            print("\033[1;96m对 macOS Tahoe 26 的支持:\033[0m")
            print("要补丁 macOS Tahoe 26，您必须从 GitHub 上的")
            print("我的仓库 \033[4mlzhoang2801/OpenCore-Legacy-Patcher\033[0m 下载 OpenCore-Patcher 3.0.0 或更新版本。")
            print("较旧版本或官方 Dortania 发布版不支持 Tahoe 26。")
            print("")
            option = self.u.request_input("您要继续使用 OpenCore Legacy Patcher 吗？(是/否): ").strip().lower()
            if option in ("是", "yes"):
                return True
            elif option in ("否", "no"):
                return False

    def select_macos_version(self, hardware_report, native_macos_version, ocl_patched_macos_version):
        suggested_macos_version = native_macos_version[1]
        version_pattern = re.compile(r'^(\d+)(?:\.(\d+)(?:\.(\d+))?)?$')

        for device_type in ("GPU", "Network", "Bluetooth", "SD 控制器"):
            if device_type in hardware_report:
                for device_name, device_props in hardware_report[device_type].items():
                    if device_props.get("Compatibility", (None, None)) != (None, None):
                        if device_type == "GPU" and device_props.get("Device Type") == "Integrated GPU":
                            device_id = device_props.get("Device ID", ""*8)[5:]

                            if device_props.get("Manufacturer") == "AMD" or device_id.startswith(("59", "87C0")):
                                suggested_macos_version = "22.99.99"
                            elif device_id.startswith(("09", "19")):
                                suggested_macos_version = "21.99.99"

                        if self.u.parse_darwin_version(suggested_macos_version) > self.u.parse_darwin_version(device_props.get("Compatibility")[0]):
                            suggested_macos_version = device_props.get("Compatibility")[0]

        while True:
            if "Beta" in os_data.get_macos_name_by_darwin(suggested_macos_version):
                suggested_macos_version = "{}{}".format(int(suggested_macos_version[:2]) - 1, suggested_macos_version[2:])
            else:
                break

        while True:
            self.u.head("选择 macOS 版本")
            if native_macos_version[1][:2] != suggested_macos_version[:2]:
                print("")
                print("\033[1;36m建议的 macOS 版本:\033[0m")
                print("- 为了更好的兼容性和稳定性，我们建议您仅使用 {} 或更旧版本。".format(os_data.get_macos_name_by_darwin(suggested_macos_version)))
            print("")
            print("可用的 macOS 版本:")
            print("")

            oclp_min = int(ocl_patched_macos_version[-1][:2]) if ocl_patched_macos_version else 99
            oclp_max = int(ocl_patched_macos_version[0][:2]) if ocl_patched_macos_version else 0
            min_version = min(int(native_macos_version[0][:2]), oclp_min)
            max_version = max(int(native_macos_version[-1][:2]), oclp_max)

            for darwin_version in range(min_version, max_version + 1):
                name = os_data.get_macos_name_by_darwin(str(darwin_version))
                label = " (\033[1;93m需要 OpenCore Legacy Patcher\033[0m)" if oclp_min <= darwin_version <= oclp_max else ""
                print("   {}. {}{}".format(darwin_version, name, label))

            print("")
            print("\033[1;93m注意:\033[0m")
            print("- 要选择主版本，请输入数字（例如：19）。")
            print("- 要指定完整版本，请使用 Darwin 版本格式（例如：22.4.6）。")
            print("")
            print("Q. 退出")
            print("")
            option = self.u.request_input("请输入您要使用的 macOS 版本（默认：{}）: ".format(os_data.get_macos_name_by_darwin(suggested_macos_version))) or suggested_macos_version
            if option.lower() == "q":
                self.u.exit_program()

            match = version_pattern.match(option)
            if match:
                target_version = "{}.{}.{}".format(match.group(1), match.group(2) if match.group(2) else 99, match.group(3) if match.group(3) else 99)
                
                if ocl_patched_macos_version and self.u.parse_darwin_version(ocl_patched_macos_version[-1]) <= self.u.parse_darwin_version(target_version) <= self.u.parse_darwin_version(ocl_patched_macos_version[0]):
                    return target_version
                elif self.u.parse_darwin_version(native_macos_version[0]) <= self.u.parse_darwin_version(target_version) <= self.u.parse_darwin_version(native_macos_version[-1]):
                    return target_version

    def build_opencore_efi(self, hardware_report, disabled_devices, smbios_model, macos_version, needs_oclp):
        steps = [
            "正在复制 EFI 基础文件到结果文件夹",
            "正在应用 ACPI 补丁",
            "正在复制 kexts 并快照到 config.plist",
            "正在生成 config.plist",
            "正在清理未使用的驱动程序、资源和工具"
        ]
        
        title = "正在构建 OpenCore EFI"

        self.u.progress_bar(title, steps, 0)
        self.u.create_folder(self.result_dir, remove_content=True)

        if not os.path.exists(self.k.ock_files_dir):
            raise Exception("目录 '{}' 不存在。".format(self.k.ock_files_dir))
        
        source_efi_dir = os.path.join(self.k.ock_files_dir, "OpenCorePkg")
        shutil.copytree(source_efi_dir, self.result_dir, dirs_exist_ok=True)

        config_file = os.path.join(self.result_dir, "EFI", "OC", "config.plist")
        config_data = self.u.read_file(config_file)
        
        if not config_data:
            raise Exception("错误：文件 {} 不存在。".format(config_file))
        
        self.u.progress_bar(title, steps, 1)
        config_data["ACPI"]["Add"] = []
        config_data["ACPI"]["Delete"] = []
        config_data["ACPI"]["Patch"] = []
        if self.ac.ensure_dsdt():
            self.ac.hardware_report = hardware_report
            self.ac.disabled_devices = disabled_devices
            self.ac.acpi_directory = os.path.join(self.result_dir, "EFI", "OC", "ACPI")
            self.ac.smbios_model = smbios_model
            self.ac.lpc_bus_device = self.ac.get_lpc_name()

            for patch in self.ac.patches:
                if patch.checked:
                    if patch.name == "BATP":
                        patch.checked = getattr(self.ac, patch.function_name)()
                        self.k.kexts[kext_maestro.kext_data.kext_index_by_name.get("ECEnabler")].checked = patch.checked
                        continue

                    acpi_load = getattr(self.ac, patch.function_name)()

                    if not isinstance(acpi_load, dict):
                        continue

                    config_data["ACPI"]["Add"].extend(acpi_load.get("Add", []))
                    config_data["ACPI"]["Delete"].extend(acpi_load.get("Delete", []))
                    config_data["ACPI"]["Patch"].extend(acpi_load.get("Patch", []))
        
        config_data["ACPI"]["Patch"].extend(self.ac.dsdt_patches)
        config_data["ACPI"]["Patch"] = self.ac.apply_acpi_patches(config_data["ACPI"]["Patch"])

        self.u.progress_bar(title, steps, 2)
        kexts_directory = os.path.join(self.result_dir, "EFI", "OC", "Kexts")
        self.k.install_kexts_to_efi(macos_version, kexts_directory)
        config_data["Kernel"]["Add"] = self.k.load_kexts(hardware_report, macos_version, kexts_directory)

        self.u.progress_bar(title, steps, 3)
        self.co.genarate(hardware_report, disabled_devices, smbios_model, macos_version, needs_oclp, self.k.kexts, config_data)
        self.u.write_file(config_file, config_data)

        self.u.progress_bar(title, steps, 4)
        files_to_remove = []

        drivers_directory = os.path.join(self.result_dir, "EFI", "OC", "Drivers")
        driver_list = self.u.find_matching_paths(drivers_directory, extension_filter=".efi")
        driver_loaded = [kext.get("Path") for kext in config_data.get("UEFI").get("Drivers")]
        for driver_path, type in driver_list:
            if not driver_path in driver_loaded:
                files_to_remove.append(os.path.join(drivers_directory, driver_path))

        resources_audio_dir = os.path.join(self.result_dir, "EFI", "OC", "Resources", "Audio")
        if os.path.exists(resources_audio_dir):
            files_to_remove.append(resources_audio_dir)

        picker_variant = config_data.get("Misc", {}).get("Boot", {}).get("PickerVariant")
        if picker_variant in (None, "Auto"):
            picker_variant = "Acidanthera/GoldenGate" 
        if os.name == "nt":
            picker_variant = picker_variant.replace("/", "\\")

        resources_image_dir = os.path.join(self.result_dir, "EFI", "OC", "Resources", "Image")
        available_picker_variants = self.u.find_matching_paths(resources_image_dir, type_filter="dir")

        for variant_name, variant_type in available_picker_variants:
            variant_path = os.path.join(resources_image_dir, variant_name)
            if ".icns" in ", ".join(os.listdir(variant_path)):
                if picker_variant not in variant_name:
                    files_to_remove.append(variant_path)

        tools_directory = os.path.join(self.result_dir, "EFI", "OC", "Tools")
        tool_list = self.u.find_matching_paths(tools_directory, extension_filter=".efi")
        tool_loaded = [tool.get("Path") for tool in config_data.get("Misc").get("Tools")]
        for tool_path, type in tool_list:
            if not tool_path in tool_loaded:
                files_to_remove.append(os.path.join(tools_directory, tool_path))

        if "manifest.json" in os.listdir(self.result_dir):
            files_to_remove.append(os.path.join(self.result_dir, "manifest.json"))

        for file_path in files_to_remove:
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
            except Exception as e:
                print("删除文件失败：{}".format(e))
        
        self.u.progress_bar(title, steps, len(steps), done=True)
        
        print("OpenCore EFI 构建完成。")
        time.sleep(2)
        
    def check_bios_requirements(self, org_hardware_report, hardware_report):
        requirements = []
        
        org_firmware_type = org_hardware_report.get("BIOS", {}).get("Firmware Type", "Unknown")
        firmware_type = hardware_report.get("BIOS", {}).get("Firmware Type", "Unknown")
        if org_firmware_type == "Legacy" and firmware_type == "UEFI":
            requirements.append("启用 UEFI 模式（禁用 Legacy/CSM（兼容性支持模块））")

        secure_boot = hardware_report.get("BIOS", {}).get("Secure Boot", "Unknown")
        if secure_boot != "Disabled":
            requirements.append("禁用安全启动（Secure Boot）")
        
        if hardware_report.get("Motherboard", {}).get("Platform") == "Desktop" and hardware_report.get("Motherboard", {}).get("Chipset") in chipset_data.IntelChipsets[112:]:
            resizable_bar_enabled = any(gpu_props.get("Resizable BAR", "Disabled") == "Enabled" for gpu_props in hardware_report.get("GPU", {}).values())
            if not resizable_bar_enabled:
                requirements.append("启用 Above 4G Decoding")
                requirements.append("禁用 Resizable BAR/Smart Access Memory")
                
        return requirements

    def before_using_efi(self, org_hardware_report, hardware_report):
        while True:
            self.u.head("使用 EFI 之前")
            print("")                 
            print("\033[93m请完成以下步骤:\033[0m")
            print("")
            
            bios_requirements = self.check_bios_requirements(org_hardware_report, hardware_report)
            if bios_requirements:
                print("* 需要配置 BIOS/UEFI 设置:")
                for requirement in bios_requirements:
                    print("    - {}".format(requirement))
                print("")
            
            print("* USB 映射:")
            print("    - 使用 USBToolBox 工具映射 USB 端口。")
            print("    - 将创建的 UTBMap.kext 添加到 {} 文件夹。".format("EFI\\OC\\Kexts" if os.name == "nt" else "EFI/OC/Kexts"))
            print("    - 从 {} 文件夹中删除 UTBDefault.kext。".format("EFI\\OC\\Kexts" if os.name == "nt" else "EFI/OC/Kexts"))
            print("    - 编辑 config.plist:")
            print("        - 使用 ProperTree 打开您的 config.plist。")
            print("        - 按 Command/Ctrl + R 运行 OC Snapshot。")
            print("        - 如果单个控制器上有超过 15 个端口，请启用 XhciPortLimit 补丁。")
            print("        - 完成后保存文件。")
            print("")
            self.u.open_folder(self.result_dir)
            self.u.request_input()

    def main(self):
        hardware_report_path = None
        native_macos_version = None
        disabled_devices = None
        macos_version = None
        ocl_patched_macos_version = None
        needs_oclp = False
        smbios_model = None

        while True:
            self.u.head()
            print("")
            print("  硬件报告：{}".format(hardware_report_path or '未选择'))
            if hardware_report_path:
                print("")
                print("  macOS 版本：{}".format(os_data.get_macos_name_by_darwin(macos_version) if macos_version else '未选择') + (' (' + macos_version + ')' if macos_version else '') + ('. \033[1;93m需要 OpenCore Legacy Patcher\033[0m' if needs_oclp else ''))
                print("  SMBIOS:       {}".format(smbios_model or '未选择'))
                if disabled_devices:
                    print("  禁用的设备:")
                    for device, _ in disabled_devices.items():
                        print("    - {}".format(device))
            print("")

            print("1. 选择硬件报告")
            print("2. 选择 macOS 版本")
            print("3. 自定义 ACPI 补丁")
            print("4. 自定义 Kexts")
            print("5. 自定义 SMBIOS 型号")
            print("6. 构建 OpenCore EFI")
            print("")
            print("Q. 退出")
            print("")

            option = self.u.request_input("选择一个选项：")
            if option.lower() == "q":
                self.u.exit_program()
           
            if option == "1":
                hardware_report_path, hardware_report = self.select_hardware_report()
                hardware_report, native_macos_version, ocl_patched_macos_version = self.c.check_compatibility(hardware_report)
                macos_version = self.select_macos_version(hardware_report, native_macos_version, ocl_patched_macos_version)
                customized_hardware, disabled_devices, needs_oclp = self.h.hardware_customization(hardware_report, macos_version)
                smbios_model = self.s.select_smbios_model(customized_hardware, macos_version)
                if not self.ac.ensure_dsdt():
                    self.ac.select_acpi_tables()
                self.ac.select_acpi_patches(customized_hardware, disabled_devices)
                needs_oclp = self.k.select_required_kexts(customized_hardware, macos_version, needs_oclp, self.ac.patches)
                self.s.smbios_specific_options(customized_hardware, smbios_model, macos_version, self.ac.patches, self.k)

            if not hardware_report_path:
                self.u.head()
                print("\n\n")
                print("\033[1;93m请先选择一个硬件报告。\033[0m")
                print("\n\n")
                self.u.request_input("按回车键返回...")
                continue

            if option == "2":
                macos_version = self.select_macos_version(hardware_report, native_macos_version, ocl_patched_macos_version)
                customized_hardware, disabled_devices, needs_oclp = self.h.hardware_customization(hardware_report, macos_version)
                smbios_model = self.s.select_smbios_model(customized_hardware, macos_version)
                needs_oclp = self.k.select_required_kexts(customized_hardware, macos_version, needs_oclp, self.ac.patches)
                self.s.smbios_specific_options(customized_hardware, smbios_model, macos_version, self.ac.patches, self.k)
            elif option == "3":
                self.ac.customize_patch_selection()
            elif option == "4":
                self.k.kext_configuration_menu(macos_version)
            elif option == "5":
                smbios_model = self.s.customize_smbios_model(customized_hardware, smbios_model, macos_version)
                self.s.smbios_specific_options(customized_hardware, smbios_model, macos_version, self.ac.patches, self.k)
            elif option == "6":
                if needs_oclp and not self.show_oclp_warning():
                    macos_version = self.select_macos_version(hardware_report, native_macos_version, ocl_patched_macos_version)
                    customized_hardware, disabled_devices, needs_oclp = self.h.hardware_customization(hardware_report, macos_version)
                    smbios_model = self.s.select_smbios_model(customized_hardware, macos_version)
                    needs_oclp = self.k.select_required_kexts(customized_hardware, macos_version, needs_oclp, self.ac.patches)
                    self.s.smbios_specific_options(customized_hardware, smbios_model, macos_version, self.ac.patches, self.k)
                    continue

                try:
                    self.o.gather_bootloader_kexts(self.k.kexts, macos_version)
                except Exception as e:
                    print("\033[91m错误：{}\033[0m".format(e))
                    print("")
                    self.u.request_input("按回车键继续...")
                    continue
                
                self.build_opencore_efi(customized_hardware, disabled_devices, smbios_model, macos_version, needs_oclp)
                self.before_using_efi(hardware_report, customized_hardware)

                self.u.head("结果")
                print("")
                print("您的 {} OpenCore EFI 已构建完成，位于:".format(customized_hardware.get("Motherboard").get("Name")))
                print("\t{}".format(self.result_dir))
                print("")
                self.u.request_input("按回车键返回主菜单...")

if __name__ == '__main__':
    update_flag = updater.Updater().run_update()
    if update_flag:
        os.execv(sys.executable, ['python3'] + sys.argv)

    o = OCPE()
    while True:
        try:
            o.main()
        except Exception as e:
            o.u.head("发生错误")
            print("")
            print(traceback.format_exc())
            o.u.request_input()