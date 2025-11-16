#!/usr/bin/env python3
"""测试Gemini-2.0-flash支持"""

import os

# 设置环境变量
os.environ['GEMINI_API_KEY'] = 'AIzaSyCxaUNsUN9I9aTJImYdlVIa22xLoeEBN9k'

print("🧪 测试Gemini-2.0-flash支持")
print("="*40)

try:
    from ai_scientist.llm import AVAILABLE_LLMS, create_client, get_response_from_llm

    # 检查是否支持gemini-2.0-flash
    gemini_20_flash = 'gemini-2.0-flash'
    if gemini_20_flash in AVAILABLE_LLMS:
        print(f"✓ {gemini_20_flash} 在支持列表中")

        # 测试客户端创建
        print(f"\n🔗 创建 {gemini_20_flash} 客户端...")
        client, model = create_client(gemini_20_flash)
        print(f"✓ 客户端创建成功: {model}")

        # 显示所有Gemini模型
        gemini_models = [m for m in AVAILABLE_LLMS if 'gemini' in m]
        print(f"\n📋 所有Gemini模型 ({len(gemini_models)} 个):")
        for model in gemini_models:
            print(f"  • {model}")

        print(f"\n🎉 {gemini_20_flash} 已成功集成到AI Scientist中!")

    else:
        print(f"❌ {gemini_20_flash} 不在支持列表中")
        print("可用Gemini模型:")
        for m in AVAILABLE_LLMS:
            if 'gemini' in m:
                print(f"  • {m}")

except Exception as e:
    print(f"❌ 错误: {e}")
    import traceback
    traceback.print_exc()
