import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_product_description(title):
    client = OpenAI(
        api_key=os.getenv("AI_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": f"Напиши короткий рекламний опис для товару: {title}. Максимум 2 речення."
        }],
        model="llama-3.3-70b-versatile",

    )
    return response.choices[0].message.content