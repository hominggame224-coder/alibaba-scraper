"""
PyInstaller 打包配置脚本
将 PyQt5 应用打包成可独立运行的 .exe 文件
"""

import os
import sys
from pathlib import Path

# PyInstaller 打包命令
WINDOWS_BUILD_CMD = """
pyinstaller --onefile ^
    --windowed ^
    --name "阿里巴巴游戏机爬虫" ^
    --icon=icon.ico ^
    --add-data "data:data" ^
    --hidden-import=PyQt5.QtCore ^
    --hidden-import=PyQt5.QtGui ^
    --hidden-import=PyQt5.QtWidgets ^
    --hidden-import=pandas ^
    --hidden-import=openpyxl ^
    gui_app.py
"""

MACOS_BUILD_CMD = """
pyinstaller --onefile \\
    --windowed \\
    --name "阿里巴巴游戏机爬虫" \\
    --icon=icon.icns \\
    --add-data "data:data" \\
    --hidden-import=PyQt5.QtCore \\
    --hidden-import=PyQt5.QtGui \\
    --hidden-import=PyQt5.QtWidgets \\
    --hidden-import=pandas \\
    --hidden-import=openpyxl \\
    gui_app.py
"""

LINUX_BUILD_CMD = """
pyinstaller --onefile \\
    --windowed \\
    --name "阿里巴巴游戏机爬虫" \\
    --add-data "data:data" \\
    --hidden-import=PyQt5.QtCore \\
    --hidden-import=PyQt5.QtGui \\
    --hidden-import=PyQt5.QtWidgets \\
    --hidden-import=pandas \\
    --hidden-import=openpyxl \\
    gui_app.py
"""


def print_instructions():
    """打印打包说明"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║          PyInstaller 应用打包说明                              ║
╚════════════════════════════════════════════════════════════════╝

【前置要求】
1. 安装所有依赖:
   pip install -r requirements.txt

2. 确保已安装 PyInstaller:
   pip install PyInstaller

3. 创建应用图标（可选）

【打包步骤】

【Windows 系统】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 打开命令提示符 (cmd) 或 PowerShell
2. 进入项目目录:
   cd alibaba-scraper

3. 运行打包命令:
   pyinstaller --onefile --windowed \\
     --name "阿里巴巴游戏机爬虫" \\
     --hidden-import=PyQt5.QtCore \\
     --hidden-import=PyQt5.QtGui \\
     --hidden-import=PyQt5.QtWidgets \\
     --hidden-import=pandas \\
     --hidden-import=openpyxl \\
     gui_app.py

4. 等待打包完成（通常 2-5 分钟）

5. 完成！应用在:
   dist/阿里巴巴游戏机爬虫.exe

【macOS 系统】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 打开终端 (Terminal)
2. 进入项目目录:
   cd alibaba-scraper

3. 运行打包命令:
   pyinstaller --onefile --windowed \\
     --name "阿里巴巴游戏机爬虫" \\
     --hidden-import=PyQt5.QtCore \\
     --hidden-import=PyQt5.QtGui \\
     --hidden-import=PyQt5.QtWidgets \\
     --hidden-import=pandas \\
     --hidden-import=openpyxl \\
     gui_app.py

4. 完成！应用在:
   dist/阿里巴巴��戏机爬虫.app

【Linux 系统】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 打开终端
2. 进入项目目录:
   cd alibaba-scraper

3. 运行打包命令:
   pyinstaller --onefile --windowed \\
     --name "阿里巴巴游戏机爬虫" \\
     --hidden-import=PyQt5.QtCore \\
     --hidden-import=PyQt5.QtGui \\
     --hidden-import=PyQt5.QtWidgets \\
     --hidden-import=pandas \\
     --hidden-import=openpyxl \\
     gui_app.py

4. 完成！应用在:
   dist/阿里巴巴游戏机爬虫

【打包输出说明】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
打包完成后，你会看到三个目录：

📁 build/           - 打包的中间文件（可删除）
📁 dist/            - ⭐ 可运行的应用在这里
📄 阿里巴巴游戏机爬虫.spec - PyInstaller 配置文件

【运行应用】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Windows:
  双击 dist/阿里巴巴游戏机爬虫.exe

macOS:
  打开 Finder → Applications → 双击应用
  或在终端: open dist/阿里巴巴游戏机爬虫.app

Linux:
  终端运行: ./dist/阿里巴巴游戏机爬虫

【分发应用】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 可以直接将 dist 文件夹中的应用发给别人
✅ 接收者无需安装 Python 或任何依赖
✅ 完全独立可运行

【优化打包】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
添加图标使应用更美观：

1. 准备图标文件：icon.ico (Windows) 或 icon.icns (macOS)
2. 修改打包命令，添加：
   --icon=icon.ico

3. 重新打包

【故障排除】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ "ModuleNotFoundError"
✅ 解决: pip install -r requirements.txt

❌ PyInstaller 未找到某些模块
✅ 解决: 使用 --hidden-import=module_name 参数

❌ 打包的应用启动很慢
✅ 正常: 首次启动会加载所有依赖，请耐心等待

❌ 应用无法生成 Excel
✅ 解决: 确保 data/ 目录在同一位置或使用 --add-data 参数

【其他选项】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--onefile       : 打包成单个 .exe 文件
--windowed      : 隐藏控制台窗口（只显示 GUI）
--icon=path     : 指定应用图标
--name=name     : 应用名称
--distpath=path : 输出目录

【自动打包脚本】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
使用 build.py 脚本自动打包（如果有的话）:
  python build.py

    """)


if __name__ == '__main__':
    print_instructions()
