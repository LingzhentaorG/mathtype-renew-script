# MathType 7.8 试用期续杯工具

<p align="center">
  <img src="https://img.shields.io/badge/MathType-7.8.2-blue.svg" alt="MathType Version">
  <img src="https://img.shields.io/badge/Python-3.6+-green.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <b>自动重置 MathType 30 天试用期的便捷工具</b>
</p>

---

## 📋 目录

- [简介](#-简介)
- [功能特性](#-功能特性)
- [系统要求](#-系统要求)
- [文件说明](#-文件说明)
- [使用方法](#-使用方法)
- [工作流程](#-工作流程)
- [常见问题](#-常见问题)
- [手动操作指南](#-手动操作指南)
- [技术细节](#-技术细节)
- [更新日志](#-更新日志)
- [免责声明](#-免责声明)

---

## 🎯 简介

MathType 7.8 试用期续杯工具是一个自动化脚本，帮助用户在 MathType 30 天试用期结束后，通过完全卸载、清理残留文件和注册表、重新安装的方式重置试用期。

**核心优势：**
- ✅ 一键自动化操作，无需手动干预
- ✅ 完整的清理流程，确保试用期彻底重置
- ✅ 静默安装模式，无需手动点击安装向导
- ✅ 智能错误处理和用户提示

---

## ✨ 功能特性

| 功能 | 描述 |
|------|------|
| 🔧 **自动卸载** | 使用官方卸载程序静默卸载现有 MathType |
| 🧹 **深度清理** | 删除安装目录及残留文件 |
| 🗑️ **注册表清理** | 清除许可证相关的注册表项 |
| 📦 **静默安装** | 自动重新安装 MathType 到默认目录 |
| ✔️ **安装验证** | 检查安装是否成功完成 |
| 🔐 **权限管理** | 自动请求管理员权限 |

---

## 💻 系统要求

### 操作系统
- Windows 10 / Windows 11
- Windows 8.1 / Windows 8（可能兼容）

### 软件依赖
- **Python 3.6** 或更高版本
- **MathType 7.8.2** 安装包（已包含在工具包中）

### 权限要求
- 必须以 **管理员身份** 运行脚本

---

## 📁 文件说明

```
mathtype-renew-script/
├── 📄 renew_mathtype_trial.py          # 主脚本文件（Python）
├── 📦 MathType-win-zh-7.8.2.441.exe    # MathType 7.8.2 中文版安装包
├── 📖 Network administrator's manual.md # 官方网络管理员手册
└── 📋 README.md                         # 本说明文档
```

### 文件详解

#### `renew_mathtype_trial.py`
主脚本文件，包含以下核心类和方法：

- **`MathTypeRenewer`** 类：续杯操作的核心类
  - `is_admin()` - 检查是否以管理员权限运行
  - `run_as_admin()` - 请求管理员权限
  - `silent_uninstall()` - 静默卸载 MathType
  - `delete_directory()` - 删除安装目录
  - `force_delete_directory()` - 强制删除（处理占用情况）
  - `delete_registry_keys()` - 清理注册表项
  - `install_mathtype()` - 重新安装 MathType
  - `verify_installation()` - 验证安装结果
  - `run()` - 执行完整的续杯流程

#### `MathType-win-zh-7.8.2.441.exe`
MathType 7.8.2 中文版官方安装包，支持静默安装参数。

---

## 🚀 使用方法

### 方法一：右键运行（推荐）

#### 前提条件：配置 .py 文件右键运行

Windows 默认不支持直接右键运行 .py 文件，需要进行以下配置：

**步骤 1：安装 Python（已安装可跳过）**
1. 下载并安装 Python 3.6+：https://www.python.org/downloads/
2. **重要**：安装时勾选 **"Add Python to PATH"** 和 **"Install py launcher"**

**步骤 2：配置文件关联**

以管理员身份运行 CMD，执行以下命令：

```batch
:: 将 .py 文件关联到 Python
assoc .py=Python.File

:: 设置打开方式
ftype Python.File="C:\Windows\py.exe" "%%1" %%*
```

**步骤 3：添加右键菜单（可选，推荐）**

以管理员身份运行 CMD，执行以下注册表命令：

```batch
:: 添加"以管理员身份运行"到 .py 文件的右键菜单
reg add "HKEY_CLASSES_ROOT\Python.File\shell\runas" /ve /t REG_SZ /d "以管理员身份运行" /f
reg add "HKEY_CLASSES_ROOT\Python.File\shell\runas\command" /ve /t REG_SZ /d "\"C:\Windows\py.exe\" \"%1\" %*" /f

:: 添加普通运行选项
reg add "HKEY_CLASSES_ROOT\Python.File\shell\open" /ve /t REG_SZ /d "运行" /f
reg add "HKEY_CLASSES_ROOT\Python.File\shell\open\command" /ve /t REG_SZ /d "\"C:\Windows\py.exe\" \"%1\" %*" /f
```

**验证配置：**
配置完成后，右键点击 `renew_mathtype_trial.py` 文件，应该能看到：
- 🏃 **"运行"** 选项
- 🛡️ **"以管理员身份运行"** 选项

#### 运行脚本

1. 找到 `renew_mathtype_trial.py` 文件
2. **右键点击** → 选择 **"以管理员身份运行"**
3. 等待脚本自动完成所有操作
4. 按提示操作即可

### 方法二：命令行运行

1. 以管理员身份打开 PowerShell 或 CMD
2. 切换到脚本所在目录：
   ```powershell
   cd D:\Desktop\mathtype-renew-script
   ```
3. 运行脚本：
   ```powershell
   python renew_mathtype_trial.py
   ```

### 方法三：Python 直接执行

```powershell
python "D:\Desktop\mathtype-renew-script\renew_mathtype_trial.py"
```

---

## 🔄 工作流程

脚本执行时会按以下顺序自动完成操作：

```
┌─────────────────────────────────────────────────────────────┐
│                    MathType 续杯流程                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  步骤 1/5    🔧 静默卸载                                     │
│             └─ 运行 Setup.exe -Q -R                         │
│                                                             │
│  步骤 2/5    🧹 清理安装目录                                 │
│             └─ 删除 C:\Program Files (x86)\MathType         │
│                                                             │
│  步骤 3/5    🗑️ 清理注册表                                   │
│             └─ 删除 license 注册表项                         │
│             └─ 删除 Options7.8 值                           │
│                                                             │
│  步骤 4/5    📦 重新安装                                     │
│             └─ 静默安装到默认目录                            │
│                                                             │
│  步骤 5/5    ✔️ 验证安装                                     │
│             └─ 检查 MathType.exe 是否存在                    │
│                                                             │
│  ✅ 完成     试用期已重置为 30 天                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ❓ 常见问题

### Q1: 提示"需要管理员权限"怎么办？

**解决方法：**
1. 右键点击脚本，选择"以管理员身份运行"
2. 或者在 PowerShell 中以管理员身份运行：
   ```powershell
   Start-Process python -ArgumentList "renew_mathtype_trial.py" -Verb RunAs
   ```

### Q2: 提示"文件被占用，删除失败"怎么办？

**解决方法：**
1. 打开任务管理器（Ctrl + Shift + Esc）
2. 结束以下进程：
   - `MathType.exe`
   - `MathTypeServer.exe`
   - Microsoft Word（如果打开了 MathType 插件）
3. 手动删除目录：`C:\Program Files (x86)\MathType`
4. 重新运行脚本

### Q3: 安装包不存在怎么办？

**错误提示：**
```
安装包不存在: D:\Desktop\mathtype-renew-script\MathType-win-zh-7.8.2.441.exe
```

**解决方法：**
1. 确认安装包文件名是否正确
2. 将安装包放置在与脚本相同的目录
3. 或修改脚本中的 `installer_path` 变量指向正确的路径

### Q4: 试用期未重置怎么办？

**排查步骤：**
1. 确认注册表清理成功（查看脚本输出）
2. 手动检查注册表项是否存在：
   - `HKEY_CURRENT_USER\Software\JavaSoft\Prefs\com\wiris\editor\license`
   - `HKEY_CURRENT_USER\Software\Install Options\Options7.8`
3. 重启电脑后再次运行脚本
4. 检查是否有其他 MathType 配置文件残留

### Q5: 杀毒软件拦截怎么办？

**解决方法：**
1. 将脚本添加到杀毒软件白名单
2. 暂时关闭实时保护（不推荐）
3. 使用 Windows Defender 的用户可以添加排除项：
   - 设置 → 更新和安全 → Windows 安全中心 → 病毒和威胁防护 → 排除项

### Q6: 脚本运行后没有任何反应？

**可能原因及解决：**
1. **Python 未安装** - 安装 Python 3.6+ 并添加到 PATH
2. **文件关联问题** - 使用命令行方式运行
3. **权限问题** - 确保以管理员身份运行

---

## 🔧 手动操作指南

如果自动脚本无法正常工作，可以手动执行以下步骤：

### 1. 手动卸载 MathType

以管理员身份运行 CMD，执行：

```batch
"C:\Program Files (x86)\MathType\Setup.exe" -Q -R
```

### 2. 手动删除安装目录

删除以下目录（如果存在）：

```
C:\Program Files (x86)\MathType
C:\Program Files\MathType
```

### 3. 手动清理注册表

1. 按 `Win + R`，输入 `regedit`，回车
2. 导航到以下路径并删除：
   - `HKEY_CURRENT_USER\Software\JavaSoft\Prefs\com\wiris\editor\license`
   - `HKEY_CURRENT_USER\Software\Install Options` 中的 `Options7.8` 值

⚠️ **警告：** 修改注册表前请备份！

### 4. 手动安装 MathType

以管理员身份运行 CMD，执行：

```batch
MathType-win-zh-7.8.2.441.exe /S
```

安装完成后，MathType 将拥有新的 30 天试用期。

---

## 🔍 技术细节

### 注册表清理说明

脚本会清理以下注册表项，这些位置存储了 MathType 的许可证信息：

| 注册表路径 | 说明 |
|-----------|------|
| `HKEY_CURRENT_USER\Software\JavaSoft\Prefs\com\wiris\editor\license` | 存储许可证密钥和激活状态 |
| `HKEY_CURRENT_USER\Software\Install Options\Options7.8` | 存储安装选项和试用期信息 |

### 静默安装参数

MathType 安装包支持以下静默安装参数：

| 参数 | 说明 |
|------|------|
| `/S` | 静默模式，无用户交互 |
| `/DIR=路径` | 指定安装目录 |

### 卸载参数

| 参数 | 说明 |
|------|------|
| `-Q` | 静默模式 |
| `-R` | 卸载模式 |

---

## 📝 更新日志

### v1.1.0 (2025-03-14)
- ✅ 添加脚本入口点，支持直接双击运行
- ✅ 完善 `verify_installation()` 方法
- ✅ 添加 `run()` 方法执行完整流程
- ✅ 优化错误处理和用户提示
- ✅ 更新 README 文档

### v1.0.0 (初始版本)
- 🎉 首次发布
- 实现基本的卸载、清理、安装功能
- 支持注册表清理

---

## ⚠️ 免责声明

**本工具仅供学习研究使用，请支持正版软件。**

1. 使用本工具造成的任何问题，开发者不承担任何责任
2. 请在法律允许的范围内使用本工具
3. 建议购买正版 MathType 许可证以获得完整功能和技术支持
4. 本工具不会破解软件，仅通过重新安装方式重置试用期

---

## 📞 技术支持

如遇到问题，请检查以下事项：

- [ ] 是否以管理员身份运行
- [ ] Python 版本是否为 3.6 或更高
- [ ] 安装包是否完整且未损坏
- [ ] 目标目录是否有写入权限
- [ ] 杀毒软件是否拦截了脚本

### 反馈问题

如果遇到无法解决的问题，请提供以下信息：
1. 操作系统版本
2. Python 版本
3. 完整的错误提示信息
4. 脚本输出日志

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

---

<p align="center">
  <b>⭐ 如果本工具对你有帮助，欢迎 Star 支持！</b>
</p>
