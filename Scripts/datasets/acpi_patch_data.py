class PatchInfo:
    def __init__(self, name, description, function_name):
        self.name = name
        self.description = description
        self.function_name = function_name
        self.checked = False

patches = [
    PatchInfo(
        name = "ALS",
        description = "模拟或启用环境光传感器设备以存储当前亮度/自动亮度级别",
        function_name = "ambient_light_sensor"
    ),
    PatchInfo(
        name = "APIC",
        description = "在 HEDT 系统上通过将第一个 CPU 条目指向活动 CPU 来避免内核恐慌",
        function_name = "fix_apic_processor_id"
    ),
    PatchInfo(
        name = "BATP",
        description = "在笔记本电脑上启用显示电池百分比",
        function_name = "battery_status_patch"
    ),
    PatchInfo(
        name = "BUS0",
        description = "添加系统管理总线设备以修复 AppleSMBus 问题",
        function_name = "add_system_management_bus_device"
    ),
    PatchInfo(
        name = "Disable Devices",
        description = "禁用不受支持的 PCI 设备，如 GPU、Wi-Fi 卡和 SD 卡读卡器",
        function_name = "disable_unsupported_device"
    ),
    PatchInfo(
        name = "FakeEC",
        description = "支持操作系统的虚拟嵌入式控制器（由 CorpNewt 开发）",
        function_name = "fake_embedded_controller"
    ),
    PatchInfo(
        name = "RCSP",
        description = "删除条件 ACPI 作用域声明",
        function_name = "remove_conditional_scope"
    ),
    PatchInfo(
        name = "CMOS",
        description = "修复 HP 实时时钟电源丢失 (005) 开机错误",
        function_name = "fix_hp_005_post_error"
    ),
    PatchInfo(
        name = "FixHPET",
        description = "修补 IRQ 冲突（由 CorpNewt 开发）",
        function_name = "fix_irq_conflicts"
    ),
    PatchInfo(
        name = "GPI0",
        description = "启用 GPIO 设备以使 I2C 触控板正常工作",
        function_name = "enable_gpio_device"
    ),
    PatchInfo(
        name = "IMEI",
        description = "创建虚拟 IMEI 设备以确保 Intel 集成显卡加速功能正常工作",
        function_name = "add_intel_management_engine"
    ),
    PatchInfo(
        name = "MCHC",
        description = "添加内存控制器集线器设备以修复 AppleSMBus",
        function_name = "add_memory_controller_device"
    ),
    PatchInfo(
        name = "PMC",
        description = "添加 PMCR 设备以为 300 系列主板启用 NVRAM 支持",
        function_name = "enable_nvram_support"
    ),
    PatchInfo(
        name = "PM (Legacy)",
        description = "阻止 CpuPm 和 Cpu0Ist ACPI 表以避免 Intel Ivy Bridge 及更旧 CPU 的恐慌",
        function_name = "drop_cpu_tables"
    ),
    PatchInfo(
        name = "PLUG",
        description = "将 CPU 对象重新定义为处理器并设置 plugin-type = 1（由 CorpNewt 开发）",
        function_name = "enable_cpu_power_management"
    ),
    PatchInfo(
        name = "PNLF",
        description = "定义 PNLF 设备以在笔记本电脑上启用背光控制",
        function_name = "enable_backlight_controls"
    ),
    PatchInfo(
        name = "RMNE",
        description = "创建虚拟以太网以允许 macOS 系统访问 iServices",
        function_name = "add_null_ethernet_device"
    ),
    PatchInfo(
        name = "RTC0",
        description = "创建新的 RTC 设备以解决 HEDT 系统上的 PCI 配置问题",
        function_name = "fix_system_clock_hedt"
    ),
    PatchInfo(
        name = "RTCAWAC",
        description = "上下文感知的 AWAC 禁用和 RTC 启用/虚拟/范围修复（由 CorpNewt 开发）",
        function_name = "fix_system_clock_awac"
    ),
    PatchInfo(
        name = "PRW",
        description = "修复 _PRW 方法中的睡眠状态值以防止 macOS 中立即唤醒",
        function_name = "instant_wake_fix"
    ),
    PatchInfo(
        name = "Surface Patch",
        description = "适用于所有 Surface Pro/Book/Laptop 硬件的特殊补丁",
        function_name = "surface_laptop_special_patch"
    ),
    PatchInfo(
        name = "UNC",
        description = "禁用未使用的 uncore 桥接器以防止 HEDT 系统上的内核恐慌",
        function_name = "fix_uncore_bridge"
    ),
    PatchInfo(
        name = "USB Reset",
        description = "禁用 USB 集线器设备以手动重建端口",
        function_name = "disable_usb_hub_devices"
    ),
    PatchInfo(
        name = "USBX",
        description = "创建 USBX 设备以注入 USB 电源属性",
        function_name = "add_usb_power_properties"
    ),
    PatchInfo(
        name = "WMIS",
        description = "某些型号忘记从 ThermalZone 返回结果",
        function_name = "return_thermal_zone"
    ),
    PatchInfo(
        name = "XOSI",
        description = "将操作系统伪装为 Windows，在 macOS 上启用被非 Windows 系统锁定的设备",
        function_name = "operating_system_patch"
    )
]