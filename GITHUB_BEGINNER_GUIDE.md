# 🎯 GitHub 操作傻瓜式指南

## 👋 前言

如果你不懂 GitHub，这个指南就是为你写的！
用**最简单**的方式，**一步步**教你如何使用。

---

## 第一步：了解你现在有什么

### 你的项目现在在哪里？

你的项目已经在这里：
```
https://github.com/hominggame224-coder/alibaba-scraper
```

点击这个链接就能看到你的项目！✅

### 你现在有什么文件？

我已经帮你创建了这些文件：
```
✅ DESKTOP_APP_GUIDE.md       - 完整使用手册（最重要！）
✅ BUILD_GUIDE.md              - 打包指南
✅ QUICK_REFERENCE.md          - 快速参考
✅ build.py                    - 一键打包脚本
✅ run.bat                     - Windows 启动脚本
✅ run.sh                      - macOS/Linux 启动脚本
✅ requirements.txt            - 更新的依赖列表
```

这些文件**已经自动上传到 GitHub 了**！🎉

---

## 第二步：本地获取这些文件

### 方式 A：使用 Git 命令（推荐开发者）

#### 1️⃣ 安装 Git
- **Windows**: https://git-scm.com/download/win
- **macOS**: `brew install git`
- **Linux**: `sudo apt-get install git`

#### 2️⃣ 打开命令行/终端

**Windows**: 右键 → "在此处打开 PowerShell"
**macOS/Linux**: 按 Command+Space，搜索"终端"

#### 3️⃣ 克隆项目
```bash
git clone https://github.com/hominggame224-coder/alibaba-scraper.git
cd alibaba-scraper
```

✅ 完成！��有文件都下载到你的电脑了

---

### 方式 B：直接下载（最简单！👍）

#### 1️⃣ 打开你的项目
访问: https://github.com/hominggame224-coder/alibaba-scraper

#### 2️⃣ 找到绿色按钮 "Code"

```
┌─────────────────────────────────┐
│  GitHub 网页                     │
│                                 │
│   【Code ▼】 【Issues】 【...】  │
│    ↑ 点这里                      │
└─────────────────────────────────┘
```

#### 3️⃣ 点击 "Download ZIP"

```
┌──────────────────────────────┐
│ Local                        │
│ ├─ HTTPS                     │
│ └─ GitHub CLI                │
│                              │
│ 📥 Download ZIP  ← 点这个    │
└──────────────────────────────┘
```

#### 4️⃣ 保存到你的电脑
- 选择一个位置（比如 `C:\Users\你的用户名\Desktop`）
- 点击保存

#### 5️⃣ 解压文件
- 右键 ZIP 文件 → 解压

✅ 完成！

---

## 第三步：安装依赖（所有人都需要做）

现在打开命令行/终端，输入：

```bash
cd 你的项目路径
pip install -r requirements.txt
```

例如：
```bash
cd C:\Users\你的用户名\Desktop\alibaba-scraper
pip install -r requirements.txt
```

等待安装完成...（可能需要 2-5 分钟）

✅ 完成！

---

## 第四步：运行应用！

### Windows 用户

方式1（最简单）：
```
直接双击 run.bat 文件
```

方式2（命令行）：
```bash
python gui_app.py
```

### macOS/Linux 用户

方式1（最简单）：
```bash
bash run.sh
```

方式2（命令行）：
```bash
python3 gui_app.py
```

### 🎉 应用启动了！

现在你应该看到一个漂亮的 GUI 界面：

```
╔═══════════════════════════════════════╗
║  🎮 阿里巴巴游戏机爬虫                 ║
├───────────────────────────────────────┤
║                                       ║
║  爬虫参数设置                          ║
║  • 关键词: [game machine ▼]           ║
║  • 数量: [500]                        ║
║  ☑ 爬取完成后自动打开 Excel           ║
║                                       ║
║  [🚀 开始爬取]                        ║
║                                       ║
╚═══════════════════════════════════════╝
```

试试点击 "🚀 开始爬取"！

---

## 第五步：打包成可执行文件（可选）

如果你想要一个 `.exe` 文件（不需要 Python 就能运行），运行：

```bash
python build.py
```

等待打包完成...

完成后，你会在 `dist/` 文件夹找到 `阿里巴巴游戏机爬虫.exe`！

就像这样：
```
📁 dist/
  └─ 阿里巴巴游戏机爬虫.exe  ← 可以直接运行！
```

✅ 现在你可以把这个文件分享给任何人，他们都能直接运行！

---

## 📚 文档在哪里？

所有文档都在项目文件夹里：

