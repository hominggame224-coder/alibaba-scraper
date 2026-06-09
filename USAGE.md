"""
快速使用指南 - 三种方式运行爬虫
"""

# ============================================================
# 方式1: 最简单 - 直接运行Python脚本 (本地电脑)
# ============================================================

"""
步骤1: 打开命令行/终端，进入项目目录
cd alibaba-scraper

步骤2: 安装依赖 (首次运行)
pip install -r requirements.txt

步骤3: 运行爬虫脚本
python run_scraper.py

步骤4: 等待完成
- 大约需要5-10分钟（取决于网络速度）
- Excel文件会自动生成在 data/ 文件夹

步骤5: 打开Excel文件查看数据
data/alibaba_game_machines_20240609_153000.xlsx
"""

# ============================================================
# 方式2: 自动化 - GitHub Actions 每天自动运行
# ============================================================

"""
GitHub Actions 配置已完成，每天凌晨00:00北京时间自动运行

操作步骤:
1. 进入 GitHub 仓库页面
   https://github.com/hominggame224-coder/alibaba-scraper

2. 点击 "Actions" 选项卡

3. 左侧找到 "Daily Alibaba Game Machine Scrape" 工作流

4. 点击 "Run workflow" 按钮手动触发 (可选)
   - 或等待每天自动运行

5. 查看运行日志
   - 点击工作流名称查看详细日志
   - 成功时会显示绿色✅

6. 下载数据文件
   - 进入仓库主页
   - 打开 data/ 文件夹
   - 下载最新的 .xlsx 文件
"""

# ============================================================
# 方式3: 完全自定义 - 修改参数后运行
# ============================================================

"""
A. 修改爬取数量
   编辑 run_scraper.py 第27行:
   scraper.run(max_products=1000)  # 改为1000个商品

B. 修改爬取关键词
   编辑 scraper.py 第33行:
   self.keywords = ['game machine', 'amusement game machine', 'arcade game']

C. 修改自动运行时间
   编辑 .github/workflows/daily-scrape.yml 第7行:
   - cron: '0 8 * * *'  # 改为每天08:00 UTC (北京时间16:00)
   
   常用时间表:
   - '0 0 * * *' = 每天00:00 UTC (北京时间08:00)
   - '0 8 * * *' = 每天08:00 UTC (北京时间16:00)
   - '0 16 * * *' = 每天16:00 UTC (北京时间次日00:00 凌晨)

D. 修改自动提交
   目前自动提交数据到 GitHub，可以在 .github/workflows/daily-scrape.yml 
   中修改或删除提交步骤
"""

# ============================================================
# 常见问题与解决
# ============================================================

"""
Q1: 运行 python run_scraper.py 时出现 "ModuleNotFoundError"
A:  还没有安装依赖包
    运行: pip install -r requirements.txt

Q2: Excel 文件为什么没有生成？
A:  - 检查 data/ 文件夹是否存在（会自动创建）
    - 查看终端输出，可能有错误信息
    - 尝试删除 __pycache__ 文件夹后重新运行

Q3: GitHub Actions 运行失败怎么办？
A:  1. 点击 Actions → 找到失败的工作流
    2. 点击进入查看详细日志
    3. 查看 "Run scraper" 步骤的错误信息
    4. 常见原因:
       - 网络问题（等待重试）
       - 依赖安装失败（修改 requirements.txt）

Q4: 爬虫运行很慢
A:  这是正常的。阿里巴巴有反爬虫机制，爬虫脚本添加了延迟以避免被封IP
    - 500个商品通常需要 5-15 分钟
    - 不要修改延迟时间，否则容易被封IP

Q5: 如何只爬取特定的商品类别？
A:  修改 scraper.py 中的 keywords 列表:
    self.keywords = ['gaming machine arcade']  # 只爬取这个关键词

Q6: Excel 如何分析数据？
A:  推荐步骤:
    1. 按 "Transactions" (成交量) 排序，找出最热销产品
    2. 按 "Shop Name" 分组，找出优质店铺
    3. 按 "Rating" (评分) 筛选 4.5 分以上
    4. 创建透视表统计不同价格区间的商品数量
"""

# ============================================================
# Excel 数据导出后如何使用
# ============================================================

"""
打开 Excel 文件后，你会看到以下列:

1. product_title       - 商品标题
2. price              - 商品价格
3. transactions       - 成交量/已售数量
4. shop_name          - 店铺名称
5. rating             - 评分 (如 4.8/5.0)
6. review_count       - 评价数量
7. product_url        - 商品详情页链接
8. keyword            - 搜索关键词
9. scraped_at         - 爬取时间

数据分析建议:
✅ 排序: 按 transactions 从高到低，找热销品
✅ 筛选: 只看 rating 4.5 以上的好店
✅ 透视表: 统计平均价格、评分等
✅ 制图: 用评分和成交量制作散点图
✅ 导出: 保存为 CSV 给其他人分享
"""

# ============================================================
# 项目文件说明
# ============================================================

"""
alibaba-scraper/
├── scraper.py                 # ⭐ 主爬虫脚本 (核心代码)
├── run_scraper.py             # ⭐ 简化运行脚本 (直接运行这个)
├── requirements.txt           # Python依赖列表
├── README.md                  # 详细说明文档
├── USAGE.md                   # 本文件 - 快速使用指南
├── data/                      # 📁 数据输出文件夹
│   ├── alibaba_game_machines_20240609_150000.xlsx  # Excel表格
│   ├── alibaba_game_machines_20240609_150000.csv   # CSV表格
│   └── alibaba_game_machines_20240609_150000.json  # JSON文件
├── .gitignore                 # Git忽略文件配置
└── .github/workflows/
    └── daily-scrape.yml       # ⭐ GitHub Actions 自动化配置

重要文件:
- 要运行爬虫: python run_scraper.py
- 要修改参数: 编辑 scraper.py 或 run_scraper.py
- 要设置自动运行: 编辑 .github/workflows/daily-scrape.yml
"""

# ============================================================
# 下一步建议
# ============================================================

"""
1. 立即测试
   运行: python run_scraper.py
   生成第一份数据

2. 查看数据
   打开生成的 Excel 文件
   熟悉数据结构

3. 设置自动化 (可选)
   推送到 GitHub
   启用 GitHub Actions
   每天自动更新数据

4. 数据分析
   使用 Excel 或 Python Pandas 分析数据
   找出热销产品、价格趋势等

5. 持续改进
   如果爬虫失效，更新 HTML 选择器
   如果需要更多字段，修改 extract_product_info 方法
"""
