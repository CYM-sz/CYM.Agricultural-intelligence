import os
from openai import OpenAI

# 初始化客户端（自动读取环境变量 OPENAI_API_KEY）
client = OpenAI()

def ask_agriculture_ai(user_input):
    system_prompt = """
You are an intelligent agricultural assistant.
Based on user's location, land condition, and goals, you provide:
1. Suitable crops
2. Planting instructions
3. Growth cycle
4. Nutrient management
5. Harvesting guidance
Keep answers practical and structured.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🌱 AI农业助手已启动（输入 exit 退出）")

    while True:
        user_input = input("\n你：")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 已退出")
            break

        answer = ask_agriculture_ai(user_input)
        print("\n🤖 AI建议：\n", answer)
