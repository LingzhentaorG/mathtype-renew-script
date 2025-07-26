# MathType 30天试用期续杯工具

## 简介
这个工具包提供了自动卸载、清理和重新安装MathType 7.8的方法，用于在30天试用期结束后重置试用期。

## 包含文件
- `renew_mathtype_trial.py` - Python脚本（推荐）
- `MathType-win-zh-7.8.2.441.exe` - MathType 7.8.2中文版安装包
- `Network administrator's manual.md` - 官方网络管理员手册

## 使用方法

### 使用Python脚本
1. 确保已安装Python 3.6或更高版本
2. 右键点击`renew_mathtype_trial.py`，选择"以管理员身份运行"
3. 按照提示操作即可

## 操作步骤
脚本会自动执行以下操作：

1. **静默卸载MathType**
   - 使用官方卸载命令：Setup.exe -Q -R

2. **删除安装目录**
   - 删除默认安装目录（通常为 `C:\Program Files (x86)\MathType` 或 `C:\Program Files\MathType`）
   - 如果文件被占用，会提示用户手动删除

3. **清理注册表**
   - 删除 `HKEY_CURRENT_USER\Software\JavaSoft\Prefs\com\wiris\editor\license`
   - 删除 `HKEY_CURRENT_USER\Software\Install Options` 中的 `Options7.8`

4. **重新安装**
   - 使用静默安装模式
   - 安装到默认目录（通常为 `C:\Program Files (x86)\MathType` 或 `C:\Program Files\MathType`）
   - 自动创建新30天试用期

5. **自动启动**
   - 安装完成后自动启动MathType
   - 用户可立即验证试用期状态

## 注意事项

### 重要提醒
- **必须**以管理员身份运行脚本
- 关闭所有MathType相关程序（Word、MathType等）
- 安装过程中不要中断操作
- 如果提示文件被占用，请手动结束相关进程

### 常见问题

#### 1. 权限问题
如果提示权限不足：
- 右键选择"以管理员身份运行"
- 或关闭UAC后重试

#### 2. 文件被占用
如果删除目录失败：
- 打开任务管理器
- 结束所有MathType相关进程
- 手动删除默认安装目录（通常为 `C:\Program Files (x86)\MathType` 或 `C:\Program Files\MathType`）

#### 3. 安装失败
- 检查安装包是否完整
- 确保有足够的磁盘空间
- 检查杀毒软件是否拦截

#### 4. 试用期未重置
- 确保注册表清理成功
- 检查是否还有其他注册表残留
- 重启电脑后重试

## 手动操作指南

### 手动卸载
```batch
"C:\Program Files (x86)\MathType\Setup.exe" -Q -R
```

### 手动删除注册表
1. Win+R打开运行，输入`regedit`
2. 导航到：
   - `计算机\HKEY_CURRENT_USER\Software\JavaSoft\Prefs\com\wiris\editor\license`
   - `计算机\HKEY_CURRENT_USER\Software\Install Options`
3. 删除对应项

### 手动安装
```batch
MathType-win-zh-7.8.2.441.exe /S
```

## 技术支持
如遇到问题，请检查：
1. 是否以管理员身份运行
2. 安装包是否完整
3. 目标目录是否有权限
4. 杀毒软件是否拦截

## 免责声明
本工具仅供学习研究使用，请支持正版软件。使用本工具造成的任何问题，开发者不承担任何责任。