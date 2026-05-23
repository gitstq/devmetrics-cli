#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevMetrics-CLI: 轻量级开发者代码度量与生产力分析引擎
Lightweight Developer Code Metrics & Productivity Analysis Engine

Author: DevMetrics Team
License: MIT
Version: 1.0.0
"""

import os
import sys
import re
import json
import subprocess
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import argparse


class Colors:
    """终端颜色定义"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'


class DevMetrics:
    """开发者代码度量分析引擎"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.git_available = self._check_git()
        self.commits: List[Dict] = []
        self.stats = {
            'total_commits': 0,
            'total_files_changed': 0,
            'total_insertions': 0,
            'total_deletions': 0,
            'languages': Counter(),
            'hourly_activity': Counter(),
            'daily_activity': Counter(),
            'monthly_activity': Counter(),
            'file_extensions': Counter(),
            'commit_messages': [],
            'authors': Counter(),
            'active_days': set(),
        }

    def _check_git(self) -> bool:
        """检查Git是否可用"""
        try:
            subprocess.run(['git', '--version'], capture_output=True, check=True)
            git_dir = self.repo_path / '.git'
            return git_dir.exists()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def _run_git_command(self, args: List[str]) -> str:
        """运行Git命令"""
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

    def collect_commits(self, since: Optional[str] = None, until: Optional[str] = None,
                       author: Optional[str] = None, max_count: Optional[int] = None) -> List[Dict]:
        """收集提交历史"""
        cmd = ['log', '--pretty=format:%H|%an|%ae|%ad|%s', '--date=iso']

        if since:
            cmd.extend(['--since', since])
        if until:
            cmd.extend(['--until', until])
        if author:
            cmd.extend(['--author', author])
        if max_count:
            cmd.extend(['-n', str(max_count)])

        output = self._run_git_command(cmd)
        if not output:
            return []

        commits = []
        for line in output.split('\n'):
            if '|' in line:
                parts = line.split('|', 4)
                if len(parts) >= 5:
                    commits.append({
                        'hash': parts[0],
                        'author': parts[1],
                        'email': parts[2],
                        'date': parts[3],
                        'message': parts[4]
                    })

        self.commits = commits
        return commits

    def analyze_commit_stats(self) -> Dict:
        """分析提交统计"""
        if not self.commits:
            self.collect_commits()

        total_insertions = 0
        total_deletions = 0
        files_changed = 0

        for commit in self.commits[:100]:  # 限制分析最近的100个提交
            # 获取每个提交的统计
            cmd = ['show', '--stat', '--format=', commit['hash']]
            output = self._run_git_command(cmd)

            # 解析插入/删除行数
            insertions = re.findall(r'(\d+) insertion', output)
            deletions = re.findall(r'(\d+) deletion', output)
            files = re.findall(r'(\d+) file', output)

            total_insertions += sum(int(x) for x in insertions)
            total_deletions += sum(int(x) for x in deletions)
            files_changed += sum(int(x) for x in files)

        self.stats['total_commits'] = len(self.commits)
        self.stats['total_insertions'] = total_insertions
        self.stats['total_deletions'] = total_deletions
        self.stats['total_files_changed'] = files_changed

        return {
            'total_commits': len(self.commits),
            'total_insertions': total_insertions,
            'total_deletions': total_deletions,
            'total_files_changed': files_changed,
            'net_lines': total_insertions - total_deletions
        }

    def analyze_time_patterns(self) -> Dict:
        """分析时间模式"""
        if not self.commits:
            self.collect_commits()

        hourly = Counter()
        daily = Counter()
        monthly = Counter()
        active_days = set()

        for commit in self.commits:
            try:
                date_str = commit['date']
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00').replace('+', ' +').split(' +')[0])

                hourly[dt.hour] += 1
                daily[dt.strftime('%A')] += 1
                monthly[dt.strftime('%Y-%m')] += 1
                active_days.add(dt.strftime('%Y-%m-%d'))
            except:
                continue

        self.stats['hourly_activity'] = hourly
        self.stats['daily_activity'] = daily
        self.stats['monthly_activity'] = monthly
        self.stats['active_days'] = active_days

        return {
            'hourly': dict(hourly),
            'daily': dict(daily),
            'monthly': dict(monthly),
            'active_days_count': len(active_days),
            'most_active_hour': hourly.most_common(1)[0] if hourly else None,
            'most_active_day': daily.most_common(1)[0] if daily else None
        }

    def analyze_languages(self) -> Dict:
        """分析编程语言"""
        if not self.commits:
            self.collect_commits()

        extensions = Counter()
        language_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React',
            '.tsx': 'React TS',
            '.java': 'Java',
            '.go': 'Go',
            '.rs': 'Rust',
            '.cpp': 'C++',
            '.c': 'C',
            '.h': 'C/C++ Header',
            '.hpp': 'C++ Header',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.r': 'R',
            '.m': 'Objective-C',
            '.cs': 'C#',
            '.fs': 'F#',
            '.clj': 'Clojure',
            '.ex': 'Elixir',
            '.erl': 'Erlang',
            '.hs': 'Haskell',
            '.lua': 'Lua',
            '.pl': 'Perl',
            '.groovy': 'Groovy',
            '.dart': 'Dart',
            '.vue': 'Vue',
            '.svelte': 'Svelte',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sass': 'Sass',
            '.less': 'Less',
            '.json': 'JSON',
            '.xml': 'XML',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.toml': 'TOML',
            '.md': 'Markdown',
            '.sql': 'SQL',
            '.sh': 'Shell',
            '.bash': 'Bash',
            '.zsh': 'Zsh',
            '.ps1': 'PowerShell',
            '.dockerfile': 'Dockerfile',
            '.tf': 'Terraform',
            '.tfvars': 'Terraform',
            '.proto': 'Protocol Buffers',
            '.graphql': 'GraphQL',
            '.prisma': 'Prisma',
        }

        languages = Counter()

        for commit in self.commits[:50]:  # 分析最近50个提交
            cmd = ['show', '--name-only', '--format=', commit['hash']]
            output = self._run_git_command(cmd)

            for line in output.split('\n'):
                if '.' in line:
                    ext = '.' + line.split('.')[-1].lower()
                    extensions[ext] += 1
                    if ext in language_map:
                        languages[language_map[ext]] += 1

        self.stats['file_extensions'] = extensions
        self.stats['languages'] = languages

        return {
            'languages': dict(languages.most_common(10)),
            'extensions': dict(extensions.most_common(10))
        }

    def analyze_contributors(self) -> Dict:
        """分析贡献者"""
        if not self.commits:
            self.collect_commits()

        authors = Counter()
        for commit in self.commits:
            authors[commit['author']] += 1

        self.stats['authors'] = authors

        return {
            'total_contributors': len(authors),
            'top_contributors': authors.most_common(10)
        }

    def generate_report(self) -> Dict:
        """生成完整报告"""
        if not self.git_available:
            return {'error': 'Not a git repository or git not available'}

        return {
            'repository': str(self.repo_path),
            'generated_at': datetime.now().isoformat(),
            'commit_stats': self.analyze_commit_stats(),
            'time_patterns': self.analyze_time_patterns(),
            'languages': self.analyze_languages(),
            'contributors': self.analyze_contributors()
        }


class TerminalUI:
    """终端用户界面"""

    def __init__(self):
        self.width = self._get_terminal_width()

    def _get_terminal_width(self) -> int:
        """获取终端宽度"""
        try:
            import shutil
            return shutil.get_terminal_size().columns
        except:
            return 80

    def print_header(self, title: str):
        """打印标题"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * self.width}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{title.center(self.width)}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * self.width}{Colors.RESET}\n")

    def print_section(self, title: str):
        """打印章节标题"""
        print(f"\n{Colors.BOLD}{Colors.YELLOW}▶ {title}{Colors.RESET}")
        print(f"{Colors.DIM}{'─' * (len(title) + 3)}{Colors.RESET}")

    def print_stat(self, label: str, value: str, color: str = Colors.WHITE):
        """打印统计项"""
        print(f"  {Colors.DIM}•{Colors.RESET} {label}: {color}{Colors.BOLD}{value}{Colors.RESET}")

    def print_bar_chart(self, data: Dict, max_width: int = 40):
        """打印条形图"""
        if not data:
            return

        max_val = max(data.values()) if data else 1
        max_label_len = max(len(str(k)) for k in data.keys())

        for label, value in data.items():
            bar_len = int((value / max_val) * max_width) if max_val > 0 else 0
            bar = '█' * bar_len
            pct = (value / sum(data.values()) * 100) if sum(data.values()) > 0 else 0
            print(f"  {str(label):>{max_label_len}} │{Colors.GREEN}{bar}{Colors.RESET} {value} ({pct:.1f}%)")

    def print_heatmap(self, data: Counter, title: str = ""):
        """打印热力图"""
        if not data:
            return

        max_val = max(data.values()) if data else 1
        blocks = [' ', '░', '▒', '▓', '█']

        print(f"\n  {Colors.BOLD}{title}{Colors.RESET}")
        for label, value in sorted(data.items()):
            intensity = min(int((value / max_val) * 4), 4)
            block = blocks[intensity]
            color = Colors.GREEN if intensity >= 3 else (Colors.YELLOW if intensity >= 2 else Colors.DIM)
            print(f"    {str(label):>10} {color}{block * 20}{Colors.RESET} {value}")

    def print_summary_box(self, stats: Dict):
        """打印摘要框"""
        print(f"\n{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} 📊 DEVMETRICS SUMMARY {Colors.RESET}")
        print(f"{Colors.CYAN}┌{'─' * (self.width - 2)}┐{Colors.RESET}")

        items = [
            ("Total Commits", stats.get('total_commits', 0), Colors.GREEN),
            ("Files Changed", stats.get('total_files_changed', 0), Colors.YELLOW),
            ("Lines Added", stats.get('total_insertions', 0), Colors.GREEN),
            ("Lines Deleted", stats.get('total_deletions', 0), Colors.RED),
            ("Net Change", stats.get('total_insertions', 0) - stats.get('total_deletions', 0),
             Colors.CYAN if stats.get('total_insertions', 0) >= stats.get('total_deletions', 0) else Colors.RED),
        ]

        for label, value, color in items:
            line = f"  {label:<15} {color}{value:>10,}{Colors.RESET}  "
            padding = self.width - len(line) + len(color) + len(Colors.RESET) * 2
            print(f"{Colors.CYAN}│{Colors.RESET}{line}{' ' * (padding - 25)}{Colors.CYAN}│{Colors.RESET}")

        print(f"{Colors.CYAN}└{'─' * (self.width - 2)}┘{Colors.RESET}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='DevMetrics-CLI: 开发者代码度量与生产力分析引擎',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                          # 分析当前目录
  %(prog)s /path/to/repo            # 分析指定仓库
  %(prog)s --since "30 days ago"    # 分析最近30天
  %(prog)s --author "John Doe"      # 分析特定作者
  %(prog)s --json                   # 输出JSON格式
        """
    )

    parser.add_argument('path', nargs='?', default='.', help='仓库路径 (默认: 当前目录)')
    parser.add_argument('--since', help='开始日期 (如: "30 days ago", "2024-01-01")')
    parser.add_argument('--until', help='结束日期')
    parser.add_argument('--author', help='指定作者')
    parser.add_argument('--json', action='store_true', help='输出JSON格式')
    parser.add_argument('--limit', type=int, default=1000, help='最大提交数 (默认: 1000)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    # 初始化
    metrics = DevMetrics(args.path)
    ui = TerminalUI()

    if not metrics.git_available:
        print(f"{Colors.RED}Error: Not a git repository or git not available{Colors.RESET}")
        sys.exit(1)

    # 收集数据
    metrics.collect_commits(since=args.since, until=args.until, author=args.author, max_count=args.limit)

    if args.json:
        # JSON输出
        report = metrics.generate_report()
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        # 终端可视化输出
        ui.print_header("🔥 DEVMETRICS-CLI v1.0.0")
        print(f"{Colors.DIM}Repository: {Colors.RESET}{Colors.CYAN}{metrics.repo_path}{Colors.RESET}")
        print(f"{Colors.DIM}Generated:  {Colors.RESET}{Colors.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")

        # 提交统计
        ui.print_section("📈 Commit Statistics")
        commit_stats = metrics.analyze_commit_stats()
        ui.print_summary_box(commit_stats)

        # 时间模式
        ui.print_section("⏰ Time Patterns")
        time_patterns = metrics.analyze_time_patterns()

        if time_patterns.get('most_active_hour'):
            ui.print_stat("Most Active Hour", f"{time_patterns['most_active_hour'][0]}:00 ({time_patterns['most_active_hour'][1]} commits)", Colors.GREEN)
        if time_patterns.get('most_active_day'):
            ui.print_stat("Most Active Day", f"{time_patterns['most_active_day'][0]} ({time_patterns['most_active_day'][1]} commits)", Colors.GREEN)
        ui.print_stat("Active Days", str(time_patterns['active_days_count']), Colors.CYAN)

        if time_patterns.get('hourly'):
            ui.print_heatmap(Counter(time_patterns['hourly']), "Hourly Activity")

        # 编程语言
        ui.print_section("💻 Programming Languages")
        languages = metrics.analyze_languages()
        if languages.get('languages'):
            ui.print_bar_chart(languages['languages'])

        # 贡献者
        ui.print_section("👥 Contributors")
        contributors = metrics.analyze_contributors()
        ui.print_stat("Total Contributors", str(contributors['total_contributors']), Colors.CYAN)
        if contributors.get('top_contributors'):
            print(f"\n  {Colors.BOLD}Top Contributors:{Colors.RESET}")
            for name, count in contributors['top_contributors'][:5]:
                print(f"    {Colors.GREEN}•{Colors.RESET} {name}: {Colors.BOLD}{count}{Colors.RESET} commits")

        # 页脚
        print(f"\n{Colors.DIM}{'=' * ui.width}{Colors.RESET}")
        print(f"{Colors.DIM}DevMetrics-CLI v1.0.0 | MIT License | Generated with ❤️{Colors.RESET}\n")


if __name__ == '__main__':
    main()
