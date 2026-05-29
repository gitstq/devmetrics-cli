<div align="center">

# 📊 DevMetrics-CLI

**轻量级开发者生产力指标追踪与分析引擎**

*Lightweight Developer Productivity Metrics Tracking & Analysis Engine*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Zero-Dependencies-orange.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()

[简体中文](#简体中文) | [繁體中文](#繁體中文) | [English](#english)

</div>

---

## 简体中文

### 🎉 项目介绍

**DevMetrics-CLI** 是一款专为开发者打造的**零依赖**生产力分析工具。它通过分析 Git 提交历史，帮助您深入了解自己的编码习惯、生产力趋势和技术栈分布。

#### 💡 灵感来源

在日常开发中，我们往往难以量化自己的工作效率和编码模式。DevMetrics-CLI 应运而生，它让开发者能够：
- 📈 追踪个人编码生产力趋势
- ⏰ 发现最高效的编码时段
- 💻 了解技术栈使用分布
- 📊 生成可视化的分析报告

#### ✨ 核心差异化亮点

- **🔒 隐私优先** - 纯本地分析，代码永不离开您的设备
- **🚀 零依赖** - 仅需 Python 3.7+，无需安装任何第三方库
- **🎨 美观 TUI** - 终端可视化仪表盘，条形图、热力图一目了然
- **📄 多格式导出** - 支持 JSON 和 Markdown 报告导出
- **⚡ 极速分析** - 针对大型仓库优化，秒级完成分析

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 📊 **生产力评分** | 智能算法计算 0-100 生产力评分 |
| 📈 **提交分析** | 日/周/月提交频率统计 |
| 🕐 **时间热力图** | 24小时编码活跃度可视化 |
| 💻 **语言检测** | 自动识别 20+ 编程语言 |
| 👥 **贡献者统计** | 团队项目贡献度分析 |
| 📝 **代码变更** | 新增/删除行数统计 |
| 📄 **报告导出** | JSON / Markdown 双格式支持 |

### 🚀 快速开始

#### 环境要求

- **Python**: 3.7 或更高版本
- **Git**: 任意版本
- **操作系统**: Linux / macOS / Windows

#### 安装

**方式一：直接下载使用（推荐）**

```bash
# 克隆仓库
git clone https://github.com/gitstq/devmetrics-cli.git
cd devmetrics-cli

# 直接运行
python devmetrics.py
```

**方式二：通过 pip 安装**

```bash
pip install devmetrics-cli
```

**方式三：全局命令安装**

```bash
# 安装到系统
python setup.py install

# 现在可以使用全局命令
devmetrics --help
dm --help
```

#### 基本使用

```bash
# 分析当前目录的 Git 仓库
python devmetrics.py

# 分析指定仓库
python devmetrics.py /path/to/your/repo

# 分析最近 7 天
python devmetrics.py --days 7

# 分析特定作者的提交
python devmetrics.py --author "张三"

# 导出 JSON 报告
python devmetrics.py --json report.json

# 导出 Markdown 报告
python devmetrics.py --markdown report.md
```

### 📖 详细使用指南

#### 命令行参数

```
usage: devmetrics.py [-h] [--days DAYS] [--author AUTHOR] [--json FILE] [--markdown FILE] [--version] [path]

位置参数:
  path                  仓库路径 (默认: 当前目录)

可选参数:
  -h, --help            显示帮助信息
  --days DAYS, -d DAYS  分析天数 (默认: 30)
  --author AUTHOR, -a AUTHOR
                        指定作者过滤
  --json FILE, -j FILE  导出JSON报告
  --markdown FILE, -m FILE
                        导出Markdown报告
  --version, -v         显示版本信息
```

#### 典型使用场景

**场景一：个人生产力追踪**

```bash
# 每周生成生产力报告
python devmetrics.py --days 7 --markdown weekly-report.md
```

**场景二：团队项目分析**

```bash
# 分析团队贡献分布
python devmetrics.py --days 30 --json team-stats.json
```

**场景三：编码习惯分析**

```bash
# 查看自己的编码时间分布
python devmetrics.py --author "Your Name" --days 90
```

### 💡 设计思路与迭代规划

#### 设计理念

1. **极简主义** - 零依赖设计，降低使用门槛
2. **隐私保护** - 本地分析，数据不上传
3. **开发者优先** - 针对开发者日常工作场景优化

#### 技术选型

- **纯 Python 标准库** - 确保零依赖和跨平台兼容
- **ANSI 转义序列** - 实现彩色终端输出
- **Git 命令解析** - 直接调用 git 命令获取数据

#### 后续迭代计划

- [ ] 添加趋势对比功能（周/月对比）
- [ ] 支持导出 HTML 交互式报告
- [ ] 集成 AI 驱动的生产力建议
- [ ] 添加更多图表类型（饼图、折线图）
- [ ] 支持多仓库批量分析

### 📦 打包与部署

#### 打包为可执行文件

**使用 PyInstaller：**

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包为单文件可执行程序
pyinstaller --onefile --name devmetrics devmetrics.py

# 输出位置: dist/devmetrics
```

**使用 Nuitka（推荐，性能更好）：**

```bash
# 安装 Nuitka
pip install nuitka

# 编译为原生可执行文件
python -m nuitka --standalone --onefile --enable-plugin=anti-bloat devmetrics.py
```

### 🤝 贡献指南

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 繁體中文

### 🎉 專案介紹

**DevMetrics-CLI** 是一款專為開發者打造的**零依賴**生產力分析工具。它透過分析 Git 提交歷史，幫助您深入了解自己的編碼習慣、生產力趨勢和技術棧分布。

#### 💡 靈感來源

在日常開發中，我們往往難以量化自己的工作效率和編碼模式。DevMetrics-CLI 應運而生，它讓開發者能夠：
- 📈 追蹤個人編碼生產力趨勢
- ⏰ 發現最高效的編碼時段
- 💻 了解技術棧使用分布
- 📊 生成可視化的分析報告

#### ✨ 核心差異化亮點

- **🔒 隱私優先** - 純本地分析，程式碼永不離開您的設備
- **🚀 零依賴** - 僅需 Python 3.7+，無需安裝任何第三方庫
- **🎨 美觀 TUI** - 終端可視化儀表板，條形圖、熱力圖一目瞭然
- **📄 多格式匯出** - 支援 JSON 和 Markdown 報告匯出
- **⚡ 極速分析** - 針對大型倉庫優化，秒級完成分析

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 📊 **生產力評分** | 智慧演算法計算 0-100 生產力評分 |
| 📈 **提交分析** | 日/週/月提交頻率統計 |
| 🕐 **時間熱力圖** | 24小時編碼活躍度可視化 |
| 💻 **語言檢測** | 自動識別 20+ 程式語言 |
| 👥 **貢獻者統計** | 團隊專案貢獻度分析 |
| 📝 **程式碼變更** | 新增/刪除行數統計 |
| 📄 **報告匯出** | JSON / Markdown 雙格式支援 |

### 🚀 快速開始

#### 環境要求

- **Python**: 3.7 或更高版本
- **Git**: 任意版本
- **作業系統**: Linux / macOS / Windows

#### 安裝

**方式一：直接下載使用（推薦）**

```bash
# 克隆倉庫
git clone https://github.com/gitstq/devmetrics-cli.git
cd devmetrics-cli

# 直接執行
python devmetrics.py
```

**方式二：透過 pip 安裝**

```bash
pip install devmetrics-cli
```

**方式三：全域命令安裝**

```bash
# 安裝到系統
python setup.py install

# 現在可以使用全域命令
devmetrics --help
dm --help
```

#### 基本使用

```bash
# 分析當前目錄的 Git 倉庫
python devmetrics.py

# 分析指定倉庫
python devmetrics.py /path/to/your/repo

# 分析最近 7 天
python devmetrics.py --days 7

# 分析特定作者的提交
python devmetrics.py --author "張三"

# 匯出 JSON 報告
python devmetrics.py --json report.json

# 匯出 Markdown 報告
python devmetrics.py --markdown report.md
```

### 📖 詳細使用指南

#### 命令列參數

```
usage: devmetrics.py [-h] [--days DAYS] [--author AUTHOR] [--json FILE] [--markdown FILE] [--version] [path]

位置參數:
  path                  倉庫路徑 (預設: 當前目錄)

可選參數:
  -h, --help            顯示說明資訊
  --days DAYS, -d DAYS  分析天數 (預設: 30)
  --author AUTHOR, -a AUTHOR
                        指定作者過濾
  --json FILE, -j FILE  匯出JSON報告
  --markdown FILE, -m FILE
                        匯出Markdown報告
  --version, -v         顯示版本資訊
```

#### 典型使用場景

**場景一：個人生產力追蹤**

```bash
# 每週生成生產力報告
python devmetrics.py --days 7 --markdown weekly-report.md
```

**場景二：團隊專案分析**

```bash
# 分析團隊貢獻分布
python devmetrics.py --days 30 --json team-stats.json
```

**場景三：編碼習慣分析**

```bash
# 查看自己的編碼時間分布
python devmetrics.py --author "Your Name" --days 90
```

### 💡 設計思路與迭代規劃

#### 設計理念

1. **極簡主義** - 零依賴設計，降低使用門檻
2. **隱私保護** - 本地分析，資料不上傳
3. **開發者優先** - 針對開發者日常工作場景優化

#### 技術選型

- **純 Python 標準庫** - 確保零依賴和跨平台相容
- **ANSI 轉義序列** - 實現彩色終端輸出
- **Git 命令解析** - 直接呼叫 git 命令獲取資料

#### 後續迭代計劃

- [ ] 添加趨勢對比功能（週/月對比）
- [ ] 支援匯出 HTML 互動式報告
- [ ] 整合 AI 驅動的生產力建議
- [ ] 添加更多圖表類型（圓餅圖、折線圖）
- [ ] 支援多倉庫批次分析

### 📦 打包與部署

#### 打包為可執行檔案

**使用 PyInstaller：**

```bash
# 安裝 PyInstaller
pip install pyinstaller

# 打包為單檔案可執行程式
pyinstaller --onefile --name devmetrics devmetrics.py

# 輸出位置: dist/devmetrics
```

**使用 Nuitka（推薦，效能更好）：**

```bash
# 安裝 Nuitka
pip install nuitka

# 編譯為原生可執行檔案
python -m nuitka --standalone --onefile --enable-plugin=anti-bloat devmetrics.py
```

### 🤝 貢獻指南

我們歡迎各種形式的貢獻！請查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳情。

### 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## English

### 🎉 Introduction

**DevMetrics-CLI** is a **zero-dependency** productivity analysis tool designed specifically for developers. By analyzing Git commit history, it helps you gain deep insights into your coding habits, productivity trends, and tech stack distribution.

#### 💡 Inspiration

In daily development, we often struggle to quantify our work efficiency and coding patterns. DevMetrics-CLI was born to help developers:
- 📈 Track personal coding productivity trends
- ⏰ Discover the most productive coding hours
- 💻 Understand tech stack usage distribution
- 📊 Generate visual analysis reports

#### ✨ Key Differentiators

- **🔒 Privacy First** - Pure local analysis, code never leaves your device
- **🚀 Zero Dependencies** - Only requires Python 3.7+, no third-party libraries needed
- **🎨 Beautiful TUI** - Terminal visualization dashboard with bar charts and heatmaps
- **📄 Multi-format Export** - Supports JSON and Markdown report export
- **⚡ Lightning Fast** - Optimized for large repositories, completes analysis in seconds

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 📊 **Productivity Score** | Smart algorithm calculates 0-100 productivity score |
| 📈 **Commit Analysis** | Daily/weekly/monthly commit frequency statistics |
| 🕐 **Time Heatmap** | 24-hour coding activity visualization |
| 💻 **Language Detection** | Auto-detect 20+ programming languages |
| 👥 **Contributor Stats** | Team project contribution analysis |
| 📝 **Code Changes** | Lines added/deleted statistics |
| 📄 **Report Export** | JSON / Markdown dual format support |

### 🚀 Quick Start

#### Requirements

- **Python**: 3.7 or higher
- **Git**: Any version
- **OS**: Linux / macOS / Windows

#### Installation

**Option 1: Direct Download (Recommended)**

```bash
# Clone repository
git clone https://github.com/gitstq/devmetrics-cli.git
cd devmetrics-cli

# Run directly
python devmetrics.py
```

**Option 2: Install via pip**

```bash
pip install devmetrics-cli
```

**Option 3: Global Command Installation**

```bash
# Install to system
python setup.py install

# Now you can use global commands
devmetrics --help
dm --help
```

#### Basic Usage

```bash
# Analyze current directory's Git repository
python devmetrics.py

# Analyze specific repository
python devmetrics.py /path/to/your/repo

# Analyze last 7 days
python devmetrics.py --days 7

# Analyze specific author's commits
python devmetrics.py --author "John Doe"

# Export JSON report
python devmetrics.py --json report.json

# Export Markdown report
python devmetrics.py --markdown report.md
```

### 📖 Detailed Usage Guide

#### Command Line Arguments

```
usage: devmetrics.py [-h] [--days DAYS] [--author AUTHOR] [--json FILE] [--markdown FILE] [--version] [path]

Positional Arguments:
  path                  Repository path (default: current directory)

Optional Arguments:
  -h, --help            Show help message
  --days DAYS, -d DAYS  Analysis days (default: 30)
  --author AUTHOR, -a AUTHOR
                        Filter by author
  --json FILE, -j FILE  Export JSON report
  --markdown FILE, -m FILE
                        Export Markdown report
  --version, -v         Show version info
```

#### Typical Use Cases

**Case 1: Personal Productivity Tracking**

```bash
# Generate weekly productivity report
python devmetrics.py --days 7 --markdown weekly-report.md
```

**Case 2: Team Project Analysis**

```bash
# Analyze team contribution distribution
python devmetrics.py --days 30 --json team-stats.json
```

**Case 3: Coding Habit Analysis**

```bash
# View your coding time distribution
python devmetrics.py --author "Your Name" --days 90
```

### 💡 Design Philosophy & Roadmap

#### Design Principles

1. **Minimalism** - Zero-dependency design, low barrier to entry
2. **Privacy Protection** - Local analysis, data never uploaded
3. **Developer First** - Optimized for daily developer workflows

#### Tech Stack

- **Pure Python Standard Library** - Ensures zero dependencies and cross-platform compatibility
- **ANSI Escape Sequences** - Enables colorful terminal output
- **Git Command Parsing** - Direct git command invocation for data retrieval

#### Future Roadmap

- [ ] Add trend comparison features (week/month comparison)
- [ ] Support HTML interactive report export
- [ ] Integrate AI-driven productivity suggestions
- [ ] Add more chart types (pie charts, line graphs)
- [ ] Support multi-repository batch analysis

### 📦 Packaging & Deployment

#### Package as Executable

**Using PyInstaller:**

```bash
# Install PyInstaller
pip install pyinstaller

# Package as single-file executable
pyinstaller --onefile --name devmetrics devmetrics.py

# Output location: dist/devmetrics
```

**Using Nuitka (Recommended, better performance):**

```bash
# Install Nuitka
pip install nuitka

# Compile to native executable
python -m nuitka --standalone --onefile --enable-plugin=anti-bloat devmetrics.py
```

### 🤝 Contributing

We welcome all forms of contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ for Developers**

[⭐ Star us on GitHub](https://github.com/gitstq/devmetrics-cli) | [🐛 Report Issues](https://github.com/gitstq/devmetrics-cli/issues)

</div>
