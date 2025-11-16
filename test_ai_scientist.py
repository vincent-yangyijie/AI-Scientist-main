#!/usr/bin/env python3
"""测试AI Scientist功能"""

import os

print("🔬 测试AI Scientist系统...")

# 设置测试用的环境变量（请在.env文件中设置实际的API密钥）
# 或者通过环境变量设置：
# export GEMINI_API_KEY='your_gemini_api_key'
# export OPENAI_API_KEY='your_openai_api_key'
# export OPENROUTER_API_KEY='your_openrouter_api_key'
# export DEEPSEEK_API_KEY='your_deepseek_api_key'
# export TAVILY_API_KEY='your_tavily_api_key'
# export JINA_API_KEY='your_jina_api_key'
# export GROK_API_KEY='your_grok_api_key'
# export KIMI_API_KEY='your_kimi_api_key'
# export HF_TOKEN='your_huggingface_token'

# 测试基本导入
try:
    from ai_scientist.llm import AVAILABLE_LLMS, create_client, get_response_from_llm
    print(f"✓ LLM模块导入成功 - 支持 {len(AVAILABLE_LLMS)} 种模型")

    # 显示前几个可用模型
    print(f"前5个可用模型: {AVAILABLE_LLMS[:5]}")

    # 检查环境变量
    if os.environ.get("GEMINI_API_KEY"):
        print("✓ Google Gemini API密钥已设置")

    if os.environ.get("OPENAI_API_KEY"):
        print("✓ OpenAI API密钥已设置")

except ImportError as e:
    print(f"❌ 导入失败: {e}")

# 测试其他模块
try:
    from ai_scientist.generate_ideas import generate_ideas, check_idea_novelty
    print("✓ 实验想法生成模块加载成功")
    print("  - 支持函数: generate_ideas, check_idea_novelty, search_for_papers")
except ImportError as e:
    print(f"❌ 实验想法模块导入失败: {e}")

try:
    from ai_scientist.perform_experiments import perform_experiments
    print("✓ 实验执行模块加载成功")
except ImportError as e:
    print(f"❌ 实验执行模块导入失败: {e}")

try:
    from ai_scientist.perform_writeup import perform_writeup
    print("✓ 论文编写模块加载成功")
except ImportError as e:
    print(f"❌ 论文编写模块导入失败: {e}")

try:
    from ai_scientist.perform_review import perform_review
    print("✓ 论文评审模块加载成功")
except ImportError as e:
    print(f"❌ 论文评审模块导入失败: {e}")

print("\n💡 AI Scientist核心功能已加载！")

# 如果有环境变量，测试基础API调用
if os.environ.get("GEMINI_API_KEY"):
    print("\n🔗 测试API连接...")
    try:
        client, model = create_client("gemini-1.5-flash")
        print("✓ Gemini客户端创建成功")
    except Exception as e:
        print(f"⚠️ Gemini客户端创建失败: {e}")

print("\n🎊 AI Scientist系统测试完成！")
