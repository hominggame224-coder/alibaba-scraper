#!/bin/bash
# 阿里巴巴游戏机爬虫 - macOS/Linux 快速启动脚本
# 直接运行 PyQt5 GUI 应用

echo ""
echo "==================================================="
echo "  🎮 阿里巴巴游戏机爬虫 - GUI应用启动器"
echo "==================================================="
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    echo ""
    echo "请先安装 Python3:"
    echo "  macOS: brew install python3"
    echo "  Ubuntu: sudo apt-get install python3"
    exit 1
fi

echo "✅ 检测到 Python"
python3 --version

# 检查依赖
echo ""
echo "📦 检查依赖..."

python3 -c "import PyQt5" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  缺少 PyQt5，正在安装..."
    pip3 install PyQt5 -q
fi

python3 -c "import pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  缺少 pandas，正在安装..."
    pip3 install pandas -q
fi

python3 -c "import openpyxl" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  缺少 openpyxl，正在安装..."
    pip3 install openpyxl -q
fi

# 启动应用
echo ""
echo "🚀 启动应用..."
echo ""

python3 gui_app.py
