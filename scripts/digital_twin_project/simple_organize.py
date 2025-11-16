#!/usr/bin/env python3
"""简化的AI Scientist文件整理脚本"""

import os
import shutil
from pathlib import Path

def organize_files():
    print("整理AI Scientist相关文件到AI-Scientist-main文件夹")

    # 创建目录
    scripts_dir = Path("AI-Scientist-main") / "scripts" / "digital_twin_project"
    reports_dir = Path("AI-Scientist-main") / "reports" / "digital_twin"

    scripts_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    # 定义文件列表
    scripts_to_move = [
        "analyze_digital_twin_corpus.py",
        "simple_analyze.py",
        "ai_scientist_digital_twin_demo_simple.py"
    ]

    reports_to_move = [
        "digital_twin_comprehensive_report.md",
        "digital_twin_executive_summary.md",
        "ai_scientist_review_report.md"
    ]

    # 移动脚本
    print("移动脚本文件...")
    for filename in scripts_to_move:
        src = Path(filename)
        dst = scripts_dir / filename
        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"  已移动: {filename}")

    # 移动报告
    print("移动报告文件...")
    for filename in reports_to_move:
        src = Path(filename)
        dst = reports_dir / filename
        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"  已移动: {filename}")

    print("文件整理完成！")
    print("检查AI-Scientist-main/scripts/digital_twin_project/")
    print("检查AI-Scientist-main/reports/digital_twin/")

if __name__ == "__main__":
    organize_files()
