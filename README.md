# 🎮 阿里巴巴游戏机爬虫 (Alibaba Game Machine Scraper)

自动爬取阿里巴巴平台上 **game machine** 和 **amusement game machine** 的实时销售数据，每日更新，支持导出Excel表格。

## 📊 功能特性

- ✅ **自动爬取** 500个游戏机商品数据
- ✅ **每日定时更新** (凌晨00:00 北京时间)
- ✅ **导出Excel表格** 方便数据分析
- ✅ **提取关键数据**:
  - 商品标题 (Product Title)
  - 价格 (Price)
  - 成交量 (Transactions/Sales)
  - 店铺名 (Shop Name)
  - 评分 (Rating)
  - 评价数 (Review Count)
  - 商品链接 (Product URL)
  - 搜索关键词 (Keyword)
  - 爬取时间戳 (Timestamp)

---

## 🚀 快速开始

### 方式一: 本地运行 (最简单)

#### 1️⃣ 克隆仓库
```bash
git clone https://github.com/hominggame224-coder/alibaba-scraper.git
cd alibaba-scraper
```

#### 2️⃣ 安装依赖
```bash
pip install -r requirements.txt
```

#### 3️⃣ 运行爬虫
```bash
python run_scraper.py
```

#### 4️⃣ 查看结果
- Excel文件自动生成在 `data/` 目录下
- 文件格式: `alibaba_game_machines_YYYYMMDD_HHMMSS.xlsx`

---

### 方式二: 自动化运行 (GitHub Actions)

#### 1️⃣ GitHub Actions 已配置
- 配置文件: `.github/workflows/daily-scrape.yml`
- 自动运行时间: **每天凌晨00:00 (北京时间)**
- 自动提交数据到仓库

#### 2️⃣ 启用自动运行
```
在GitHub仓库页面 → Actions 选项卡 → 确保工作流已启用
```

#### 3️⃣ 手动触发
```
Actions → Daily Alibaba Game Machine Scrape → Run workflow
```

#### 4️⃣ 查看运行结果
```
GitHub仓库 → data/ 文件夹 → 最新的 .xlsx 文件
```

---

## 📁 项目结构

```
alibaba-scraper/
├── scraper.py                 # 主爬虫脚本
├── run_scraper.py             # 简化运行脚本 (直接运行此文件)
├── requirements.txt           # Python依赖
├── README.md                  # 本文件
├── data/                      # 数据输出目录
│   ├── alibaba_game_machines_YYYYMMDD_HHMMSS.xlsx
│   ├── alibaba_game_machines_YYYYMMDD_HHMMSS.csv
│   └── alibaba_game_machines_YYYYMMDD_HHMMSS.json
└── .github/workflows/
    └── daily-scrape.yml       # GitHub Actions 工作流
```

---

## 📝 使用说明

### 本地运行示例

```python
from scraper import AlibabaGameMachineScraper

# 创建爬虫实例
scraper = AlibabaGameMachineScraper()

# 运行爬虫 (爬取500个商品)
csv_file, json_file = scraper.run(max_products=500)

print(f"数据已保存到: {csv_file}")
```

### 自定义爬取数量

编辑 `run_scraper.py` 第25行:
```python
excel_path = scraper.run(max_products=1000)  # 改为1000个商品
```

### 自定义爬取关键词

编辑 `scraper.py` 第33行:
```python
self.keywords = ['game machine', 'amusement game machine', '其他关键词']
```

---

## 📊 输出数据格式

### Excel 表格示例

| Product Title | Price | Transactions | Shop Name | Rating | Review Count | Product URL | Keyword | Scraped At |
|---|---|---|---|---|---|---|---|---|
| Gaming Machine X100 | $500-1000 | 150+ sold | ABC Store | 4.8 | 200+ | https://... | game machine | 2024-06-09 15:30:00 |
| Amusement Equipment | $800-2000 | 80+ sold | XYZ Factory | 4.6 | 150+ | https://... | amusement game machine | 2024-06-09 15:35:00 |

### CSV 格式
可直接用Excel、Google Sheets、Python Pandas等工具打开

### JSON 格式
用于API集成或进一步数据处理

---

## ⚙️ 配置说明

### 修改自动运行时间

编辑 `.github/workflows/daily-scrape.yml` 第7行的 `cron` 表达式:

```yaml
- cron: '0 16 * * *'  # UTC时间 16:00 = 北京时间 00:00 (凌晨)
```

**Cron 表达式说明:**
- `分钟 小时 日 月 周`
- `0 16 * * *` = 每天16:00 UTC (北京时间次日00:00)
- `0 8 * * *` = 每天08:00 UTC (北京时间次日16:00)
- `0 0 * * *` = 每天00:00 UTC (北京时间次日08:00)

**北京时间转换 (UTC + 8小时):**
- 凌晨00:00 → UTC 16:00 (前一天) → `0 16 * * *`
- 早上08:00 → UTC 00:00 → `0 0 * * *`
- 中午12:00 → UTC 04:00 → `0 4 * * *`

---

## 🔧 故障排除

### 问题1: 爬虫运行缓慢
**原因**: 网络延迟或阿里巴巴反爬虫机制
**解决**: 
- 增加延迟时间 (在 `scraper.py` 中修改)
- 使用代理IP (企业级方案)

### 问题2: 数据为 N/A
**原因**: HTML选择器不匹配 (阿里巴巴可能更新了页面结构)
**解决**:
- 检查网页源代码，更新选择器
- 联系我进行维护

### 问题3: GitHub Actions 失败
**查看日志**:
1. 进入仓库 → Actions 选项卡
2. 点击最新的运行记录
3. 查看 "Run scraper" 步骤的详细日志

### 问题4: 权限不足提交数据
**解决**: 确保仓库设置中允许 Actions 写入权限
1. Settings → Actions → General
2. 勾选 "Read and write permissions"

---

## 📈 数据分析建议

下载Excel文件后，可以使用以下工具分析:

1. **Excel 内置功能**
   - 排序: 按成交量排序找热销产品
   - 筛选: 按评分/价格范围筛选
   - 透视表: 按店铺名/关键词统计

2. **Python 分析**
   ```python
   import pandas as pd
   
   df = pd.read_excel('alibaba_game_machines_20240609.xlsx')
   
   # 按成交量排序
   top_products = df.sort_values('Transactions', ascending=False).head(20)
   
   # 按店铺统计
   shop_stats = df.groupby('Shop Name').agg({
       'Transactions': 'sum',
       'Rating': 'mean'
   })
   ```

3. **Google Sheets**
   - 上传Excel文件到Google Drive
   - 使用内置图表功能可视化数据

---

## 🤝 贡献与反馈

- 发现问题? 在Issues中提交
- 有建议? 欢迎提交Pull Request
- 需要帮助? 联系 hominggame224@gmail.com

---

## ⚖️ 免责声明

- 本工具仅用于学习和研究目的
- 使用时请遵守阿里巴巴服务条款
- 不建议大规模高频爬虫，可能被封IP
- 爬取的数据仅供个人分析使用

---

## 📝 更新日志

### v1.0.0 (2024-06-09)
- ✅ 初始版本发布
- ✅ 支持自动爬取500个商品
- ✅ 导出Excel/CSV/JSON格式
- ✅ GitHub Actions 自动化部署

---

## 📧 联系方式

- GitHub: [@hominggame224-coder](https://github.com/hominggame224-coder)
- Email: hominggame224@gmail.com

---

**祝你数据分析愉快！** 🎉
