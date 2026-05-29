# 🤝 贡献指南

感谢您对 DevMetrics-CLI 的兴趣！我们欢迎各种形式的贡献。

## 🚀 如何贡献

### 报告问题

如果您发现了bug或有功能建议，请通过 GitHub Issues 提交：

1. 检查是否已有相关问题
2. 使用对应的 Issue 模板
3. 提供详细的复现步骤（如果是bug）
4. 标注相关标签

### 提交代码

1. **Fork 仓库**
   ```bash
   git clone https://github.com/your-username/DevMetrics-CLI.git
   cd DevMetrics-CLI
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/bug-description
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   ```

4. **推送并创建 Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `perf:` 性能优化
- `test:` 测试相关
- `chore:` 构建/工具相关

### 代码规范

- 遵循 PEP 8 规范
- 添加适当的注释和文档字符串
- 保持零依赖设计原则
- 确保代码在 Python 3.7+ 兼容

## 📋 开发环境

```bash
# 克隆仓库
git clone https://github.com/gitstq/DevMetrics-CLI.git
cd DevMetrics-CLI

# 安装开发模式
pip install -e .

# 运行测试
python devmetrics.py --help
```

## 🙏 感谢

感谢您的贡献！
