<br/>
<div align="center">
  <h3 align="center">OpCore Simplify</h3>

  <p align="center">
    这是一款专用工具，可简化 <a href="https://github.com/acidanthera/OpenCorePkg">OpenCore</a> EFI 创建过程，通过自动化基本设置流程并提供标准化配置。旨在减少手动操作，确保您的黑苹果之旅准确无误。
    <br />
    <br />
    <a href="#-特性">特性</a> •
    <a href="#-使用方法">使用方法</a> •
    <a href="#-贡献">贡献</a> •
    <a href="#-许可证">许可证</a> •
    <a href="#-致谢">致谢</a> •
    <a href="#-联系方式">联系方式</a>
  </p>
  
  <p align="center">
    <a href="https://trendshift.io/repositories/15410" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15410" alt="lzhoang2801%2FOpCore-Simplify | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  </p>
</div>

> [!NOTE]
> **OpenCore Legacy Patcher 3.0.0 – 现已支持 macOS Tahoe 26！**
> 
> 期待已久的 OpenCore Legacy Patcher 3.0.0 版本已经发布，为社区带来了对 **macOS Tahoe 26 的初步支持**！
> 
> 🚨 **请注意：**  
> - 只有来自 [lzhoang2801/OpenCore-Legacy-Patcher](https://github.com/lzhoang2801/OpenCore-Legacy-Patcher/releases/tag/3.0.0) 仓库的 OpenCore-Patcher 3.0.0 **才支持** macOS Tahoe 26（含早期补丁）。
> - 官方的 Dortania 发布版本或旧版补丁**无法用于** macOS Tahoe 26。  
>
> [!WARNING]
> 虽然 OpCore Simplify 大幅减少了设置时间，但黑苹果之旅仍然需要：
> - 了解 [Dortania 指南](https://dortania.github.io/OpenCore-Install-Guide/) 中的基本概念
> - 在安装过程中进行测试和故障排除
> - 以耐心和毅力解决出现的任何问题
>
> 我们的工具不保证首次安装就能成功，但它应该能帮助您顺利开始。

## ✨ **特性**

1. **全面的硬件和 macOS 支持**  
   完全支持现代硬件。使用 `Compatibility Checker`（兼容性检查器）来检查受支持/不支持的设备和 macOS 版本。

   | **组件**  | **支持情况**                                                                                       |
   |----------------|-----------------------------------------------------------------------------------------------------|
   | **CPU**        | Intel：Nehalem 和 Westmere（第 1 代）→ Arrow Lake（第 15 代/Core Ultra Series 2）<br> AMD：Ryzen 和 Threadripper，支持 [AMD Vanilla](https://github.com/AMD-OSX/AMD_Vanilla) |
   | **GPU**        | Intel 核显：Iron Lake（第 1 代）→ Ice Lake（第 10 代）<br> AMD APU：整个 Vega Raven ASIC 系列（Ryzen 1xxx → 5xxx，7x30 系列）<br> AMD 独显：Navi 23、Navi 22、Navi 21 代及更早系列<br> NVIDIA：Kepler、Pascal、Maxwell、Fermi、Tesla 代 |
   | **macOS**      | macOS High Sierra → macOS Tahoe |

2. **ACPI 补丁和 Kext**  
   根据硬件配置自动检测并添加 ACPI 补丁和 kext。
   
   - 集成 [SSDTTime](https://github.com/corpnewt/SSDTTime) 用于常见补丁（例如 FakeEC、FixHPET、PLUG、RTCAWAC）。
   - 包含自定义补丁：
      - 通过将第一个 CPU 条目指向活动 CPU、禁用 UNC0 设备并为 HEDT 系统创建新的 RTC 设备来防止内核恐慌。
      - 禁用不支持或未使用的 PCI 设备，例如 GPU（使用 Optimus 和 Bumblebee 方法或添加 disable-gpu 属性）、Wi-Fi 卡和 NVMe 存储控制器。
      - 修复 _PRW 方法（GPRW、UPRW、HP special）中的睡眠状态值以防止立即唤醒。
      - 添加设备包括 ALS0、BUS0、MCHC、PMCR、PNLF、RMNE、IMEI、USBX、XOSI，以及 Surface 补丁。
      - 启用 ALSD 和 GPI0 设备。

3. **自动更新**  
    在每次 EFI 构建之前，自动检查并更新来自 [Dortania Builds](https://dortania.github.io/builds/) 和 GitHub 发布的 OpenCorePkg 和 kext。
            
4. **EFI 配置**  
   基于广泛使用的来源和个人经验，应用额外的自定义设置。

   - 为某些在 macOS 中无法识别的 AMD GPU 伪装 GPU ID。
   - 对具有 P 核和 E 核的 Intel CPU 使用 CpuTopologyRebuild kext 以提升性能。
   - 禁用系统完整性保护（SIP）。
   - 为 Intel Pentium、Celeron、Core 和 Xeon 处理器伪装 CPU ID。
   - 为 AMD CPU 以及 Intel Pentium、Celeron、Xeon 和 Core 系列（从 Rocket Lake（第 11 代）及更新的世代）添加自定义 CPU 名称。
   - 添加补丁以允许使用不受支持的 SMBIOS 启动 macOS。
   - 添加 NVRAM 条目以绕过内部蓝牙控制器的检查。
   - 根据具体的可调整 BAR 信息正确配置 ResizeAppleGpuBars。
   - 当存在支持的独显时，允许在无头模式和驱动显示器之间灵活配置 Intel 核显。
   - 强制 Intel GPU 进入 VESA 模式（使用 HDMI 和 DVI 连接器）以简化安装过程。
   - 提供使用 OpenCore Legacy Patcher 所需的配置。
   - 为网络设备添加内置设备属性（修复使用 iServices 时出现"无法与服务器通信"的问题）和存储控制器（修复内部驱动器显示为外部的问题）。
   - 优先使用针对电源管理和性能优化的 SMBIOS。
   - 在 macOS Ventura 13 及更高版本上重新启用旧款 Intel CPU 的电源管理。
   - 为 itlwm kext 应用 WiFi 配置文件以在启动时启用自动 WiFi 连接。

   以及更多...

5. **轻松自定义**  
   除了应用的默认设置外，用户还可以根据需要进行进一步的自定义。

   - 自定义 ACPI 补丁、kext 和 SMBIOS 调整（**不推荐**）。
   - 在不受支持的 macOS 版本上强制加载 kext。

## 🚀 **使用方法**

1. **下载 OpCore Simplify**：
   - 点击 **Code** → **Download ZIP**，或通过此 [链接](https://github.com/lzhoang2801/OpCore-Simplify/archive/refs/heads/main.zip) 直接下载。  
   - 将下载的 ZIP 文件解压到所需位置。

   ![下载 OpCore Simplify](https://i.imgur.com/mcE7OSX.png)

2. **运行 OpCore Simplify**：
   - 在 **Windows** 上，运行 `OpCore-Simplify.bat`。
   - 在 **macOS** 上，运行 `OpCore-Simplify.command`。
   - 在 **Linux** 上，使用现有的 Python 解释器运行 `OpCore-Simplify.py`。

   ![OpCore Simplify 菜单](https://i.imgur.com/vTr1V9D.png)

3. **选择硬件报告**：
   - 在 Windows 上，将有一个选项 `E. Export hardware report`（导出硬件报告）。建议在构建时使用此选项以获得最佳的硬件配置和 BIOS 效果。
   - 或者，使用 [**Hardware Sniffer**](https://github.com/lzhoang2801/Hardware-Sniffer) 创建 `Report.json` 和 ACPI 转储以进行手动配置。

   ![选择硬件报告](https://i.imgur.com/MbRmIGJ.png)

   ![加载 ACPI 表](https://i.imgur.com/SbL6N6v.png)

   ![兼容性检查器](https://i.imgur.com/kuDGMmp.png)

4. **选择 macOS 版本和自定义 OpenCore EFI**：
   - 默认情况下，将为您的硬件选择最新的兼容 macOS 版本。
   - OpCore Simplify 将自动应用基本的 ACPI 补丁和 kext。 
   - 您可以根据需要手动审查和自定义这些设置。

   ![OpCore Simplify 菜单](https://i.imgur.com/TSk9ejy.png)

5. **构建 OpenCore EFI**：
   - 自定义所有选项后，选择 **Build OpenCore EFI** 以生成您的 EFI。
   - 工具将自动下载必要的引导加载程序和 kext，这可能需要几分钟时间。

   ![WiFi 配置文件提取器](https://i.imgur.com/71TkJkD.png)

   ![选择编解码器布局 ID](https://i.imgur.com/Mcm20EQ.png)

   ![构建 OpenCore EFI](https://i.imgur.com/deyj5de.png)

6. **USB 映射**：
   - 构建 EFI 后，按照步骤进行 USB 端口映射。

   ![结果](https://i.imgur.com/MIPigPF.png)

7. **创建 USB 安装器并安装 macOS**： 
   - 在 Windows 上使用 [**UnPlugged**](https://github.com/corpnewt/UnPlugged) 创建 USB macOS 安装器，或参考 [本指南](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/mac-install.html)（适用于 macOS）。
   - 如需故障排除，请参考 [OpenCore 故障排除指南](https://dortania.github.io/OpenCore-Install-Guide/troubleshooting/troubleshooting.html)。

> [!NOTE]
> 1. 成功安装后，如果需要 OpenCore Legacy Patcher，只需应用根补丁以激活缺失的功能（例如现代 Broadcom Wi-Fi 卡和图形加速）。
> 
> 2. 对于 AMD GPU，在应用 OpenCore Legacy Patcher 的根补丁后，您需要移除启动参数 `-radvesa`/`-amd_no_dgpu_accel` 以使图形加速正常工作。

## 🤝 **贡献**

我们**非常感谢**您的贡献！如果您有改进本项目的想法，欢迎 fork 仓库并创建 pull request，或提交带有 "enhancement" 标签的 issue。

不要忘记给项目 ⭐ star！感谢您的支持！🌟

## 📜 **许可证**

根据 BSD 3-Clause 许可证分发。有关更多信息，请参见 `LICENSE` 文件。

## 🙌 **致谢**

- [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) 和 [kexts](https://github.com/lzhoang2801/OpCore-Simplify/blob/main/Scripts/datasets/kext_data.py) – 本项目的核心支柱。
- [SSDTTime](https://github.com/corpnewt/SSDTTime) – SSDT 补丁工具。

## 📞 **联系方式**

> QQ 3314967083 &nbsp;&middot;&nbsp;
> 邮箱：3314967083@qq.com

