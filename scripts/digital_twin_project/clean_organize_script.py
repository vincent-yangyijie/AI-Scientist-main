#!/usr/bin/env python3
"""AI Scientist系统文件组织整理工具 - 简化版"""

import os
import shutil
from pathlib import Path

def organize_ai_scientist_files():
    """整理AI Scientist相关文件到AI-Scientist-main文件夹"""

    print("开始整理AI Scientist系统文件到AI-Scientist-main文件夹")
    print("="*60)

    # 定义目标目录
    scripts_dir = Path("AI-Scientist-main") / "scripts" / "digital_twin_project"
    reports_dir = Path("AI-Scientist-main") / "reports" / "digital_twin"
    docs_dir = Path("AI-Scientist-main") / "docs" / "digital_twin_reports"

    # 创建目录结构
    for directory in [scripts_dir, reports_dir, docs_dir]:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"创建目录: {directory}")

    # 定义需要移动的文件列表
    script_files = [
        "analyze_digital_twin_corpus.py",
        "simple_analyze.py",
        "ai_scientist_digital_twin_demo_simple.py",
        "ai_scientist_digital_twin_demo.py",
        "generate_creative_research_report.py",
        "simple_creative_report.py",
        "generate_review_report.py",
        "generate_experiment_validation_scheme.py",
        "organize_ai_scientist_files.py"
    ]

    report_files = [
        "digital_twin_comprehensive_report.md",
        "digital_twin_executive_summary.md",
        "digital_twin_creative_final_report.md",
        "ai_scientist_review_report.md",
        "ai_scientist_evaluation_summary.md"
    ]

    # 统计
    moved_scripts = 0
    moved_reports = 0

    # 移动脚本文件
    print("\n移动脚本文件...")
    for filename in script_files:
        src = Path(filename)
        dst = scripts_dir / filename

        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"  ✅ {filename}")
            moved_scripts += 1
        else:
            print(f"  ⚠️  {filename} 不存在")

    # 移动报告文件
    print("\n移动报告文件...")
    for filename in report_files:
        src = Path(filename)
        dst = reports_dir / filename

        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"  ✅ {filename}")
            moved_reports += 1
        else:
            print(f"  ⚠️  {filename} 不存在")

    # 创建项目README
    readme_content = f"""# AI Scientist 数字孪生项目整理说明

## 文件整理结果

✅ **脚本文件** ({moved_scripts}个):
- 位置: AI-Scientist-main/scripts/digital_twin_project/
- 包含: 分析脚本、生成器、演示程序

✅ **报告文件** ({moved_reports}个):
- 位置: AI-Scientist-main/reports/digital_twin/
- 包含: 趋势报告、创新创意、系统评审等

## 使用说明

1. 进入AI-Scientist-main目录查看整理后的文件
2. 运行脚本: python scripts/digital_twin_project/simple_analyze.py
3. 查看报告: reports/digital_twin/下的所有.md文件

整理时间: {datetime.now().strftime('%Y年%m月%d日')}"""

    from datetime import datetime
    with open("AI-Scientist-main/file_organization_guide.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("
整理完成！"    print(f"脚本文件: {moved_scripts}个 → scripts/digital_twin_project/")
    print(f"报告文件: {moved_reports}个 → reports/digital_twin/")
    print("使用指南: AI-Scientist-main/file_organization_guide.md")

if __name__ == "__main__":
    organize_ai_scientist_files()
