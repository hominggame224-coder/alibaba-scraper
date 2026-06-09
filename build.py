"""
自动打包脚本 - 一键生成可执行应用
"""

import os
import sys
import platform
import subprocess
from pathlib import Path


def run_command(cmd):
    """运行命令"""
    print(f"\n📌 执行: {cmd}")
    result = os.system(cmd)
    if result != 0:
        print(f"❌ 命令执行失败")
        return False
    return True


def build_app():
    """构建应用"""
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║          🚀 阿里巴巴游戏机爬虫 - 应用打包                       ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    # 检查依赖
    print("\n✅ 检查依赖...")
    try:
        import PyQt5
        import pandas
        import openpyxl
        import PyInstaller
        print("✅ 所有依赖已安装")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return False
    
    # 确定系统
    system = platform.system()
    print(f"\n📱 系统: {system}")
    
    # 构建命令
    base_cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "阿里巴巴游戏机爬虫",
        "--hidden-import=PyQt5.QtCore",
        "--hidden-import=PyQt5.QtGui",
        "--hidden-import=PyQt5.QtWidgets",
        "--hidden-import=pandas",
        "--hidden-import=openpyxl",
    ]
    
    # 如果有图标文件，添加图标
    if Path("icon.ico").exists() and system == "Windows":
        base_cmd.extend(["--icon", "icon.ico"])
        print("✅ 检测到图标文件: icon.ico")
    
    if Path("icon.icns").exists() and system == "Darwin":
        base_cmd.extend(["--icon", "icon.icns"])
        print("✅ 检测到图标文件: icon.icns")
    
    # 添加数据目录
    if Path("data").exists():
        base_cmd.extend(["--add-data", "data:data"])
        print("✅ 包含 data 目录")
    
    base_cmd.append("gui_app.py")
    
    cmd = " ".join(base_cmd)
    
    # 执行打包
    print("\n🔨 开始打包应用...")
    print("这可能需要几分钟，请耐心等待...\n")
    
    if not run_command(cmd):
        return False
    
    # 检查输出
    dist_dir = Path("dist")
    if dist_dir.exists():
        print("\n✅ 打包成功！")
        
        if system == "Windows":
            app_path = dist_dir / "阿里巴巴游戏机爬虫.exe"
        elif system == "Darwin":
            app_path = dist_dir / "阿里巴巴游戏机爬虫.app"
        else:
            app_path = dist_dir / "阿里巴巴游戏机爬虫"
        
        if app_path.exists():
            print(f"\n📦 应用位置:")
            print(f"   {app_path.absolute()}")
            print(f"\n📊 文件大小: {app_path.stat().st_size / (1024*1024):.2f} MB")
            
            print(f"\n🎉 完成！现在可以:")
            print(f"   1. 直接运行应用")
            print(f"   2. 将 dist 文件夹分发给其他人")
            print(f"   3. 不需要 Python 环境即可运行")
            
            # 提示清理
            print(f"\n🧹 清理:")
            print(f"   可以删除 build 文件夹节省空间:")
            print(f"   rm -rf build  (或在文件管理器中手动删除)")
            
            return True
        else:
            print(f"❌ 应用文件未找到: {app_path}")
            return False
    else:
        print("❌ dist 目录不存在")
        return False


def main():
    try:
        success = build_app()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中止打包")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
