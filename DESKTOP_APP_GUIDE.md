# 🎮 阿里巴巴游戏机爬虫 - 桌面应用完整使用指南

## 📋 目录
1. [快速开始](#快速开始)
2. [安装指南](#安装指南)
3. [GUI应用使用](#gui应用使用)
4. [打包成可执行文件](#打包成可执行文件)
5. [常见问题](#常见问题)
6. [高级功能](#高级功能)

---

## 🚀 快速开始

### 方式1：直接运行GUI应用（推荐）

**Windows 用户：**
```bash
# 方法A：双击 run.bat
run.bat

# 方法B：命令行
python gui_app.py
```

**macOS/Linux 用户：**
```bash
# 方法A：运行脚本
bash run.sh

# 方法B：命令行
python3 gui_app.py
```

### 方式2：一键打包成可执行应用

```bash
python build.py
```

完成后在 `dist/` 文件夹找到 `.exe`（Windows）或 `.app`（macOS）文件

---

## 💾 安装指南

### 第一步：下载项目

```bash
git clone https://github.com/hominggame224-coder/alibaba-scraper.git
cd alibaba-scraper
```

### 第二步：安装 Python 依赖

```bash
pip install -r requirements.txt
```

**依赖列表：**
- `requests` - HTTP 请求库
- `beautifulsoup4` - HTML 解析
- `pandas` - 数据处理
- `selenium` - 浏览器自动化
- `openpyxl` - Excel 文件生成
- `PyQt5` - GUI 框架
- `PyInstaller` - 应用打包

### 第三步：验证安装

```bash
python -c "import PyQt5; print('✅ PyQt5 安装成功')"
```

---

## 🖥️ GUI应用使用

### 界面介绍

```
┌─────────────────────────────────────────────────────┐
│  🎮 阿里巴巴游戏机爬虫工具                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ⚙️ 爬虫参数设置                                    │
│  ├─ 搜索关键词: [下拉菜单]                          │
│  ├─ 爬取数量: [500] 个商品                          │
│  └─ ☑ 爬取完成后自动打开 Excel                     │
│                                                     │
│  [🚀 开始爬取] [📁 打开数据文件夹] [📊 打开最新文件] │
│                                                     │
│  ▮▮▮▮▮▮▯▯▯▯ 50%                                   │
│                                                     │
│  📝 运行日志                                        │
│  ├─ [16:30:45] 🚀 爬虫启动                         │
│  ├─ [16:30:46] 📌 目标关键词: game machine        │
│  ├─ [16:31:00] 📌 目标数量: 500 个商品             │
│  └─ [16:35:20] ✅ Excel 已生成                    │
│                                                     │
│  ✅ 就绪  |  已爬取: 500 条                        │
└─────────────────────────────────────────────────────┘
```

### 使用步骤

#### 步骤1：选择搜索关键词
- **game machine** - 搜索"游戏机"
- **amusement game machine** - 搜索"娱乐游戏机"
- **两个都爬取** - 同时搜索两个关键词（推荐）

#### 步骤2：设置爬取数量
- 滑块或输入框选择数量
- 范围：10-2000 个商品
- 推荐：500 个（平衡速度和数据量）
- ⚠️ 越多耗时越长（通常 5-15 分钟）

#### 步骤3：可选设置
- ✅ **自动打开 Excel** - 爬虫完成后自动打开数据文件

#### 步骤4：开始爬虫
- 点击 **🚀 开始爬取** 按钮
- 观看实时日志输出
- 等待进度条完成

#### 步骤5：查看结果
- 自动打开 Excel 文件（如果勾选）
- 或手动点击 **📊 打开最新文件**
- 或点击 **📁 打开数据文件夹** 查看所有文件

### 按钮功能说明

| 按钮 | 功能 | 说明 |
|-----|-----|------|
| 🚀 开始爬取 | 启动爬虫 | 开始从阿里巴巴爬取数据 |
| 📁 打开文件夹 | 打开数据目录 | 在文件管理器中打开 data 文件夹 |
| 📊 打开最新文件 | 打开 Excel | 直接打开最新生成的 Excel 文件 |

---

## 📦 打包成可执行文件

### 方式1：使用自动打包脚本（推荐）

```bash
python build.py
```

✅ 自动检查依赖
✅ 自动选择正确的系统参数
✅ 自动检测图标文件
✅ 完成后提示应用位置

### 方式2：手动打包

#### Windows
```cmd
pyinstaller --onefile --windowed ^
  --name "阿里巴巴游戏机爬虫" ^
  --hidden-import=PyQt5.QtCore ^
  --hidden-import=PyQt5.QtGui ^
  --hidden-import=PyQt5.QtWidgets ^
  --hidden-import=pandas ^
  --hidden-import=openpyxl ^
  gui_app.py
```

#### macOS/Linux
```bash
pyinstaller --onefile --windowed \
  --name "阿里巴巴游戏机爬虫" \
  --hidden-import=PyQt5.QtCore \
  --hidden-import=PyQt5.QtGui \
  --hidden-import=PyQt5.QtWidgets \
  --hidden-import=pandas \
  --hidden-import=openpyxl \
  gui_app.py
```

### 输出位置

打包完成后：
- **Windows**: `dist/阿里巴巴游戏机爬虫.exe`
- **macOS**: `dist/阿里巴巴游戏机爬虫.app`
- **Linux**: `dist/阿里巴巴游戏机爬虫`

### 分发应用

✅ 打包完成后可直接分发 `dist` 文件夹中的应用
✅ 接收者无需安装 Python 或依赖
✅ 完全独立可运行

---

## 📊 输出数据说明

### 生成的文件

爬虫生成的 Excel 文件位置：
```
data/alibaba_game_machines_YYYYMMDD_HHMMSS.xlsx
```

### Excel 数据结构

| 列序号 | 列名 | 说明 | 示例 |
|------|------|------|------|
| 1 | product_title | 商品标题 | Gaming Machine X100 |
| 2 | price | 商品价格 | $500-1000 / CNY 3000-5000 |
| 3 | **transactions** | **成交量/已售数** ⭐ | **150+ sold / 已售150笔** |
| 4 | shop_name | 店铺名称 | ABC Gaming Factory |
| 5 | rating | 评分 | 4.8/5.0 |
| 6 | review_count | 评价数量 | 200+ reviews |
| 7 | product_url | 商品链接 | https://www.alibaba.com/... |
| 8 | keyword | 搜索关键词 | game machine |
| 9 | scraped_at | 爬取时间戳 | 2024-06-09 15:30:00 |

### 数据分析建议

```python
import pandas as pd

# 读取 Excel
df = pd.read_excel('data/alibaba_game_machines_*.xlsx')

# 找热销TOP20
top20 = df.nlargest(20, 'transactions')
print(top20[['product_title', 'price', 'transactions']])

# 高评分产品
high_rated = df[df['rating'].astype(float) >= 4.5]
print(f"高评分产品数: {len(high_rated)}")

# 按店铺统计
shop_stats = df.groupby('shop_name').agg({
    'transactions': 'sum',
    'product_title': 'count',
    'rating': 'mean'
}).rename(columns={'product_title': 'product_count'})
print(shop_stats)

# 价格分布
print(df['price'].value_counts())
```

---

## ❓ 常见问题

### Q1: 运行时提示 "ModuleNotFoundError"

**问题**：无法导入某个模块

**解决**：
```bash
pip install -r requirements.txt
```

### Q2: GUI 界面无法打开

**问题**：PyQt5 无法初始化

**解决**：
```bash
# 重新安装 PyQt5
pip install --upgrade PyQt5
```

### Q3: 爬虫运行很慢

**正常现象**：
- 反爬虫延迟是设计的，避免 IP 被封
- 500 个商品通常需要 5-15 分钟
- ⚠️ 不要修改代码中的延迟时间

### Q4: Excel 无法生成

**检查**：
1. data 文件夹是否存在
2. 磁盘空间是否充足
3. 数据是否成功爬取（查看日志）

**解决**：
```bash
python init_dirs.py
```

### Q5: 爬虫数据为 "N/A" 或空值

**原因**：阿里巴巴可能更新了页面结构

**解决**：
- 等待爬虫代码更新
- 在 GitHub 提交 Issue 报告问题
- 检查网络连接

### Q6: 打包后的应用无法运行

**检查**：
1. 确保所有依赖已安装
2. 使用最新的 PyInstaller：`pip install --upgrade PyInstaller`
3. 确保 Python 版本 >= 3.7

**重新打包**：
```bash
rm -rf build dist *.spec
python build.py
```

### Q7: 如何修改爬取关键词？

**方式1**：使用 GUI 的下拉菜单选择

**方式2**：修改代码
```python
# 编辑 scraper.py
self.keywords = ['your_keyword_1', 'your_keyword_2']
```

### Q8: 如何定时自动爬虫？

**Windows**：使用任务计划程序
```
设置 → 任务计划程序 → 创建基本任务 → 指向 gui_app.py
```

**macOS/Linux**：使用 cron
```bash
# 每天早上 8 点运行
0 8 * * * /usr/bin/python3 /path/to/run_scraper.py
```

---

## 🎯 高级功能

### 自定义爬虫参数

编辑 `config.py`：
```python
# 最大爬取商品数
MAX_PRODUCTS = 1000

# 搜索关键词
KEYWORDS = ['game machine', 'amusement game machine']

# 请求延迟（秒）
REQUEST_DELAY = 2

# 超时时间（秒）
TIMEOUT = 10

# 输出目录
OUTPUT_DIR = 'data'
```

### 修改 GUI 样式

编辑 `gui_app.py` 中的 `setStyleSheet()`：
```python
self.setStyleSheet("""
    QMainWindow {
        background-color: #your_color;
    }
    /* 修改其他样式 */
""")
```

### 添加代理 IP

编辑 `scraper.py`：
```python
proxies = {
    'http': 'http://proxy_ip:port',
    'https': 'http://proxy_ip:port',
}
response = requests.get(url, proxies=proxies)
```

### 导出其他格式

```python
import pandas as pd

df = pd.read_excel('alibaba_game_machines_*.xlsx')

# 导出 CSV
df.to_csv('output.csv', index=False)

# 导出 JSON
df.to_json('output.json')

# 导出 HTML
df.to_html('output.html')
```

---

## 📞 获取帮助

### 遇到问题？

1. **查看日志** - GUI 中的"运行日志"显示详细信息
2. **检查文档** - README.md、USAGE.md、BUILD_GUIDE.md
3. **GitHub Issues** - 提交问题报告
4. **重新安装依赖** - `pip install -r requirements.txt --upgrade`

### 项目链接

- **GitHub 仓库**: https://github.com/hominggame224-coder/alibaba-scraper
- **提交 Issue**: https://github.com/hominggame224-coder/alibaba-scraper/issues
- **开发者**: hominggame224-coder

---

## 📈 使用提示

### 最佳实践

✅ 定期运行爬虫（每周或每月）收集数据
✅ 保存历史数据进行对比分析
✅ 按不同关键词分别爬取以获得全面数据
✅ 定期检查爬虫是否正常工作

### 性能优化

- 降低爬取数量以加快速度
- 使用 SSD 存储以加快 Excel 生成
- 在网络条件好时运行爬虫
- 避免在高峰时间（中午、晚上）运行

### 安全提醒

⚠️ 遵守阿里巴巴的爬虫协议
⚠️ 不要过度频繁爬取（容易被 IP 封禁）
⚠️ 个人学习和研究使用
⚠️ 不用于商业目的

---

## 🎉 总结

现在你有一个完整的、可安装的桌面应用爬虫！

### 三种使用方式：

| 方式 | 命令 | 难度 | 推荐 |
|-----|------|------|-----|
| CLI 脚本 | `python run_scraper.py` | ⭐ | 开发者 |
| GUI 应用 | `python gui_app.py` 或 `run.bat` | ⭐⭐ | 一般用户 |
| 可执行文件 | `python build.py` → `dist/*.exe` | ⭐⭐ | 普通用户 |

### 下一步：

1. ✅ 运行 GUI 应用测试
2. ✅ 爬取一些数据
3. ✅ 打包成可执行文件
4. ✅ 分享给其他人使用

祝你使用愉快！🚀

---

**最后更新**: 2024年6月
**版本**: 2.0 (GUI Desktop App)
**作者**: hominggame224-coder
