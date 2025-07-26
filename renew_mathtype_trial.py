#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MathType 7.8 试用期续杯脚本
自动卸载、清理并重新安装MathType以重置30天试用期
"""

import os
import sys
import subprocess
import shutil
import winreg
import ctypes
from pathlib import Path

class MathTypeRenewer:
    def __init__(self):
        self.installer_path = os.path.join(os.path.dirname(__file__), "MathType-win-zh-7.8.2.441.exe")
        # 使用MathType默认安装路径
        if os.environ.get("ProgramFiles(x86)"):
            self.install_dir = os.path.join(os.environ.get("ProgramFiles(x86)", ""), "MathType")
        else:
            self.install_dir = os.path.join(os.environ.get("ProgramFiles", ""), "MathType")
        self.registry_paths = [
            r"Software\JavaSoft\Prefs\com\wiris\editor\license",
            r"Software\Install Options"
        ]
        
    def is_admin(self):
        """检查是否以管理员权限运行"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def run_as_admin(self):
        """以管理员权限重新运行脚本"""
        if not self.is_admin():
            print("需要管理员权限，正在请求提升权限...")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)
    
    def silent_uninstall(self):
        """静默卸载MathType"""
        print("正在静默卸载MathType...")
        uninstall_path = r"C:\Program Files (x86)\MathType\Setup.exe"
        
        if os.path.exists(uninstall_path):
            try:
                cmd = [uninstall_path, "-Q", "-R"]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                if result.returncode == 0:
                    print("✓ MathType已成功卸载")
                    return True
                else:
                    print(f"卸载失败: {result.stderr}")
                    return False
            except subprocess.TimeoutExpired:
                print("卸载超时，可能需要手动确认")
                return False
            except Exception as e:
                print(f"卸载出错: {e}")
                return False
        else:
            print("未找到卸载程序，可能MathType未安装")
            return True
    
    def delete_directory(self):
        """删除安装目录"""
        print(f"正在删除目录: {self.install_dir}")
        
        if os.path.exists(self.install_dir):
            try:
                # 先尝试正常删除
                shutil.rmtree(self.install_dir)
                print("✓ 目录已成功删除")
                return True
            except PermissionError as e:
                print(f"权限错误: {e}")
                return self.force_delete_directory()
            except Exception as e:
                print(f"删除失败: {e}")
                return self.force_delete_directory()
        else:
            print("目录不存在，无需删除")
            return True
    
    def force_delete_directory(self):
        """强制删除目录（处理进程占用）"""
        print("检测到文件被占用，准备强制删除...")
        
        # 使用Windows的rmdir命令强制删除
        try:
            cmd = ["cmd", "/c", f"rmdir /s /q \"{self.install_dir}\""]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ 使用强制删除成功")
                return True
            else:
                print("强制删除失败，需要用户手动操作")
                self.prompt_manual_delete()
                return False
        except Exception as e:
            print(f"强制删除出错: {e}")
            self.prompt_manual_delete()
            return False
    
    def prompt_manual_delete(self):
        """提示用户手动删除目录"""
        print("\n" + "="*50)
        print("需要手动删除目录")
        print(f"请手动删除以下目录：{self.install_dir}")
        print("步骤：")
        print("1. 关闭所有MathType相关进程")
        print("2. 打开文件资源管理器")
        print("3. 导航到D:\\MyApplications")
        print("4. 删除mathtype7文件夹")
        print("5. 按任意键继续...")
        print("="*50)
        input("完成删除后按Enter键继续...")
    
    def delete_registry_keys(self):
        """删除注册表相关键值"""
        print("正在清理注册表...")
        
        # 删除HKEY_CURRENT_USER下的注册表项
        for reg_path in self.registry_paths:
            try:
                # 删除license文件夹
                if "license" in reg_path:
                    try:
                        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path)
                        print(f"✓ 已删除注册表项: {reg_path}")
                    except FileNotFoundError:
                        print(f"注册表项不存在: {reg_path}")
                    except OSError as e:
                        print(f"删除注册表项失败: {reg_path} - {e}")
                
                # 删除Install Options中的Options7.8
                elif "Install Options" in reg_path:
                    try:
                        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS) as key:
                            try:
                                winreg.DeleteValue(key, "Options7.8")
                                print("✓ 已删除注册表值: Options7.8")
                            except FileNotFoundError:
                                print("注册表值不存在: Options7.8")
                    except FileNotFoundError:
                        print(f"注册表项不存在: {reg_path}")
                        
            except Exception as e:
                print(f"处理注册表时出错: {e}")
    
    def install_mathtype(self):
        """重新安装MathType"""
        print("正在重新安装MathType...")
        
        if not os.path.exists(self.installer_path):
            print(f"安装包不存在: {self.installer_path}")
            return False
        
        # 确保安装目录存在
        os.makedirs(self.install_dir, exist_ok=True)
        
        try:
            # 静默安装到指定目录
            cmd = [
                self.installer_path,
                "/S",  # 静默模式
                f"/DIR={self.install_dir}"  # 指定安装目录
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✓ MathType已成功重新安装")
                print(f"安装目录: {self.install_dir}")
                return True
            else:
                print(f"安装失败: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("安装超时，请检查安装过程")
            return False
        except Exception as e:
            print(f"安装出错: {e}")
            return False
    
    def verify_installation(self):
        """验证安装是否成功"""
        # 检查多个可能的安装位置
        possible_paths = [
            os.path.join(self.install_dir, "MathType.exe"),
            r"C:\Program Files (x86)\MathType\MathType.exe",
            r"C:\Program Files\MathType\MathType.exe",
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "MathType", "MathType.exe"),
            os.path.join(os.environ.get("ProgramFiles", ""), "MathType", "MathType.exe")
        ]