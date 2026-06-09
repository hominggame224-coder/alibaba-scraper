"""
创建 data/ 目录的初始化脚本
"""

from pathlib import Path

# 创建必要的目录
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# 创建子目录 (可选)
snapshots_dir = data_dir / 'snapshots'
snapshots_dir.mkdir(exist_ok=True)

print("✅ 目录结构初始化完成")
print(f"📁 数据将保存到: {data_dir.absolute()}")
