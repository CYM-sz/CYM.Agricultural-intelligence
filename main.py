import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SoilMicrobiomeAnalyzer:
    """分析土壤微生物对种植的影响"""
    
    def __init__(self):
        self.microbe_types = {
            "细菌": ["固氮菌", "溶磷菌", "有益菌"],
            "真菌": ["菌根真菌", "木腐菌", "放线菌"],
            "原生动物": ["阿米巴虫", "鞭毛虫"]
        }
    
    def analyze_soil_impact(self, crop_type, soil_composition):
        """分析土壤微生物对特定作物的影响"""
        prompt = f"""
        作为农业土壤微生物专家，请分析土壤微生物对以下作物的影响：
        
        作物类型: {crop_type}
        土壤成分: {soil_composition}
        
        请提供：
        1. 该土壤中的主要微生物类型及其作用
        2. 对该作物生长的正面影响
        3. 可能存在的问题及解决方案
        4. 改善土壤微生物的建议
        """
        
        response = client.chat.completions.create(
            model="gpt-4-mini",
            messages=[
                {"role": "system", "content": "你是一位农业土壤微生物学专家"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content


class IrrigationRecommender:
    """灌溉推荐系统"""
    
    def __init__(self):
        self.crops_water_needs = {
            "小麦": 400,
            "玉米": 500,
            "水稻": 1200,
            "蔬菜": 300,
            "棉花": 600,
            "大豆": 450
        }
    
    def get_irrigation_schedule(self, crop_type, current_moisture, weather, region):
        """获取灌溉计划"""
        prompt = f"""
        作为灌溉专家，请为以下情况提供灌溉建议：
        
        作物类型: {crop_type}
        当前土壤含水量: {current_moisture}%
        天气情况: {weather}
        地区: {region}
        
        请提供：
        1. 是否需要立即灌溉
        2. 建议的灌溉时间表
        3. 每次灌溉的水量
        4. 灌溉方式建议（滴灌/喷灌/漫灌）
        5. 注意事项
        """
        
        response = client.chat.completions.create(
            model="gpt-4-mini",
            messages=[
                {"role": "system", "content": "你是一位灌溉管理专家"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content


def ask_agriculture_ai(user_input):
    """通用农业AI助手"""
    system_prompt = """
You are an intelligent agricultural assistant.
Based on user's location, land condition, and goals, you provide:
1. Suitable crops
2. Planting instructions
3. Growth cycle
4. Nutrient management
5. Harvesting guidance
6. Soil microbiome analysis
7. Irrigation recommendations
Keep answers practical and structured.
    """
    
    response = client.chat.completions.create(
        model="gpt-4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    
    return response.choices[0].message.content


def show_menu():
    """显示主菜单"""
    print("\n" + "="*50)
    print("🌱 AI农业智能助手 v2.0")
    print("="*50)
    print("1️⃣  通用农业咨询")
    print("2️⃣  土壤微生物分析")
    print("3️⃣  灌溉推荐")
    print("4️⃣  退出")
    print("="*50)


if __name__ == "__main__":
    print("🌱 AI农业助手已启动")
    
    soil_analyzer = SoilMicrobiomeAnalyzer()
    irrigation_recommender = IrrigationRecommender()
    
    while True:
        show_menu()
        choice = input("\n请选择 (1-4): ").strip()
        
        if choice == "1":
            print("\n📋 通用农业咨询")
            user_input = input("请输入您的问题: ")
            answer = ask_agriculture_ai(user_input)
            print("\n🤖 AI建议：\n", answer)
        
        elif choice == "2":
            print("\n🦠 土壤微生物分析")
            crop = input("请输入作物类型 (如: 小麦、玉米): ")
            soil = input("请描述土壤成分 (如: 黑土、红壤): ")
            analysis = soil_analyzer.analyze_soil_impact(crop, soil)
            print("\n📊 分析结果：\n", analysis)
        
        elif choice == "3":
            print("\n💧 灌溉推荐")
            crop = input("请输入作物类型: ")
            moisture = input("请输入当前土壤含水量(%): ")
            weather = input("请输入当前天气 (如: 晴朗、阴天): ")
            region = input("请输入地区: ")
            
            try:
                recommendation = irrigation_recommender.get_irrigation_schedule(
                    crop, moisture, weather, region
                )
                print("\n💧 灌溉建议：\n", recommendation)
            except ValueError:
                print("❌ 输入错误，请重新输入")
        
        elif choice == "4":
            print("👋 感谢使用，再见！")
            break
        
        else:
            print("❌ 无效的选择，请重新输入")