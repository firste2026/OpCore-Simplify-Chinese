from Scripts.datasets import os_data
import random

class KextInfo:
    def __init__(self, name, description, category, required = False, min_darwin_version = (), max_darwin_version = (), requires_kexts = [], conflict_group_id = None, github_repo = {}, download_info = {}):
        self.name = name
        self.description = description
        self.category = category
        self.required = required
        self.min_darwin_version = min_darwin_version or os_data.get_lowest_darwin_version()
        self.max_darwin_version = max_darwin_version or os_data.get_latest_darwin_version()
        self.requires_kexts = requires_kexts
        self.conflict_group_id = conflict_group_id
        self.github_repo = github_repo
        self.download_info = download_info
        self.checked = required

kexts = [
    KextInfo(
        name = "Lilu", 
        description = "用于任意 kext、库和程序补丁",
        category = "Required",
        required = True,
        github_repo = {
            "owner": "acidanthera",
            "repo": "Lilu"
        }
    ),
    KextInfo(
        name = "VirtualSMC", 
        description = "内核中的高级 Apple SMC 模拟器",
        category = "Required",
        required = True,
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "SMCBatteryManager", 
        description = "管理、监控和报告电池状态",
        category = "VirtualSMC Plugins",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "SMCDellSensors", 
        description = "启用戴尔计算机上的风扇监控和控制",
        category = "VirtualSMC Plugins",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "SMCLightSensor", 
        description = "允许系统使用环境光传感器设备",
        category = "VirtualSMC Plugins",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "SMCProcessor", 
        description = "管理 Intel CPU 温度传感器",
        category = "VirtualSMC Plugins",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "SMCRadeonSensors", 
        description = "提供 AMD GPU 温度读数",
        category = "VirtualSMC Plugins",
        min_darwin_version = "18.0.0",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "ChefKissInc",
            "repo": "SMCRadeonSensors"
        },
        download_info = {
            "id": int("".join(random.choices('0123456789', k=9))), 
            "url": "https://nightly.link/ChefKissInc/SMCRadeonSensors/workflows/main/master/Artifacts.zip"
        }
    ),
    KextInfo(
        name = "SMCSuperIO", 
        description = "监控硬件传感器和控制风扇速度",
        category = "VirtualSMC Plugins",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "VirtualSMC"
        }
    ),
    KextInfo(
        name = "NootRX", 
        description = "rDNA 2 独立显卡支持补丁 Kext",
        category = "Graphics",
        min_darwin_version = "20.5.0",
        requires_kexts = ["Lilu"],
        conflict_group_id = "GPU",
        github_repo = {
            "owner": "ChefKissInc",
            "repo": "NootRX"
        },
        download_info = {
            "id": int("".join(random.choices('0123456789', k=9))), 
            "url": "https://nightly.link/ChefKissInc/NootRX/workflows/main/master/Artifacts.zip"
        }
    ),
    KextInfo(
        name = "NootedRed", 
        description = "AMD Vega 集成显卡支持 Kext",
        category = "Graphics",
        min_darwin_version = "19.0.0",
        requires_kexts = ["Lilu"],
        conflict_group_id = "GPU",
        github_repo = {
            "owner": "ChefKissInc",
            "repo": "NootedRed"
        },
        download_info = {
            "id": int("".join(random.choices('0123456789', k=9))), 
            "url": "https://nightly.link/ChefKissInc/NootedRed/workflows/main/master/Artifacts.zip"
        }
    ),
    KextInfo(
        name = "WhateverGreen", 
        description = "GPU 所需的各种补丁预支持",
        category = "Graphics",
        requires_kexts = ["Lilu"],
        conflict_group_id = "GPU",
        github_repo = {
            "owner": "acidanthera",
            "repo": "WhateverGreen"
        }
    ),
    KextInfo(
        name = "AppleALC", 
        description = "非官方支持编解码器的原生 macOS HD 音频",
        category = "Audio",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "AppleALC"
        }
    ),
    KextInfo(
        name = "AirportBrcmFixup", 
        description = "非原生 Broadcom Wi-Fi 卡所需补丁",
        category = "Wi-Fi",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "AirportBrcmFixup"
        }
    ),
    KextInfo(
        name = "AirportItlwm", 
        description = "Intel Wi-Fi 驱动程序，支持原生 macOS Wi-Fi 界面",
        category = "Wi-Fi",
        conflict_group_id = "IntelWiFi",
        github_repo = {
            "owner": "OpenIntelWireless",
            "repo": "itlwm"
        }
    ),
    KextInfo(
        name = "corecaptureElCap", 
        description = "启用旧款 Qualcomm Atheros 无线网卡",
        category = "Wi-Fi",
        min_darwin_version = "18.0.0",
        max_darwin_version = "24.99.99",
        requires_kexts = ["IO80211ElCap"],
        download_info = {
            "id": 348147192, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Wifi/corecaptureElCap-v1.0.2.zip"
        }
    ),
    KextInfo(
        name = "IO80211ElCap", 
        description = "启用旧款 Qualcomm Atheros 无线网卡",
        category = "Wi-Fi",
        min_darwin_version = "18.0.0",
        max_darwin_version = "24.99.99",
        requires_kexts = ["corecaptureElCap"],
        download_info = {
            "id": 128321732, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Wifi/IO80211ElCap-v2.0.1.zip"
        }
    ),
    KextInfo(
        name = "IO80211FamilyLegacy", 
        description = "启用旧款 Apple 无线适配器",
        category = "Wi-Fi",
        min_darwin_version = "23.0.0",
        requires_kexts = ["AMFIPass", "IOSkywalkFamily"],
        download_info = {
            "id": 817294638, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/main/payloads/Kexts/Wifi/IO80211FamilyLegacy-v1.0.0.zip"
        }
    ),
    KextInfo(
        name = "IOSkywalkFamily", 
        description = "Intel Wi-Fi 驱动程序，伪装为以太网并通过 Heliport 连接 Wi-Fi",
        category = "Wi-Fi",
        min_darwin_version = "23.0.0",
        requires_kexts = ["AMFIPass", "IO80211FamilyLegacy"],
        download_info = {
            "id": 926584761, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/main/payloads/Kexts/Wifi/IOSkywalkFamily-v1.2.0.zip"
        }
    ),
    KextInfo(
        name = "itlwm", 
        description = "Intel Wi-Fi 驱动程序，伪装为以太网并通过 Heliport 连接 Wi-Fi",
        category = "Wi-Fi",
        conflict_group_id = "IntelWiFi",
        github_repo = {
            "owner": "OpenIntelWireless",
            "repo": "itlwm"
        }
    ),
    KextInfo(
        name = "Ath3kBT", 
        description = "上传固件以启用 Atheros 蓝牙支持",
        category = "Bluetooth",
        max_darwin_version = "20.99.99",
        requires_kexts = ["Ath3kBTInjector"],
        github_repo = {
            "owner": "zxystd",
            "repo": "AthBluetoothFirmware"
        }
    ),
    KextInfo(
        name = "Ath3kBTInjector", 
        description = "上传固件以启用 Atheros 蓝牙支持",
        category = "Bluetooth",
        max_darwin_version = "20.99.99",
        requires_kexts = ["Ath3kBT"],
        github_repo = {
            "owner": "zxystd",
            "repo": "AthBluetoothFirmware"
        }
    ),
    KextInfo(
        name = "BlueToolFixup", 
        description = "补丁蓝牙栈以支持第三方网卡",
        category = "Bluetooth",
        min_darwin_version = "21.0.0",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrcmPatchRAM"
        }
    ),
    KextInfo(
        name = "BrcmBluetoothInjector", 
        description = "在旧版本上启用 Broadcom 蓝牙开关",
        category = "Bluetooth",
        max_darwin_version = "20.99.99",
        requires_kexts = ["BrcmBluetoothInjector", "BrcmFirmwareData", "BrcmPatchRAM2", "BrcmPatchRAM3"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrcmPatchRAM"
        }
    ),
    KextInfo(
        name = "BrcmFirmwareData", 
        description = "为基于 Broadcom RAMUSB 的设备应用 PatchRAM 更新",
        category = "Bluetooth",
        requires_kexts = ["BlueToolFixup", "BrcmBluetoothInjector", "BrcmPatchRAM2", "BrcmPatchRAM3"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrcmPatchRAM"
        }
    ),
    KextInfo(
        name = "BrcmPatchRAM2", 
        description = "为基于 Broadcom RAMUSB 的设备应用 PatchRAM 更新",
        category = "Bluetooth",
        max_darwin_version = "18.99.99",
        requires_kexts = ["BlueToolFixup", "BrcmBluetoothInjector", "BrcmFirmwareData", "BrcmPatchRAM3"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrcmPatchRAM"
        }
    ),
    KextInfo(
        name = "BrcmPatchRAM3", 
        description = "为基于 Broadcom RAMUSB 的设备应用 PatchRAM 更新",
        category = "Bluetooth",
        min_darwin_version = "19.0.0",
        requires_kexts = ["BlueToolFixup", "BrcmBluetoothInjector", "BrcmFirmwareData", "BrcmPatchRAM2"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrcmPatchRAM"
        }
    ),
    KextInfo(
        name = "IntelBluetoothFirmware", 
        description = "上传固件以启用 Intel 蓝牙支持",
        category = "Bluetooth",
        requires_kexts = ["BlueToolFixup", "IntelBTPatcher", "IntelBluetoothInjector"],
        github_repo = {
            "owner": "lshbluesky",
            "repo": "IntelBluetoothFirmware"
        }
    ),
    KextInfo(
        name = "IntelBTPatcher", 
        description = "修复 Intel 蓝牙错误以改善连接性",
        category = "Bluetooth",
        requires_kexts = ["Lilu", "BlueToolFixup", "IntelBluetoothFirmware", "IntelBluetoothInjector"],
        github_repo = {
            "owner": "lshbluesky",
            "repo": "IntelBluetoothFirmware"
        }
    ),
    KextInfo(
        name = "IntelBluetoothInjector", 
        description = "在旧版本上启用 Intel 蓝牙开关",
        category = "Bluetooth",
        max_darwin_version = "20.99.99",
        requires_kexts = ["BlueToolFixup", "IntelBluetoothFirmware", "IntelBTPatcher"],
        github_repo = {
            "owner": "lshbluesky",
            "repo": "IntelBluetoothFirmware"
        }
    ),
    KextInfo(
        name = "AppleIGB", 
        description = "支持 Intel IGB 以太网控制器",
        category = "Ethernet",
        github_repo = {
            "owner": "donatengit",
            "repo": "AppleIGB"
        },
        download_info = {
            "id": 736194363, 
            "url": "https://github.com/lzhoang2801/lzhoang2801.github.io/raw/main/public/extra-files/AppleIGB-v5.11.4.zip"
        }
    ),
    KextInfo(
        name = "AppleIGC", 
        description = "支持 Intel 2.5G 以太网 (i225/i226)", 
        category = "Ethernet",
        github_repo = {
            "owner": "SongXiaoXi",
            "repo": "AppleIGC"
        }
    ),
    KextInfo(
        name = "AtherosE2200Ethernet", 
        description = "支持 Atheros E2200 系列", 
        category = "Ethernet",
        github_repo = {
            "owner": "Mieze",
            "repo": "AtherosE2200Ethernet"
        }
    ),
    KextInfo(
        name = "CatalinaBCM5701Ethernet", 
        description = "支持 Broadcom BCM57XX 以太网系列",
        category = "Ethernet",
        min_darwin_version = "20.0.0",
        download_info = {
            "id": 821327912,
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Ethernet/CatalinaBCM5701Ethernet-v1.0.2.zip"
        }
    ),
    KextInfo(
        name = "HoRNDIS", 
        description = "使用 Android 手机的 USB 共享模式上网",
        category = "Ethernet",
        github_repo = {
            "owner": "TomHeaven",
            "repo": "HoRNDIS"
        },
        download_info = {
            "id": 79378595,
            "url": "https://github.com/TomHeaven/HoRNDIS/releases/download/rel9.3_2/Release.zip"
        }
    ),
    KextInfo(
        name = "IntelLucy",
        description = "支持 Intel X500 系列",
        category = "Ethernet",
        github_repo = {
            "owner": "Mieze",
            "repo": "IntelLucy"
        }
    ),
    KextInfo(
        name = "IntelMausiEthernet", 
        description = "macOS 的 Intel 以太网 LAN 驱动程序",
        category = "Ethernet",
        github_repo = {
            "owner": "CloverHackyColor",
            "repo": "IntelMausiEthernet"
        }
    ),
    KextInfo(
        name = "LucyRTL8125Ethernet", 
        description = "支持 Realtek RTL8125 系列", 
        category = "Ethernet",
        github_repo = {
            "owner": "Mieze",
            "repo": "LucyRTL8125Ethernet"
        }
    ),
    KextInfo(
        name = "NullEthernet", 
        description = "当不存在受支持的网络硬件时创建虚拟以太网", 
        category = "Ethernet",
        github_repo = {
            "owner": "RehabMan",
            "repo": "os-x-null-ethernet"
        },
        download_info = {
            "id": 182736492, 
            "url": "https://bitbucket.org/RehabMan/os-x-null-ethernet/downloads/RehabMan-NullEthernet-2016-1220.zip"
        }
    ),
    KextInfo(
        name = "RealtekRTL8100", 
        description = "支持 Realtek RTL8100 系列", 
        category = "Ethernet",
        github_repo = {
            "owner": "Mieze",
            "repo": "RealtekRTL8100"
        },
        download_info = {
            "id": 10460478, 
            "url": "https://github.com/lzhoang2801/lzhoang2801.github.io/raw/main/public/extra-files/RealtekRTL8100-v2.0.1.zip"
        }
    ),
    KextInfo(
        name = "RealtekRTL8111", 
        description = "支持 Realtek RTL8111/8168 系列", 
        category = "Ethernet",
        github_repo = {
            "owner": "Mieze",
            "repo": "RTL8111_driver_for_OS_X"
        },
        download_info = {
            "id": 130015132, 
            "url": "https://github.com/Mieze/RTL8111_driver_for_OS_X/releases/download/2.4.2/RealtekRTL8111-V2.4.2.zip"
        }
    ),
    KextInfo(
        name = "GenericUSBXHCI", 
        description = "修复某些 Ryzen APU 基础系统上的 USB 3.0 问题",
        category = "USB",
        github_repo = {
            "owner": "RattletraPM",
            "repo": "GUX-RyzenXHCIFix"
        }
    ),
    KextInfo(
        name = "USBToolBox", 
        description = "灵活的 USB 映射",
        category = "USB",
        github_repo = {
            "owner": "USBToolBox",
            "repo": "kext"
        }
    ),
    KextInfo(
        name = "UTBDefault", 
        description = "启用所有 USB 端口（假设无端口限制）",
        category = "USB",
        requires_kexts = ["USBToolBox"],
        github_repo = {
            "owner": "USBToolBox",
            "repo": "kext"
        }
    ),
    KextInfo(
        name = "XHCI-unsupported", 
        description = "为不受支持的 xHCI 控制器启用 USB 3.0 支持",
        category = "USB",
        github_repo = {
            "owner": "daliansky",
            "repo": "OS-X-USB-Inject-All"
        },
        download_info = {
            "id": 185465401, 
            "url": "https://github.com/daliansky/OS-X-USB-Inject-All/releases/download/v0.8.0/XHCI-unsupported.kext.zip"
        }
    ),
    KextInfo(
        name = "AlpsHID", 
        description = "为 Alps I2C 触控板带来原生多点触控支持",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "blankmac",
            "repo": "AlpsHID"
        }
    ),
    KextInfo(
        name = "VoodooInput", 
        description = "为任意输入源提供 Magic Trackpad 2 软件模拟",
        category = "Input",
        github_repo = {
            "owner": "acidanthera",
            "repo": "VoodooInput"
        }
    ),
    KextInfo(
        name = "VoodooPS2Controller", 
        description = "支持 PS/2 键盘、触控板和鼠标",
        category = "Input",
        github_repo = {
            "owner": "acidanthera",
            "repo": "VoodooPS2"
        }
    ),
    KextInfo(
        name = "VoodooRMI", 
        description = "基于 SMBus/I2C 的 Synaptic 触控板 Kext",
        category = "Input",
        github_repo = {
            "owner": "VoodooSMBus",
            "repo": "VoodooRMI"
        }
    ),
    KextInfo(
        name = "VoodooSMBus", 
        description = "i2c-i801 + ELAN SMBus Touchpad kext",
        category = "Input",
        min_darwin_version = "18.0.0",
        github_repo = {
            "owner": "VoodooSMBus",
            "repo": "VoodooSMBus"
        }
    ),
    KextInfo(
        name = "VoodooI2C", 
        description = "Intel I2C 控制器和从设备驱动程序",
        category = "Input",
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "VoodooI2CAtmelMXT", 
        description = "Atmel MXT I2C 触摸屏的卫星 Kext",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "VoodooI2CELAN", 
        description = "ELAN I2C 触控板的卫星 Kext",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "VoodooI2CFTE", 
        description = "基于 FTE 触控板的卫星 Kext",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "VoodooI2CHID", 
        description = "HID I2C 或 ELAN1200+ 输入设备的卫星 Kext",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "VoodooI2CSynaptics", 
        description = "Synaptics I2C 触控板的卫星 Kext",
        category = "Input",
        requires_kexts = ["VoodooI2C"],
        github_repo = {
            "owner": "VoodooI2C",
            "repo": "VoodooI2C"
        }
    ),
    KextInfo(
        name = "AsusSMC", 
        description = "支持华硕笔记本电脑的环境光传感器、键盘背光和功能键",
        category = "Brand Specific",
        max_darwin_version = "23.99.99",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "hieplpvip",
            "repo": "AsusSMC"
        }
    ),
    KextInfo(
        name = "BigSurface", 
        description = "适用于所有 Surface 相关硬件的完全集成 Kext",
        category = "Brand Specific",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "Xiashangning",
            "repo": "BigSurface"
        }
    ),
    KextInfo(
        name = "YogaSMC", 
        description = "启用同步 SMC 键、控制传感器和管理厂商特定功能的支持",
        category = "Brand Specific",
        requires_kexts = ["Lilu", "VirtualSMC"],
        github_repo = {
            "owner": "zhen-zen",
            "repo": "YogaSMC"
        }
    ),
    KextInfo(
        name = "CtlnaAHCIPort", 
        description = "改进对某些 SATA 控制器的支持", 
        category = "Storage",
        min_darwin_version = "20.0.0",
        conflict_group_id = "SATA",
        download_info = {
            "id": 927362352,
            "url": "https://raw.githubusercontent.com/lzhoang2801/lzhoang2801.github.io/refs/heads/main/public/extra-files/CtlnaAHCIPort-v3.4.1.zip",
            "sha256": "c8cf54f8b98995d076f365765025068e3d612f6337e279774203441c06f1a474"
        }
    ),
    KextInfo(
        name = "SATA-unsupported", 
        description = "改进对某些 SATA 控制器的支持", 
        category = "Storage",
        max_darwin_version = "19.99.99",
        conflict_group_id = "SATA",
        download_info = {
            "id": 239471623,
            "url": "https://raw.githubusercontent.com/lzhoang2801/lzhoang2801.github.io/refs/heads/main/public/extra-files/SATA-unsupported-v0.9.2.zip",
            "sha256": "942395056afa1e1d0e06fb501ab7c0130bf687d00e08b02c271844769056a57c"
        }
    ),
    KextInfo(
        name = "NVMeFix", 
        description = "解决 NVMe SSD 的兼容性和性能问题", 
        category = "Storage",
        min_darwin_version = "18.0.0",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "NVMeFix"
        }
    ),
    KextInfo(
        name = "RealtekCardReader", 
        description = "Realtek PCIe/USB SD 卡读卡器驱动程序", 
        category = "Card Reader",
        min_darwin_version = "18.0.0",
        max_darwin_version = "23.99.99",
        requires_kexts = ["RealtekCardReaderFriend"],
        conflict_group_id = "RealtekCardReader",
        github_repo = {
            "owner": "0xFireWolf",
            "repo": "RealtekCardReader"
        }
    ),
    KextInfo(
        name = "RealtekCardReaderFriend", 
        description = "使系统信息能够识别您的 Realtek 读卡器",
        category = "Card Reader",
        min_darwin_version = "18.0.0",
        max_darwin_version = "22.99.99",
        requires_kexts = ["Lilu", "RealtekCardReader"],
        github_repo = {
            "owner": "0xFireWolf",
            "repo": "RealtekCardReaderFriend"
        }
    ), 
    KextInfo(
        name = "Sinetek-rtsx", 
        description = "Realtek PCIe SD 卡读卡器驱动程序",
        category = "Card Reader",
        conflict_group_id = "RealtekCardReader",
        github_repo = {
            "owner": "cholonam",
            "repo": "Sinetek-rtsx"
        }
    ),
    KextInfo(
        name = "AmdTscSync", 
        description = "适用于 AMD CPU 的修改版 VoodooTSCSync",
        category = "TSC Synchronization",
        conflict_group_id = "TSC",
        github_repo = {
            "owner": "naveenkrdy",
            "repo": "AmdTscSync"
        }
    ),
    KextInfo(
        name = "VoodooTSCSync", 
        description = "同步 Intel CPU 上 TSC 的内核扩展",
        category = "TSC Synchronization",
        conflict_group_id = "TSC",
        github_repo = {
            "owner": "RehabMan",
            "repo": "VoodooTSCSync"
        },
        download_info = {
            "id": 823728912, 
            "url": "https://github.com/lzhoang2801/lzhoang2801.github.io/raw/refs/heads/main/public/extra-files/VoodooTSCSync-v1.1.zip"
        }
    ),
    KextInfo(
        name = "CpuTscSync", 
        description = "用于 Intel CPU 上 TSC 同步和禁用 xcpm_urgency 的 Lilu 插件",
        category = "TSC Synchronization",
        requires_kexts = ["Lilu"],
        conflict_group_id = "TSC",
        github_repo = {
            "owner": "acidanthera",
            "repo": "CpuTscSync"
        }
    ),
    KextInfo(
        name = "ForgedInvariant", 
        description = "用于 AMD 和 Intel 上同步 TSC 的即插即用 Kext",
        category = "TSC Synchronization",
        requires_kexts = ["Lilu"],
        conflict_group_id = "TSC",
        github_repo = {
            "owner": "ChefKissInc",
            "repo": "ForgedInvariant"
        },
        download_info = {
            "id": int("".join(random.choices('0123456789', k=9))), 
            "url": "https://nightly.link/ChefKissInc/ForgedInvariant/workflows/main/master/Artifacts.zip"
        }
    ),
    KextInfo(
        name = "AMFIPass", 
        description = "amfi=0x80 启动参数的替代品",
        category = "Extras",
        min_darwin_version = "20.0.0",
        requires_kexts = ["Lilu"],
        download_info = {
            "id": 926491527, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/main/payloads/Kexts/Acidanthera/AMFIPass-v1.4.1-RELEASE.zip"
        }
    ),
    KextInfo(
        name = "ASPP-Override", 
        description = "重新启用 Intel Sandy Bridge CPU 的 CPU 电源管理",
        category = "Extras",
        min_darwin_version = "21.4.0",
        download_info = {
            "id": 913826421,
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Misc/ASPP-Override-v1.0.1.zip"
        }
    ),
    KextInfo(
        name = "AppleIntelCPUPowerManagement", 
        description = "在旧款 Intel CPU 上重新启用 CPU 电源管理", 
        category = "Extras",
        min_darwin_version = "22.0.0",
        download_info = {
            "id": 736296452, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Misc/AppleIntelCPUPowerManagement-v1.0.0.zip"
        }
    ),
    KextInfo(
        name = "AppleIntelCPUPowerManagementClient", 
        description = "在旧款 Intel CPU 上重新启用 CPU 电源管理", 
        category = "Extras",
        min_darwin_version = "22.0.0",
        download_info = {
            "id": 932639706, 
            "url": "https://github.com/dortania/OpenCore-Legacy-Patcher/raw/refs/heads/main/payloads/Kexts/Misc/AppleIntelCPUPowerManagementClient-v1.0.0.zip"
        }
    ),
    KextInfo(
        name = "AppleMCEReporterDisabler", 
        description = "禁用 AppleMCEReporter.kext 以防止内核恐慌", 
        category = "Extras",
        download_info = {
            "id": 738162736, 
            "url": "https://github.com/acidanthera/bugtracker/files/3703498/AppleMCEReporterDisabler.kext.zip"
        }
    ),
    KextInfo(
        name = "BrightnessKeys", 
        description = "无需 DSDT 补丁的亮度键处理程序",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "BrightnessKeys"
        }
    ),
    KextInfo(
        name = "CPUFriend", 
        description = "动态电源管理数据注入（需要 CPUFriendDataProvider）",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "CPUFriend"
        }
    ),
    KextInfo(
        name = "CpuTopologyRebuild", 
        description = "优化 Intel Alder Lake 及更新 CPU 的核心配置",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "b00t0x",
            "repo": "CpuTopologyRebuild"
        }
    ),
    KextInfo(
        name = "CryptexFixup", 
        description = "安装 Rosetta cryptex 的各种补丁",
        category = "Extras",
        min_darwin_version = "22.0.0",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "CryptexFixup"
        }
    ),
    KextInfo(
        name = "ECEnabler", 
        description = "允许读取超过 1 字节长的嵌入式控制器字段",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "1Revenger1",
            "repo": "ECEnabler"
        }
    ),
    KextInfo(
        name = "FeatureUnlock", 
        description = "在不受支持的硬件上启用额外功能",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "FeatureUnlock"
        }
    ),
    KextInfo(
        name = "HibernationFixup", 
        description = "修复休眠兼容性问题",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "HibernationFixup"
        }
    ),
    KextInfo(
        name = "NoTouchID", 
        description = "避免带有 Touch ID 传感器的板 ID 在身份验证对话框中的延迟",
        category = "Extras",
        min_darwin_version = "17.5.0",
        max_darwin_version = "19.6.0",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "al3xtjames",
            "repo": "NoTouchID"
        }
    ),
    KextInfo(
        name = "RestrictEvents", 
        description = "阻止不需要的进程并解锁功能",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "RestrictEvents"
        }
    ),
    KextInfo(
        name = "RTCMemoryFixup", 
        description = "模拟 CMOS (RTC) 内存中的某些偏移",
        category = "Extras",
        requires_kexts = ["Lilu"],
        github_repo = {
            "owner": "acidanthera",
            "repo": "RTCMemoryFixup"
        }
    )
]

kext_index_by_name = {kext.name: index for index, kext in enumerate(kexts)}