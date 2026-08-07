import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from src.woocommerce.functions import get_top_products, find_suspicious_orders, get_product_stats, generate_product_description


load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# Список Python-функций, которые Gemini может вызывать.
# SDK сам построит схему из сигнатур и docstring-ов.
available_functions = [get_top_products, find_suspicious_orders, get_product_stats, generate_product_description]


def process_with_function_calling(user_query: str) -> str:
    """Обрабатывает запрос пользователя через Gemini с Function Calling."""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Ты AI-ассистент для WooCommerce магазина. "
                     f"Используй доступные функции, чтобы получить реальные данные "
                     f"и понятно ответь пользователю на русском.\n\n"
                     f"ВАЖНО: Если пользователь просит написать описание товара, "
                     f"вызови функцию generate_product_description для структурирования, "
                     f"а ЗАТЕМ обязательно сам напиши полноценное продающее SEO-описание "
                     f"(2-3 абзаца) на основе полученных данных: заголовок, преимущества, "
                     f"характеристики, призыв к действию.\n\nЗапрос: {user_query}",
            config=types.GenerateContentConfig(
                tools=available_functions,
            ),
        )
        return response.text
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Ошибка: {str(e)}"