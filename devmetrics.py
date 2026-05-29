#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevMetrics-CLI
轻量级开发者生产力指标追踪与分析引擎
Lightweight Developer Productivity Metrics Tracking & Analysis Engine

Zero Dependencies | Local-First | Privacy-First | TUI Dashboard
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional, Any

__version__ = "1.0.0"
__author__ = "DevMetrics Team"

# ANSI Color Codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bg_blue': '\033[44m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
}

class DevMetrics:
    """开发者生产力指标分析核心类"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = os.path.abspath(repo_path)
        self.commits: List[Dict] = []
        self.stats: Dict[str, Any] = {}
        self.languages: Dict[str, int] = {}

    def _run_git_command(self, args: List[str]) -> str:
        """执行Git命令并返回输出"""
        try:
            result = subprocess.run(
                ['git'] + args,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            return result.stdout.strip()
        except Exception as e:
            return ""

    def is_git_repo(self) -> bool:
        """检查是否为Git仓库"""
        git_dir = os.path.join(self.repo_path, '.git')
        return os.path.isdir(git_dir)

    def get_repo_name(self) -> str:
        """获取仓库名称"""
        return os.path.basename(self.repo_path)

    def get_current_branch(self) -> str:
        """获取当前分支"""
        return self._run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])

    def get_remote_url(self) -> str:
        """获取远程仓库URL"""
        return self._run_git_command(['remote', 'get-url', 'origin'])

    def fetch_commits(self, days: int = 30, author: str = None) -> List[Dict]:
        """获取提交历史"""
        since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        # 格式化: hash|date|author|email|message
        format_str = '%H|%aI|%an|%ae|%s'

        args = [
            'log',
            f'--since={since_date}',
            f'--pretty=format:{format_str}',
            '--no-merges'
        ]

        if author:
            args.extend(['--author', author])

        output = self._run_git_command(args)

        commits = []
        for line in output.split('\n'):
            if '|' not in line:
                continue
            parts = line.split('|', 4)
            if len(parts) >= 5:
                commits.append({
                    'hash': parts[0],
                    'date': parts[1],
                    'author': parts[2],
                    'email': parts[3],
                    'message': parts[4]
                })

        self.commits = commits
        return commits

    def analyze_commit_frequency(self) -> Dict[str, int]:
        """分析提交频率（按天）"""
        daily_commits = defaultdict(int)
        for commit in self.commits:
            date = commit['date'][:10]  # YYYY-MM-DD
            daily_commits[date] += 1
        return dict(sorted(daily_commits.items()))

    def analyze_commit_hours(self) -> Dict[int, int]:
        """分析提交时间分布（按小时）"""
        hourly_commits = defaultdict(int)
        for commit in self.commits:
            hour = int(commit['date'][11:13])  # HH
            hourly_commits[hour] += 1
        return dict(sorted(hourly_commits.items()))

    def analyze_commit_weekdays(self) -> Dict[str, int]:
        """分析提交星期分布"""
        weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        weekday_commits = defaultdict(int)

        for commit in self.commits:
            date_str = commit['date'][:10]
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            weekday = weekdays[date_obj.weekday()]
            weekday_commits[weekday] += 1

        return dict(weekday_commits)

    def analyze_contributors(self) -> Dict[str, int]:
        """分析贡献者统计"""
        contributors = defaultdict(int)
        for commit in self.commits:
            contributors[commit['author']] += 1
        return dict(sorted(contributors.items(), key=lambda x: x[1], reverse=True))

    def analyze_code_changes(self) -> Dict[str, int]:
        """分析代码变更统计"""
        args = ['log', '--shortstat', '--pretty=format:', '--since=30 days ago']
        output = self._run_git_command(args)

        stats = {'insertions': 0, 'deletions': 0, 'files_changed': 0}

        for line in output.split('\n'):
            if 'insertion' in line:
                match = re.search(r'(\d+) insertion', line)
                if match:
                    stats['insertions'] += int(match.group(1))
            if 'deletion' in line:
                match = re.search(r'(\d+) deletion', line)
                if match:
                    stats['deletions'] += int(match.group(1))
            if 'file' in line:
                match = re.search(r'(\d+) file', line)
                if match:
                    stats['files_changed'] += int(match.group(1))

        return stats

    def detect_languages(self) -> Dict[str, int]:
        """检测项目编程语言"""
        lang_extensions = {
            'Python': ['.py'],
            'JavaScript': ['.js', '.jsx', '.mjs'],
            'TypeScript': ['.ts', '.tsx'],
            'Java': ['.java'],
            'Go': ['.go'],
            'Rust': ['.rs'],
            'C++': ['.cpp', '.cc', '.cxx', '.hpp'],
            'C': ['.c', '.h'],
            'Ruby': ['.rb'],
            'PHP': ['.php'],
            'Swift': ['.swift'],
            'Kotlin': ['.kt', '.kts'],
            'C#': ['.cs'],
            'Shell': ['.sh', '.bash', '.zsh'],
            'HTML': ['.html', '.htm'],
            'CSS': ['.css', '.scss', '.sass', '.less'],
            'Markdown': ['.md', '.markdown'],
            'JSON': ['.json'],
            'YAML': ['.yml', '.yaml'],
            'SQL': ['.sql'],
            'Vue': ['.vue'],
        }

        lang_counts = defaultdict(int)

        for root, dirs, files in os.walk(self.repo_path):
            # 跳过.git和node_modules等目录
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv', '.venv', 'dist', 'build']]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                for lang, extensions in lang_extensions.items():
                    if ext in extensions:
                        lang_counts[lang] += 1
                        break

        self.languages = dict(sorted(lang_counts.items(), key=lambda x: x[1], reverse=True))
        return self.languages

    def calculate_productivity_score(self) -> int:
        """计算生产力评分（0-100）"""
        if not self.commits:
            return 0

        score = 0

        # 提交频率评分 (0-30)
        commit_count = len(self.commits)
        if commit_count >= 50:
            score += 30
        elif commit_count >= 30:
            score += 20
        elif commit_count >= 10:
            score += 10
        else:
            score += 5

        # 代码变更评分 (0-30)
        changes = self.analyze_code_changes()
        total_changes = changes.get('insertions', 0) + changes.get('deletions', 0)
        if total_changes >= 1000:
            score += 30
        elif total_changes >= 500:
            score += 20
        elif total_changes >= 100:
            score += 10
        else:
            score += 5

        # 一致性评分 (0-20)
        daily_commits = self.analyze_commit_frequency()
        active_days = len(daily_commits)
        if active_days >= 20:
            score += 20
        elif active_days >= 10:
            score += 15
        elif active_days >= 5:
            score += 10
        else:
            score += 5

        # 多样性评分 (0-20)
        lang_count = len(self.languages)
        if lang_count >= 3:
            score += 20
        elif lang_count >= 2:
            score += 15
        elif lang_count >= 1:
            score += 10
        else:
            score += 5

        return min(score, 100)


class TUI:
    """终端用户界面类"""

    def __init__(self):
        self.width = self._get_terminal_width()

    def _get_terminal_width(self) -> int:
        """获取终端宽度"""
        try:
            import shutil
            return shutil.get_terminal_size().columns
        except:
            return 80

    def color(self, text: str, color: str) -> str:
        """添加颜色"""
        return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

    def bold(self, text: str) -> str:
        """加粗文本"""
        return self.color(text, 'bold')

    def print_header(self, title: str):
        """打印标题"""
        print()
        print(self.color("═" * self.width, 'cyan'))
        print(self.color(f"  {title}", 'bold').center(self.width))
        print(self.color("═" * self.width, 'cyan'))
        print()

    def print_section(self, title: str):
        """打印章节标题"""
        print()
        print(self.color(f"▸ {title}", 'bold'))
        print(self.color("─" * (len(title) + 3), 'dim'))

    def print_stat(self, label: str, value: str, color: str = 'white'):
        """打印统计项"""
        print(f"  {self.color(label, 'dim')}: {self.color(value, color)}")

    def print_bar_chart(self, data: Dict[str, int], max_width: int = 40):
        """打印条形图"""
        if not data:
            print("  暂无数据")
            return

        max_value = max(data.values()) if data else 1
        max_label_len = max(len(str(k)) for k in data.keys()) if data else 0

        for label, value in data.items():
            bar_len = int((value / max_value) * max_width) if max_value > 0 else 0
            bar = "█" * bar_len
            percentage = (value / sum(data.values()) * 100) if sum(data.values()) > 0 else 0
            label_str = str(label).ljust(max_label_len)
            print(f"  {label_str} │{self.color(bar, 'green')} {value} ({percentage:.1f}%)")

    def print_progress_bar(self, label: str, value: int, max_value: int = 100, color: str = 'green'):
        """打印进度条"""
        bar_width = 30
        filled = int((value / max_value) * bar_width) if max_value > 0 else 0
        bar = "█" * filled + "░" * (bar_width - filled)
        print(f"  {label:15} │{self.color(bar, color)} {value}/{max_value}")

    def print_heatmap(self, data: Dict[int, int], title: str = "提交热力图"):
        """打印小时热力图"""
        print(f"\n  {self.bold(title)}")

        max_value = max(data.values()) if data else 1

        for hour in range(24):
            count = data.get(hour, 0)
            intensity = int((count / max_value) * 4) if max_value > 0 else 0

            if count == 0:
                char = self.color("·", 'dim')
            elif intensity == 1:
                char = self.color("░", 'cyan')
            elif intensity == 2:
                char = self.color("▒", 'blue')
            elif intensity == 3:
                char = self.color("▓", 'magenta')
            else:
                char = self.color("█", 'green')

            marker = "→" if hour == datetime.now().hour else " "
            print(f"  {marker}{hour:02d}:00 {char} {count}")

    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')


def format_duration(seconds: int) -> str:
    """格式化时长"""
    if seconds < 60:
        return f"{seconds}秒"
    elif seconds < 3600:
        return f"{seconds // 60}分钟"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}小时{minutes}分钟"


def generate_json_report(metrics: DevMetrics, output_path: str):
    """生成JSON报告"""
    report = {
        'generated_at': datetime.now().isoformat(),
        'repository': {
            'name': metrics.get_repo_name(),
            'path': metrics.repo_path,
            'branch': metrics.get_current_branch(),
            'remote': metrics.get_remote_url(),
        },
        'summary': {
            'total_commits': len(metrics.commits),
            'productivity_score': metrics.calculate_productivity_score(),
        },
        'commits': {
            'frequency': metrics.analyze_commit_frequency(),
            'hourly_distribution': metrics.analyze_commit_hours(),
            'weekday_distribution': metrics.analyze_commit_weekdays(),
        },
        'contributors': metrics.analyze_contributors(),
        'code_changes': metrics.analyze_code_changes(),
        'languages': metrics.languages,
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report


def generate_markdown_report(metrics: DevMetrics, output_path: str):
    """生成Markdown报告"""
    lines = []
    lines.append("# 📊 DevMetrics 分析报告")
    lines.append("")
    lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # 仓库信息
    lines.append("## 📁 仓库信息")
    lines.append("")
    lines.append(f"- **仓库名称**: {metrics.get_repo_name()}")
    lines.append(f"- **仓库路径**: `{metrics.repo_path}`")
    lines.append(f"- **当前分支**: `{metrics.get_current_branch()}`")
    lines.append("")

    # 概览
    lines.append("## 📈 概览统计")
    lines.append("")
    lines.append(f"- **总提交数**: {len(metrics.commits)}")
    lines.append(f"- **生产力评分**: {metrics.calculate_productivity_score()}/100")
    lines.append("")

    # 代码变更
    changes = metrics.analyze_code_changes()
    lines.append("## 📝 代码变更 (最近30天)")
    lines.append("")
    lines.append(f"- **新增行数**: +{changes.get('insertions', 0)}")
    lines.append(f"- **删除行数**: -{changes.get('deletions', 0)}")
    lines.append(f"- **变更文件**: {changes.get('files_changed', 0)}")
    lines.append("")

    # 语言分布
    if metrics.languages:
        lines.append("## 💻 编程语言分布")
        lines.append("")
        lines.append("| 语言 | 文件数 |")
        lines.append("|------|--------|")
        for lang, count in list(metrics.languages.items())[:10]:
            lines.append(f"| {lang} | {count} |")
        lines.append("")

    # 贡献者
    contributors = metrics.analyze_contributors()
    if contributors:
        lines.append("## 👥 贡献者")
        lines.append("")
        lines.append("| 贡献者 | 提交数 |")
        lines.append("|--------|--------|")
        for author, count in list(contributors.items())[:10]:
            lines.append(f"| {author} | {count} |")
        lines.append("")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description='DevMetrics-CLI - 轻量级开发者生产力指标追踪与分析引擎',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                          # 分析当前目录
  %(prog)s /path/to/repo            # 分析指定仓库
  %(prog)s --days 7                 # 分析最近7天
  %(prog)s --json report.json       # 导出JSON报告
  %(prog)s --markdown report.md     # 导出Markdown报告
        """
    )

    parser.add_argument('path', nargs='?', default='.', help='仓库路径 (默认: 当前目录)')
    parser.add_argument('--days', '-d', type=int, default=30, help='分析天数 (默认: 30)')
    parser.add_argument('--author', '-a', help='指定作者过滤')
    parser.add_argument('--json', '-j', metavar='FILE', help='导出JSON报告')
    parser.add_argument('--markdown', '-m', metavar='FILE', help='导出Markdown报告')
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # 初始化
    tui = TUI()
    tui.clear_screen()
    tui.print_header("📊 DevMetrics-CLI v" + __version__)

    # 检查Git仓库
    metrics = DevMetrics(args.path)
    if not metrics.is_git_repo():
        print(tui.color("❌ 错误: 指定路径不是Git仓库", 'red'))
        print(f"   路径: {metrics.repo_path}")
        sys.exit(1)

    # 显示仓库信息
    tui.print_section("📁 仓库信息")
    tui.print_stat("仓库名称", metrics.get_repo_name(), 'cyan')
    tui.print_stat("仓库路径", metrics.repo_path, 'dim')
    tui.print_stat("当前分支", metrics.get_current_branch(), 'green')

    remote = metrics.get_remote_url()
    if remote:
        tui.print_stat("远程地址", remote[:50] + ('...' if len(remote) > 50 else ''), 'dim')

    # 获取数据
    print(tui.color("\n⏳ 正在分析提交历史...", 'yellow'))
    metrics.fetch_commits(days=args.days, author=args.author)

    print(tui.color("⏳ 正在检测编程语言...", 'yellow'))
    metrics.detect_languages()

    # 概览统计
    tui.print_section("📈 概览统计")
    tui.print_stat("分析时间范围", f"最近 {args.days} 天", 'cyan')
    tui.print_stat("总提交数", str(len(metrics.commits)), 'green')

    # 生产力评分
    score = metrics.calculate_productivity_score()
    score_color = 'green' if score >= 80 else 'yellow' if score >= 60 else 'red'
    tui.print_progress_bar("生产力评分", score, 100, score_color)

    # 代码变更统计
    changes = metrics.analyze_code_changes()
    tui.print_section("📝 代码变更")
    tui.print_stat("新增行数", f"+{changes.get('insertions', 0)}", 'green')
    tui.print_stat("删除行数", f"-{changes.get('deletions', 0)}", 'red')
    tui.print_stat("变更文件", str(changes.get('files_changed', 0)), 'cyan')

    # 编程语言
    if metrics.languages:
        tui.print_section("💻 编程语言分布")
        tui.print_bar_chart(dict(list(metrics.languages.items())[:8]))

    # 提交频率
    daily_commits = metrics.analyze_commit_frequency()
    if daily_commits:
        tui.print_section("📅 提交频率 (按天)")
        tui.print_bar_chart(dict(list(daily_commits.items())[-10:]))

    # 小时热力图
    hourly_commits = metrics.analyze_commit_hours()
    if hourly_commits:
        tui.print_heatmap(hourly_commits, "提交时间分布 (24小时)")

    # 星期分布
    weekday_commits = metrics.analyze_commit_weekdays()
    if weekday_commits:
        tui.print_section("📆 星期分布")
        weekday_order = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        ordered_weekdays = {k: weekday_commits.get(k, 0) for k in weekday_order}
        tui.print_bar_chart(ordered_weekdays)

    # 贡献者
    contributors = metrics.analyze_contributors()
    if len(contributors) > 1:
        tui.print_section("👥 贡献者统计")
        tui.print_bar_chart(dict(list(contributors.items())[:8]))

    # 导出报告
    if args.json:
        generate_json_report(metrics, args.json)
        print(f"\n{COLORS['green']}✓ JSON报告已保存: {args.json}{COLORS['reset']}")

    if args.markdown:
        generate_markdown_report(metrics, args.markdown)
        print(f"\n{COLORS['green']}✓ Markdown报告已保存: {args.markdown}{COLORS['reset']}")

    # 页脚
    print()
    print(tui.color("═" * tui.width, 'cyan'))
    print(tui.color("  🎉 分析完成! 使用 --json 或 --markdown 导出详细报告", 'dim').center(tui.width))
    print(tui.color("═" * tui.width, 'cyan'))
    print()


if __name__ == '__main__':
    main()
