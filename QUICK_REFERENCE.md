# 🚀 快速参考指南 (Quick Reference)

## ⚡ 最常用命令

### 首次安装（一次性）
```bash
git clone https://github.com/hominggame224-coder/alibaba-scraper.git
cd alibaba-scraper
pip install -r requirements.txt
```

### 运行应用（三选一）

| 方式 | 命令 | 系统 |
|-----|------|------|
| 方式1 | `python gui_app.py` | 全部 |
| 方式2 | `run.bat` | Windows |
| 方式3 | `bash run.sh` | macOS/Linux |

### 打包成可执行文件
```bash
python build.py
```

完成后在 `dist/` 找到应用 📦

---

## 📁 项目文件结构

```
alibaba-scraper/
├── gui_app.py                 ⭐ GUI 桌面应用主文件
├── run.bat                    ⭐ Windows 快速启动
├── run.sh                     ⭐ macOS/Linux 快速启动
├── build.py                   ⭐ 一键打包脚本
├── scraper.py                 爬虫核心逻辑
├── config.py                  配置文件
├── requirements.txt           依赖列表
├── DESKTOP_APP_GUIDE.md       📖 完整使用手册
├── BUILD_GUIDE.md             📖 打包指南
├── QUICK_REFERENCE.md         📖 本文件
├── data/                      📁 输出数据文件夹
└── README.md                  📖 项目介绍
```

---

## 🎯 快速任务

### 任务1：我只想运行应用
```bash
# Windows
run.bat

# macOS/Linux
bash run.sh
```
✅ 完成！享受 GUI 界面

### 任务2：我想打包成 .exe 文件
```bash
python build.py
```
✅ 在 `dist/` 文件夹找到可执行文件

### 任务3：我想分享给别人
1. 运行 `python build.py`
2. 拷贝 `dist/` 文件夹中的应用
3. 直接发给对方，无需 Python！

### 任务4：我想修改爬取关键词
编辑 `scraper.py` 第 15-18 行：
```python
self.keywords = [
    'your_keyword_1',
    'your_keyword_2'
]
```

### 任务5：我遇到问题了
1. 查看 `DESKTOP_APP_GUIDE.md` 的常见问题部分
2. 检查 GUI 中的"运行日志"
3. 重新安装依赖：`pip install -r requirements.txt --upgrade`

---

## 🔍 诊断命令

### 检查 Python 版本（需要 3.7+）
```bash
python --version
```

### 检查 PyQt5 是否正确安装
```bash
python -c "import PyQt5; print('✅ PyQt5 OK')"
```

### 检查所有依赖
```bash
pip list | grep -E "requests|beautifulsoup4|pandas|selenium|openpyxl|PyQt5"
```

### 运行爬虫测试
```bash
python -c "from scraper import GameMachineScraper; print('✅ 爬虫模块 OK')"
```

### 清理打包文件（重新打包前）
```bash
rm -rf build dist *.spec
```

---

## 💡 常用技巧

### 技巧1：快速重新安装依赖
```bash
pip install -r requirements.txt --force-reinstall --no-cache-dir
```

### 技巧2：查看爬虫实时日志
```bash
python gui_app.py 2>&1 | tee scraper.log
```

### 技巧3：导出数据为 CSV
```bash
python -c "
import pandas as pd
import glob
file = max(glob.glob('data/*.xlsx'), key=lambda x: x)
pd.read_excel(file).to_csv('data/output.csv', index=False)
print('✅ 已导出为 CSV')
"
```

### 技巧4：统计爬虫成功率
```bash
python -c "
import pandas as pd
import glob
file = max(glob.glob('data/*.xlsx'), key=lambda x: x)
df = pd.read_excel(file)
print(f'总数: {len(df)}')
print(f'有效数据: {df.notna().sum().sum()}')
"
```

### 技巧5：自动定时爬虫（Windows）
```batch
:: 创建文件 schedule.bat
@echo off
:loop
python gui_app.py
timeout /t 86400 /nobreak
goto loop
```

---

## 📊 GUI 功能速查