| 文件名 | 用途 | 打开方式 |
|------|------|--------|
| **DESKTOP_APP_GUIDE.md** | 完整使用手册 | 用记事本或文本编辑器打开 |
| **QUICK_REFERENCE.md** | 快速参考 | 同上 |
| **BUILD_GUIDE.md** | 打包指南 | 同上 |
| **README.md** | 项目介绍 | 同上 |

或者直接在 GitHub 网页上查看（自动美化显示）

---

## 🐛 常见问题

### Q1: "python 不是内部命令"

**问题**: 没有安装 Python 或 Python 不在 PATH

**解决**:
1. 下载 Python: https://www.python.org/downloads/
2. 安装时 ⚠️ **勾选 "Add Python to PATH"**
3. 重启命令行
4. 试试 `python --version`

### Q2: "No module named 'PyQt5'"

**问题**: 依赖没有安装

**解决**:
```bash
pip install -r requirements.txt
```

### Q3: 下载的 ZIP 文件无法解压

**问题**: 压缩文件损坏或路径有中文

**解决**:
1. 用 7-Zip 或 WinRAR 试试
2. 或重新下载
3. 保存到英文路径（比如 `C:\Users\username\Desktop`）

### Q4: 打开 GUI 后什么都没有

**问题**: 窗口可能在屏幕外或最小化了

**解决**:
1. 查看任务栏是否有窗口
2. 或尝试调整窗口大小
3. 或重新运行

### Q5: 爬虫很慢

**正常的！** 包含反爬虫延迟，500 个商品需要 5-15 分钟

---

## 💡 最常用的三个命令

记住这三个命令，99% 的问题都能解决：

```bash
# 1️⃣ 安装依赖（第一次做）
pip install -r requirements.txt --upgrade

# 2️⃣ 运行应用
python gui_app.py

# 3️⃣ 打包成可执行文件
python build.py
```

---

## 🎯 快速开始流程图

```
┌─────────────────────────┐
│   开始                  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 1. 下载项目             │
│ (GitHub 上点 Code →    │
│  Download ZIP)          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. 解压文件            │
│ (右键 → 解压)          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. 打开命令行          │
│ (Win: PowerShell)      │
│ (Mac: 终端)            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. 进入项目文件夹      │
│ cd alibaba-scraper     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 5. 安装依赖            │
│ pip install            │
│ -r requirements.txt    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 6. 运行应用            │
│ python gui_app.py      │
│ 或双击 run.bat         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ ✅ 享受应用！          │
└─────────────────────────┘
```

---

## 📞 我还是不会怎么办？

别急！按这个顺序试试：

1. **✅ 查看文档** - `DESKTOP_APP_GUIDE.md` 的常见问题部分
2. **✅ 查看日志** - GUI 中的"运行日志"显示详细信息
3. **✅ 重新安装** - `pip install -r requirements.txt --upgrade`
4. **✅ 提交 Issue** - 在 GitHub 上提交问题，我会帮你
   - 网址: https://github.com/hominggame224-coder/alibaba-scraper/issues
   - 点 "New Issue" 描述你的问题

---

## 🚀 最简单的 3 步启动

如果你只想快速试用，只需这 3 步：

### Step 1: 下载
访问 https://github.com/hominggame224-coder/alibaba-scraper
点 "Code" → "Download ZIP"

### Step 2: 安装
```bash
cd 你的项目文件夹
pip install -r requirements.txt
```

### Step 3: 运行
```bash
python gui_app.py
```

**就这样！** 🎉

---

## 💪 现在你会了！

恭喜！你现在已经学会了：
- ✅ 下载 GitHub 项目
- ✅ 安装 Python 依赖
- ✅ 运行桌面应用
- ✅ 打包成可执行文件

你已经从"不懂 GitHub"进化到"会使用 GitHub 项目"了！👍

---

## 📝 记住这些链接

**你的项目**: https://github.com/hominggame224-coder/alibaba-scraper

**Python 下载**: https://www.python.org/downloads/

**Git 下载**: https://git-scm.com/

**GitHub 帮助**: https://docs.github.com/en

---

## 🎓 下一步学习（可选）

如果你想更深入地学习 GitHub，可以看：
- YouTube: "GitHub 入门教程"
- Bilibili: "Git 和 GitHub 教程"
- 免费教程: https://git-scm.com/book/zh/v2

但现在你已经能够使用这个项目了！🚀

---

**有问题？别怕！再看一遍这个指南，或在 GitHub 提交 Issue！**

**祝你使用愉快！** 🎉

---

**最后提醒：**
- 📌 收藏这个指南的链接
- 📌 分享给其他不懂 GitHub 的用户
- 📌 有问题就提 Issue，我会帮你

