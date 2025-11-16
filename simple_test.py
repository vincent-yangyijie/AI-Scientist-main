#!/usr/bin/env python3
"""简化的AI Scientist测试"""

import os

# 设置环境变量
os.environ['GEMINI_API_KEY'] = 'AIzaSyCxaUNsUN9I9aTJImYdlVIa22xLoeEBN9k'

try:
    from ai_scientist.llm import AVAILABLE_LLMS
    print(f"✓ AI Scientist模块已加载 - 支持 {len(AVAILABLE_LLMS)} 种模型")
    print(f"可用模型示例: {AVAILABLE_LLMS[:3]}")
    print("🎉 AI Scientist系统正常工作！")
except Exception as e:
    print(f"❌ 错误: {e}")