| 功��� | 位置 | 用途 |
|-----|------|------|
| 选择关键词 | 上方下拉菜单 | 选择爬取的商品类型 |
| 设置数量 | 中间滑块或输入框 | 设置要爬取的商品数 |
| 自动打开 | 复选框 | 爬虫完成后自动打开 Excel |
| 开始爬虫 | 🚀 按钮 | 启动爬虫程序 |
| 打开文件夹 | 📁 按钮 | 在文件管理器打开 data 目录 |
| 打开最新文件 | 📊 按钮 | 直接打开最新的 Excel 文件 |
| 实时日志 | 下方文本框 | 查看爬虫运行详情 |
| 进度条 | 中间显示 | 爬虫进度百分比 |

---

## 🎨 自定义指南

### 修改应用标题
文件：`gui_app.py` 第 30 行
```python
self.setWindowTitle("我的游戏机爬虫")
```

### 修改窗口大小
文件：`gui_app.py` 第 31 行
```python
self.setGeometry(100, 100, 1000, 700)  # 宽度, 高度
```

### 修改默认爬取数量
文件：`gui_app.py` 第 50 行
```python
self.quantity_spinbox.setValue(300)  # 默认 300 个
```

### 修改输出目录
文件：`config.py` 第 5 行
```python
OUTPUT_DIR = 'my_data'  # 改为自己的目录
```

---

## 🔐 隐私和安全

✅ **安全特性**
- 本地运行，数据不上传
- 无登录或账户必需
- 开源代码，完全透明

⚠️ **注意事项**
- 爬虫可能被 IP 封禁，如出现 403 错误，需要更换 IP
- 遵守网站 robots.txt
- 个人学习使用，不用于商业目的
- 爬虫延迟是必要的，避免修改

---

## 📞 快速帮助

### "无法导入 PyQt5"
```bash
pip install PyQt5 --upgrade
```

### "应用打不开 Excel"
```bash
# 确保 openpyxl 已安装
pip install openpyxl --upgrade
```

### "爬虫太慢"
正常！包含反爬虫延迟。500 个商品需 5-15 分钟。

### "IP 被封了"
1. 等待 24 小时后重试
2. 更换网络环境
3. 使用代理（需修改代码）

### "数据为空或 N/A"
阿里巴巴可能更新了页面，需要等待爬虫代码更新。

---

## 🌐 网络设置

### 如果需要代理

编辑 `scraper.py`，在请求前添加：
```python
proxies = {
    'http': 'http://proxy_ip:port',
    'https': 'http://proxy_ip:port',
}
response = requests.get(url, proxies=proxies, timeout=10)
```

### 修改请求超时时间

编辑 `config.py`：
```python
TIMEOUT = 15  # 增加为 15 秒
```

---

## 📈 输出数据说明

### Excel 包含的列

```
product_title          商品标题
price                  价格
transactions           成交量 ⭐ 重要！
shop_name              店铺名
rating                 评分
review_count           评价数
product_url            商品链接
keyword                搜索词
scraped_at             爬取时间
```

### 文件位置

```
data/alibaba_game_machines_YYYYMMDD_HHMMSS.xlsx
      ↑               ↑       ↑       ↑    ↑
     目录            产品     日期    时间  格式
```

---

## 🎓 学习资源

### 相关文档
- `README.md` - 项目介绍
- `DESKTOP_APP_GUIDE.md` - 完整使用手册
- `BUILD_GUIDE.md` - 打包指南
- `QUICK_REFERENCE.md` - 本文件

### 外部资源
- [PyQt5 官方文档](https://riverbankcomputing.com/software/pyqt/intro)
- [Pandas 数据分析](https://pandas.pydata.org/docs/)
- [Beautiful Soup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium 文档](https://selenium-python.readthedocs.io/)

---

## 版本信息

**当前版本**: 2.0 Desktop GUI
**发布日期**: 2024年6月
**Python 要求**: 3.7+
**主要依赖**:
- PyQt5 5.15.9
- pandas 2.1.3
- selenium 4.15.2
- beautifulsoup4 4.12.2

---

## 📝 最后的话

这个项目提供了三种使用方式：

1. **CLI** - `python run_scraper.py`（开发者）
2. **GUI** - `python gui_app.py`（一般用户） ⭐ 推荐
3. **EXE** - `python build.py` → `dist/*.exe`（普通用户）

选择最适合你的方式，开始使用吧！🚀

---

**有问题？查看 DESKTOP_APP_GUIDE.md 的常见问题部分！**

**想贡献？欢迎 Fork 和 Pull Request！**

祝你使用愉快！ 🎉
