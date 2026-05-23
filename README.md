<div align="center">

# 🔥 DevMetrics-CLI

**轻量级开发者代码度量与生产力分析引擎**

*Lightweight Developer Code Metrics & Productivity Analysis Engine*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
[![Zero Dependencies](https://img.shields.io/badge/Zero-Dependencies-brightgreen.svg)]()

[简体中文](#简体中文) | [繁體中文](#繁體中文) | [English](#english)

</div>

---

<a name="简体中文"></a>
## 🇨🇳 简体中文

### 🎉 项目介绍

**DevMetrics-CLI** 是一款专为开发者打造的轻量级代码度量与生产力分析工具。它通过分析 Git 提交历史，帮助开发者深入了解自己的编码习惯、时间分布、语言偏好和贡献模式。

**灵感来源**：在 AI 辅助编程时代，开发者需要更好地了解自己的编码行为模式，以便优化工作效率和提升代码质量。

**自研差异化亮点**：
- 🚀 **零依赖设计** - 仅使用 Python 标准库，无需安装任何第三方包
- 📊 **终端可视化** - 精美的命令行图表和热力图展示
- ⚡ **极速分析** - 本地执行，数据不上传，保护隐私
- 🎯 **多维度洞察** - 从时间、语言、贡献者等多角度分析

### ✨ 核心特性

| 特性 | 描述 | 状态 |
|------|------|------|
| 📈 **提交统计** | 总提交数、代码行数变化、文件变更数 | ✅ |
| ⏰ **时间分析** | 活跃时段热力图、最佳编码时间识别 | ✅ |
| 💻 **语言统计** | 编程语言使用分布、文件类型分析 | ✅ |
| 👥 **贡献者分析** | 团队成员贡献度排行、协作模式 | ✅ |
| 📊 **可视化报告** | 终端条形图、热力图、摘要面板 | ✅ |
| 🔄 **JSON 导出** | 支持结构化数据导出供进一步分析 | ✅ |

### 🚀 快速开始

#### 环境要求

- **Python**: 3.8 或更高版本
- **Git**: 已安装并配置
- **操作系统**: Linux / macOS / Windows

#### 安装步骤

**方式一：直接运行（推荐）**

```bash
# 克隆仓库
git clone https://github.com/yourusername/devmetrics-cli.git
cd devmetrics-cli

# 直接运行
python devmetrics.py
```

**方式二：安装为系统命令**

```bash
# 安装
pip install -e .

# 使用全局命令
devmetrics
# 或简写
dm
```

#### 本地启动

```bash
# 分析当前目录的 Git 仓库
python devmetrics.py

# 分析指定仓库
python devmetrics.py /path/to/your/repo

# 分析最近 30 天
python devmetrics.py --since "30 days ago"

# 分析特定作者的贡献
python devmetrics.py --author "Your Name"

# 导出 JSON 格式
python devmetrics.py --json
```

### 📖 详细使用指南

#### 命令行参数

```
usage: devmetrics.py [-h] [--since SINCE] [--until UNTIL] [--author AUTHOR]
                     [--json] [--limit LIMIT] [--version]
                     [path]

DevMetrics-CLI: 开发者代码度量与生产力分析引擎

positional arguments:
  path              仓库路径 (默认: 当前目录)

optional arguments:
  -h, --help        显示帮助信息
  --since SINCE     开始日期 (如: "30 days ago", "2024-01-01")
  --until UNTIL     结束日期
  --author AUTHOR   指定作者
  --json            输出 JSON 格式
  --limit LIMIT     最大提交数 (默认: 1000)
  --version         显示版本信息
```

#### 典型使用场景

**场景 1：个人编码习惯分析**
```bash
# 查看自己的编码时间分布
python devmetrics.py --author "Your Name" --since "90 days ago"
```

**场景 2：团队贡献统计**
```bash
# 导出 JSON 供团队报告使用
python devmetrics.py --json > team_metrics.json
```

**场景 3：项目健康度检查**
```bash
# 分析整个项目的活跃度
python devmetrics.py --since "1 year ago" --limit 5000
```

### 💡 设计思路与迭代规划

#### 技术选型原因

- **纯标准库实现**：确保零依赖，任何 Python 环境均可直接运行
- **Git 命令解析**：直接调用 Git CLI，兼容所有 Git 版本
- **终端可视化**：使用 ANSI 转义码实现跨平台彩色输出

#### 后续功能迭代计划

- [ ] 趋势分析（周/月对比）
- [ ] 代码复杂度估算
- [ ] 提交信息质量分析
- [ ] HTML 报告导出
- [ ] 配置文件支持
- [ ] 多仓库聚合分析

#### 社区贡献方向

欢迎提交 Issue 和 PR！特别需要：
- 更多编程语言识别支持
- 可视化图表优化
- 性能优化建议

### 📦 打包与部署指南

#### 构建分发包

```bash
# 清理并构建
make clean
make build

# 分发包将生成在 dist/ 目录
dist/
  ├── devmetrics-cli-1.0.0.tar.gz
  └── devmetrics_cli-1.0.0-py3-none-any.whl
```

#### 安装使用

```bash
# 从 wheel 安装
pip install dist/devmetrics_cli-1.0.0-py3-none-any.whl

# 验证安装
devmetrics --version
```

### 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 📄 开源协议

本项目采用 [MIT](LICENSE) 协议开源。

---

<a name="繁體中文"></a>
## 🇹🇼 繁體中文

### 🎉 專案介紹

**DevMetrics-CLI** 是一款專為開發者打造的輕量級程式碼度量與生產力分析工具。它透過分析 Git 提交歷史，幫助開發者深入了解自己的編碼習慣、時間分布、語言偏好和貢獻模式。

**靈感來源**：在 AI 輔助程式設計時代，開發者需要更好地了解自己的編碼行為模式，以便最佳化工作效率和提升程式碼品質。

**自研差異化亮點**：
- 🚀 **零依賴設計** - 僅使用 Python 標準庫，無需安裝任何第三方套件
- 📊 **終端視覺化** - 精美的命令列圖表和熱力圖展示
- ⚡ **極速分析** - 本地執行，資料不上傳，保護隱私
- 🎯 **多維度洞察** - 從時間、語言、貢獻者等多角度分析

### ✨ 核心特性

| 特性 | 描述 | 狀態 |
|------|------|------|
| 📈 **提交統計** | 總提交數、程式碼行數變化、檔案變更數 | ✅ |
| ⏰ **時間分析** | 活躍時段熱力圖、最佳編碼時間識別 | ✅ |
| 💻 **語言統計** | 程式語言使用分布、檔案類型分析 | ✅ |
| 👥 **貢獻者分析** | 團隊成員貢獻度排行、協作模式 | ✅ |
| 📊 **視覺化報告** | 終端條形圖、熱力圖、摘要面板 | ✅ |
| 🔄 **JSON 匯出** | 支援結構化資料匯出供進一步分析 | ✅ |

### 🚀 快速開始

#### 環境要求

- **Python**: 3.8 或更高版本
- **Git**: 已安裝並配置
- **作業系統**: Linux / macOS / Windows

#### 安裝步驟

**方式一：直接執行（推薦）**

```bash
# 克隆倉庫
git clone https://github.com/yourusername/devmetrics-cli.git
cd devmetrics-cli

# 直接執行
python devmetrics.py
```

**方式二：安裝為系統命令**

```bash
# 安裝
pip install -e .

# 使用全域命令
devmetrics
# 或簡寫
dm
```

#### 本地啟動

```bash
# 分析目前目錄的 Git 倉庫
python devmetrics.py

# 分析指定倉庫
python devmetrics.py /path/to/your/repo

# 分析最近 30 天
python devmetrics.py --since "30 days ago"

# 分析特定作者的貢獻
python devmetrics.py --author "Your Name"

# 匯出 JSON 格式
python devmetrics.py --json
```

### 📖 詳細使用指南

#### 命令列參數

```
usage: devmetrics.py [-h] [--since SINCE] [--until UNTIL] [--author AUTHOR]
                     [--json] [--limit LIMIT] [--version]
                     [path]

DevMetrics-CLI: 開發者程式碼度量與生產力分析引擎

positional arguments:
  path              倉庫路徑 (預設: 目前目錄)

optional arguments:
  -h, --help        顯示說明資訊
  --since SINCE     開始日期 (如: "30 days ago", "2024-01-01")
  --until UNTIL     結束日期
  --author AUTHOR   指定作者
  --json            輸出 JSON 格式
  --limit LIMIT     最大提交數 (預設: 1000)
  --version         顯示版本資訊
```

### 💡 設計思路與迭代規劃

#### 技術選型原因

- **純標準庫實現**：確保零依賴，任何 Python 環境均可直接執行
- **Git 命令解析**：直接呼叫 Git CLI，相容所有 Git 版本
- **終端視覺化**：使用 ANSI 轉義碼實現跨平台彩色輸出

#### 後續功能迭代計劃

- [ ] 趨勢分析（週/月對比）
- [ ] 程式碼複雜度估算
- [ ] 提交資訊品質分析
- [ ] HTML 報告匯出
- [ ] 設定檔支援
- [ ] 多倉庫聚合分析

### 📦 打包與部署指南

```bash
# 清理並構建
make clean
make build

# 分發包將生成在 dist/ 目錄
pip install dist/devmetrics_cli-1.0.0-py3-none-any.whl
```

### 🤝 貢獻指南

1. Fork 本倉庫
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 建立 Pull Request

### 📄 開源協議

本專案採用 [MIT](LICENSE) 協議開源。

---

<a name="english"></a>
## 🇺🇸 English

### 🎉 Introduction

**DevMetrics-CLI** is a lightweight code metrics and productivity analysis tool designed for developers. It analyzes Git commit history to help developers gain insights into their coding habits, time distribution, language preferences, and contribution patterns.

**Inspiration**: In the era of AI-assisted programming, developers need to better understand their coding behavior patterns to optimize work efficiency and improve code quality.

**Key Differentiators**:
- 🚀 **Zero Dependencies** - Uses only Python standard library, no third-party packages required
- 📊 **Terminal Visualization** - Beautiful command-line charts and heatmaps
- ⚡ **Lightning Fast** - Local execution, no data upload, privacy protected
- 🎯 **Multi-dimensional Insights** - Analysis from time, language, contributor perspectives

### ✨ Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📈 **Commit Statistics** | Total commits, line changes, files modified | ✅ |
| ⏰ **Time Analysis** | Activity heatmaps, peak coding time identification | ✅ |
| 💻 **Language Stats** | Programming language distribution, file type analysis | ✅ |
| 👥 **Contributor Analysis** | Team member contribution ranking, collaboration patterns | ✅ |
| 📊 **Visual Reports** | Terminal bar charts, heatmaps, summary panels | ✅ |
| 🔄 **JSON Export** | Structured data export for further analysis | ✅ |

### 🚀 Quick Start

#### Requirements

- **Python**: 3.8 or higher
- **Git**: Installed and configured
- **OS**: Linux / macOS / Windows

#### Installation

**Option 1: Direct Run (Recommended)**

```bash
# Clone repository
git clone https://github.com/yourusername/devmetrics-cli.git
cd devmetrics-cli

# Run directly
python devmetrics.py
```

**Option 2: Install as System Command**

```bash
# Install
pip install -e .

# Use global command
devmetrics
# or shorthand
dm
```

#### Usage

```bash
# Analyze current directory Git repository
python devmetrics.py

# Analyze specific repository
python devmetrics.py /path/to/your/repo

# Analyze last 30 days
python devmetrics.py --since "30 days ago"

# Analyze specific author contributions
python devmetrics.py --author "Your Name"

# Export JSON format
python devmetrics.py --json
```

### 📖 Detailed Usage

#### Command Line Arguments

```
usage: devmetrics.py [-h] [--since SINCE] [--until UNTIL] [--author AUTHOR]
                     [--json] [--limit LIMIT] [--version]
                     [path]

DevMetrics-CLI: Developer Code Metrics & Productivity Analysis Engine

positional arguments:
  path              Repository path (default: current directory)

optional arguments:
  -h, --help        Show help message
  --since SINCE     Start date (e.g., "30 days ago", "2024-01-01")
  --until UNTIL     End date
  --author AUTHOR   Specific author
  --json            Output JSON format
  --limit LIMIT     Maximum commits (default: 1000)
  --version         Show version
```

### 💡 Design & Roadmap

#### Technical Choices

- **Pure Standard Library**: Ensures zero dependencies, runs in any Python environment
- **Git CLI Parsing**: Direct Git CLI calls, compatible with all Git versions
- **Terminal Visualization**: ANSI escape codes for cross-platform colored output

#### Future Roadmap

- [ ] Trend analysis (week/month comparison)
- [ ] Code complexity estimation
- [ ] Commit message quality analysis
- [ ] HTML report export
- [ ] Configuration file support
- [ ] Multi-repository aggregation

### 📦 Packaging & Deployment

```bash
# Clean and build
make clean
make build

# Distribution packages in dist/ directory
pip install dist/devmetrics_cli-1.0.0-py3-none-any.whl
```

### 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

### 📄 License

This project is open source under the [MIT](LICENSE) License.

---

<div align="center">

**Made with ❤️ by DevMetrics Team**

</div>
