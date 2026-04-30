# -*- coding: utf-8 -*-
"""
OpCore Simplify - 汉化翻译文件
Chinese Translation File for OpCore Simplify
"""

class Translator:
    def __init__(self):
        self.translations = {
            # 主菜单和通用文本
            "Select hardware report": "选择硬件报告",
            "Note:": "注意：",
            "Ensure you are using the latest version of Hardware Sniffer before generating the hardware report.": "在生成硬件报告之前，请确保您使用的是最新版本的 Hardware Sniffer。",
            "Hardware Sniffer will not collect information related to Resizable BAR option of GPU (disabled by default) and monitor connections in Windows PE.": "Hardware Sniffer 在 Windows PE 环境下不会收集与 GPU 的 Resizable BAR 选项（默认禁用）和显示器连接相关的信息。",
            "E. Export hardware report (Recommended)": "E. 导出硬件报告（推荐）",
            "Q. Quit": "Q. 退出",
            "Drag and drop your hardware report here (.JSON)": "将您的硬件报告拖放到此处 (.JSON)",
            " or type \"E\" to export": " 或输入 \"E\" 导出",
            "Exporting Hardware Report": "正在导出硬件报告",
            "Exporting hardware report to {}...": "正在导出硬件报告到 {}...",
            "Could not export the hardware report. {}.": "无法导出硬件报告。{}。",
            "Please try again or using Hardware Sniffer manually.": "请重试或手动使用 Hardware Sniffer。",
            "Press Enter to go back...": "按回车键返回...",
            "Suggestion:": "建议：",
            "Please re-export the hardware report and try again.": "请重新导出硬件报告并重试。",
            
            # OpenCore Legacy Patcher 警告
            "OpenCore Legacy Patcher Warning": "OpenCore Legacy Patcher 警告",
            "1. OpenCore Legacy Patcher is the only solution to enable dropped GPU and Broadcom WiFi": "1. OpenCore Legacy Patcher 是启用被放弃的 GPU 和 Broadcom WiFi 的唯一解决方案",
            "   support in newer macOS versions, as well as to bring back AppleHDA for macOS Tahoe 26.": "   支持较新版本的 macOS，并为 macOS Tahoe 26 恢复 AppleHDA。",
            "2. OpenCore Legacy Patcher disables macOS security features including SIP and AMFI, which may": "2. OpenCore Legacy Patcher 会禁用 macOS 安全功能（包括 SIP 和 AMFI），这可能",
            "   lead to issues such as requiring full installers for updates, application crashes, and": "   导致一些问题，例如需要完整安装程序进行更新、应用程序崩溃和",
            "   system instability.": "   系统不稳定。",
            "3. OpenCore Legacy Patcher is not officially supported for Hackintosh community.": "3. OpenCore Legacy Patcher 不被黑苹果社区官方支持。",
            "Important:": "重要提示：",
            "Please consider these risks carefully before proceeding.": "请在继续之前仔细考虑这些风险。",
            "Support for macOS Tahoe 26:": "对 macOS Tahoe 26 的支持：",
            "To patch macOS Tahoe 26, you must download OpenCore-Patcher 3.0.0 or newer from": "要修补 macOS Tahoe 26，您必须从以下地址下载 OpenCore-Patcher 3.0.0 或更高版本：",
            "my repository: ": "我的仓库：",
            " on GitHub.": " 在 GitHub 上。",
            "Older or official Dortania releases are NOT supported for Tahoe 26.": "较旧版本或官方的 Dortania 版本不支持 Tahoe 26。",
            "Do you want to continue with OpenCore Legacy Patcher? (yes/No): ": "您要继续使用 OpenCore Legacy Patcher 吗？(是/否): ",
            
            # macOS 版本选择
            "Select macOS Version": "选择 macOS 版本",
            "Suggested macOS version:": "建议的 macOS 版本：",
            "For better compatibility and stability, we suggest you to use only {} or older.": "为了获得更好的兼容性和稳定性，我们建议您仅使用 {} 或更早版本。",
            "Available macOS versions:": "可用的 macOS 版本：",
            "To select a major version, enter the number (e.g., 19).": "要选择主要版本，请输入数字（例如 19）。",
            "To specify a full version, use the Darwin version format (e.g., 22.4.6).": "要指定完整版本，请使用 Darwin 版本格式（例如 22.4.6）。",
            "Please enter the macOS version you want to use (default: {}): ": "请输入您想使用的 macOS 版本（默认：{}）：",
            
            # EFI 构建
            "Building OpenCore EFI": "正在构建 OpenCore EFI",
            "Copying EFI base to results folder": "正在将 EFI 基础文件复制到结果文件夹",
            "Applying ACPI patches": "正在应用 ACPI 补丁",
            "Copying kexts and snapshotting to config.plist": "正在复制 kext 并快照到 config.plist",
            "Generating config.plist": "正在生成 config.plist",
            "Cleaning up unused drivers, resources, and tools": "正在清理未使用的驱动程序、资源和工具",
            "OpenCore EFI build complete.": "OpenCore EFI 构建完成。",
            
            # 使用前提示
            "Before Using EFI": "在使用 EFI 之前",
            "Please complete the following steps:": "请完成以下步骤：",
            "* BIOS/UEFI Settings Required:": "* BIOS/UEFI 设置要求：",
            "* USB Mapping:": "* USB 映射：",
            "    - Use USBToolBox tool to map USB ports.": "    - 使用 USBToolBox 工具映射 USB 端口。",
            "    - Add created UTBMap.kext into the {} folder.": "    - 将创建的 UTBMap.kext 添加到 {} 文件夹。",
            "    - Remove UTBDefault.kext in the {} folder.": "    - 从 {} 文件夹中删除 UTBDefault.kext。",
            "    - Edit config.plist:": "    - 编辑 config.plist：",
            "        - Use ProperTree to open your config.plist.": "        - 使用 ProperTree 打开您的 config.plist。",
            "        - Run OC Snapshot by pressing Command/Ctrl + R.": "        - 按 Command/Ctrl + R 运行 OC 快照。",
            "        - If you have more than 15 ports on a single controller, enable the XhciPortLimit patch.": "        - 如果单个控制器上有超过 15 个端口，请启用 XhciPortLimit 补丁。",
            "        - Save the file when finished.": "        - 完成后保存文件。",
            
            # 主界面
            "  Hardware Report:": "  硬件报告：",
            "Not selected": "未选择",
            "  macOS Version:": "  macOS 版本：",
            "  SMBIOS:": "  SMBIOS：",
            "  Disabled Devices:": "  禁用的设备：",
            "1. Select Hardware Report": "1. 选择硬件报告",
            "2. Select macOS Version": "2. 选择 macOS 版本",
            "3. Customize ACPI Patch": "3. 自定义 ACPI 补丁",
            "4. Customize Kexts": "4. 自定义 Kexts",
            "5. Customize SMBIOS Model": "5. 自定义 SMBIOS 模型",
            "6. Build OpenCore EFI": "6. 构建 OpenCore EFI",
            "Select an option: ": "选择一个选项：",
            "Please select a hardware report first.": "请先选择一个硬件报告。",
            "Press Enter to continue...": "按回车键继续...",
            "Result": "结果",
            "Your OpenCore EFI for {} has been built at:": "您的 {} 的 OpenCore EFI 已构建于：",
            "Press Enter to main menu...": "按回车键返回主菜单...",
            "An Error Occurred": "发生错误",
            
            # 程序退出
            "For more information, to report errors, or to contribute to the product:": "有关更多信息、报告错误或为产品做出贡献：",
            "Thank you for using our program!": "感谢您使用我们的程序！",
            "Press Enter to exit.": "按回车键退出。",
            
            # ACPI 表选择
            "Select ACPI Tables": "选择 ACPI 表",
            "Please drag and drop ACPI Tables folder here: ": "请将 ACPI 表文件夹拖放到此处：",
            
            # 兼容性检查
            "Compatibility Checker": "兼容性检查器",
            "Checking compatibility with macOS for the following devices:": "正在检查以下设备与 macOS 的兼容性：",
            "Unchecked": "未检查",
            "Unsupported": "不支持",
            "Maximum support up to {}": "最高支持到 {}",
            "{} to {}": "{} 到 {}",
            "Up to {}": "最高到 {}",
            "No GPU found!": "未找到 GPU！",
            "Please make sure to export the hardware report with the GPU information": "请确保导出包含 GPU 信息的硬件报告",
            "and try again.": "并重试。",
            "Missing required SSE4.x instruction set.": "缺少必需的 SSE4.x 指令集。",
            "Your CPU is not supported by macOS versions newer than Sierra (10.12).": "您的 CPU 不支持比 Sierra (10.12) 更新的 macOS 版本。",
            "You cannot install macOS without a supported GPU.": "没有支持的 GPU 您无法安装 macOS。",
            "Please do NOT spam my inbox or issue tracker about this issue anymore!": "请不要再就这个问题向我的收件箱或问题跟踪器发送垃圾邮件！",
            
            # 硬件定制
            "Hardware Customization": "硬件定制",
            "Build EFI for UEFI? (Yes/no): ": "为 UEFI 构建 EFI？(是/否): ",
            "Invalid selection, please try again.": "选择无效，请重试。",
            "Device Selection Summary": "设备选择摘要",
            "Selected devices:": "已选择的设备：",
            "Type          Device                                     Device ID": "类型          设备                                     设备 ID",
            "All other devices of the same type have been disabled.": "所有其他同类型设备已被禁用。",
            "*** Multiple {} Devices Detected": "*** 检测到多个 {} 设备",
            "macOS works best with only one {} device enabled.": "macOS 在仅启用一个 {} 设备时工作最佳。",
            "Multiple active GPUs can cause kext conflicts in macOS.": "多个活动的 GPU 可能导致 macOS 中的 kext 冲突。",
            "Please select a {} combination configuration:": "请选择一个 {} 组合配置：",
            "Please select which {} device you want to use:": "请选择您想使用哪个 {} 设备：",
            "Select a {} combination (1-{}): ": "选择一个 {} 组合 (1-{}): ",
            "Select a {} device (1-{}): ": "选择一个 {} 设备 (1-{}): ",
            "Invalid option. Please try again.": "选项无效，请重试。",
            "Please enter a valid number.": "请输入有效的数字。",
            "Compatibility:": "兼容性：",
            "OCLP Compatibility:": "OCLP 兼容性：",
            "Device ID:": "设备 ID：",
            
            # Kext 选择
            "Select Required Kernel Extensions": "选择必需的内核扩展",
            "Checking for required kernel extensions...": "正在检查必需的内核扩展...",
            "Important: Black Screen Fix": "重要提示：黑屏修复",
            "If you experience a black screen after verbose mode:": "如果在详细模式后遇到黑屏：",
            "    1. Use ProperTree to open config.plist": "    1. 使用 ProperTree 打开 config.plist",
            "    2. Navigate to NVRAM -> Add -> 7C436110-AB2A-4BBB-A880-FE41995C9F82 -> boot-args": "    2. 导航到 NVRAM -> Add -> 7C436110-AB2A-4BBB-A880-FE41995C9F82 -> boot-args",
            "    3. Remove \"-v debug=0x100 keepsyms=1\" from boot-args": "    3. 从 boot-args 中移除 \"-v debug=0x100 keepsyms=1\"",
            "Select kext for your AMD {} GPU (default: {}): ": "为您的 AMD {} GPU 选择 kext（默认：{}）：",
            "Invalid selection, using recommended option: {}": "选择无效，正在使用推荐选项：{}",
            "Select kext for your Intel WiFi device (default: {}): ": "为您的 Intel WiFi 设备选择 kext（默认：{}）：",
            "Apply OCLP root patch to fix iServices? (yes/No): ": "应用 OCLP 根补丁修复 iServices？(是/否): ",
            "Kext Compatibility Check": "Kext 兼容性检查",
            "Incompatible kexts for the current macOS version ({}):": "当前 macOS 版本 ({}) 的不兼容 kext：",
            " - Lilu Plugin": " - Lilu 插件",
            "With Lilu plugins, using the \"-lilubetaall\" boot argument will force them to load.": "使用 Lilu 插件时，使用 \"-lilubetaall\" 启动参数将强制加载它们。",
            "Forcing unsupported kexts can cause system instability. Proceed with caution.": "强制使用不支持的 kext 可能导致系统不稳定。请谨慎操作。",
            "Do you want to force load {} on the unsupported macOS version? (yes/No): ": "您要在不支持的 macOS 版本上强制加载 {} 吗？(是/否): ",
            "these kexts": "这些 kext",
            "this kext": "此 kext",
            
            # SMBIOS 选择
            "List of available SMBIOS:": "可用的 SMBIOS 列表：",
            "List of compatible SMBIOS:": "兼容的 SMBIOS 列表：",
            "Lines in gray indicate mac models that are not officially supported by {}.": "灰色行表示 {} 不官方支持的 Mac 型号。",
            "A. Show all models": "A. 显示所有型号",
            "C. Show compatible models only": "C. 仅显示兼容型号",
            "R. Restore default SMBIOS model ({})": "R. 恢复默认 SMBIOS 型号 ({})",
            "Select your option: ": "选择您的选项：",
            "B. Back": "B. 返回",
            
            # 编解码器布局
            "List of Codec Layouts:": "编解码器布局列表：",
            "ID   Comment": "ID   注释",
            "The default layout may not be optimal.": "默认布局可能不是最优的。",
            "Test different layouts to find what works best for your system.": "测试不同的布局以找到最适合您系统的。",
            "Enter the ID of the codec layout you want to use (default: {}): ": "输入您想使用的编解码器布局 ID（默认：{}）：",
            
            # 文件收集
            "Gathering Files": "正在收集文件",
            "Please wait for download OpenCorePkg, kexts and macserial...": "请等待下载 OpenCorePkg、kexts 和 macserial...",
            "Could not find download URL for {}.": "找不到 {} 的下载 URL。",
            "Latest version of {} already downloaded.": "最新版本的 {} 已下载。",
            "Updating": "正在更新",
            "{}...": "{}...",
            "from {}": "来自 {}",
            "Could not download {} at this time. Please try again later.": "暂时无法下载 {}。请稍后重试。",
            "Please wait for download {}...": "请等待下载 {}...",
            "Using previously downloaded version of {}.": "正在使用之前下载的版本 {}。",
            "Unable to download {} at this time": "暂时无法下载 {}",
            "Please try again later or apply them manually.": "请稍后重试或手动应用它们。",
            "Go to {} to download {} manually.": "前往 {} 手动下载 {}。",
            "Failed to download {}.": "下载 {} 失败。",
            
            # 连续互通支持
            "Continuity Support:": "连续互通支持：",
            "Full (AirDrop, Handoff, Universal Clipboard, Instant Hotspot,...)": "完整（AirDrop、接力、通用剪贴板、即时热点等）",
            "Partial (Handoff and Universal Clipboard with AirportItlwm)": "部分（使用 AirportItlwm 的接力和通用剪贴板）",
            "Limited (No Continuity features available)": "有限（无连续互通功能可用）",
            "AirDrop, Universal Clipboard, Instant Hotspot,... not available": "AirDrop、通用剪贴板、即时热点等不可用",
            "Atheros cards are not recommended for macOS": "Atheros 卡不推荐用于 macOS",
            
            # 存储控制器
            "No storage controller found!": "未找到存储控制器！",
            "Please make sure to export the hardware report with the storage controller information": "请确保导出包含存储控制器信息的硬件报告",
            "Intel VMD controllers are not supported in macOS.": "macOS 不支持 Intel VMD 控制器。",
            "Please disable Intel VMD in the BIOS settings and try again with new hardware report.": "请在 BIOS 设置中禁用 Intel VMD 并使用新的硬件报告重试。",
            "No compatible storage controller for macOS was found!": "未找到与 macOS 兼容的存储控制器！",
            "Consider purchasing a compatible SSD NVMe for your system.": "考虑为您的系统购买兼容的 SSD NVMe。",
            "Western Digital NVMe SSDs are generally recommended for good macOS compatibility.": "通常推荐西部数据 NVMe SSD 以获得良好的 macOS 兼容性。",
            
            # 生物识别
            "Biometric authentication in macOS requires Apple T2 Chip,": "macOS 中的生物识别认证需要 Apple T2 芯片，",
            "which is not available for Hackintosh systems.": "这在黑苹果系统中不可用。",
            
            # 是/否选项
            "yes": "是",
            "no": "否",
            "Yes": "是",
            "No": "否",
            "YES": "是",
            "NO": "否",
        }
    
    def t(self, text):
        """翻译文本"""
        return self.translations.get(text, text)
    
    def tf(self, text, *args):
        """翻译并格式化文本"""
        translated = self.translations.get(text, text)
        return translated.format(*args) if args else translated

# 创建全局翻译器实例
translator = Translator()
_ = translator.t
_f = translator.tf
