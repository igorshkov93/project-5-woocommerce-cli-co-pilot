# 🤖 WooCommerce CLI Co-pilot

> AI-ассистент для командной строки, который управляет вашим WooCommerce-магазином через запросы на естественном языке. Работает на Google Gemini с Function Calling.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange.svg)](https://ai.google.dev/)
[![WooCommerce](https://img.shields.io/badge/WooCommerce-REST_API_v3-purple.svg)](https://woocommerce.github.io/woocommerce-rest-api-docs/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 О проекте

**WooCommerce CLI Co-pilot** — это инструмент командной строки, который позволяет управлять интернет-магазином на WooCommerce, задавая вопросы обычным человеческим языком. Вместо того чтобы вручную копаться в админке или писать API-запросы, вы просто говорите, что нужно — а AI сам решает, какую функцию вызвать, ходит в реальный API магазина и возвращает готовый ответ.

Проект демонстрирует ключевую концепцию современной AI-автоматизации — **Function Calling**: языковая модель не «выдумывает» данные, а вызывает реальные функции и работает с настоящими данными магазина.

## ✨ Возможности

- 🗣️ **Естественный язык** — команды на русском без специального синтаксиса
- 📊 **Аналитика товаров** — топ продаж, статистика магазина
- 🔍 **Поиск аномалий** — выявление подозрительных заказов
- ✍️ **Генерация контента** — продающие SEO-описания товаров
- 🔌 **Реальный API** — прямая интеграция с WooCommerce REST API v3
- 🤖 **Function Calling** — автоматический выбор нужной функции моделью Gemini

## 🏗️ Как это работает

```
Пользователь → CLI → Gemini (Function Calling) → WooCommerce API → Ответ
                          ↓
              AI сам выбирает, какую функцию вызвать
```

1. Вы вводите запрос на естественном языке
2. Gemini анализирует его и выбирает подходящую функцию
3. Функция обращается к реальному WooCommerce API
4. Модель получает данные и форматирует понятный ответ

## 🛠️ Технологический стек

| Технология | Назначение |
|------------|-----------|
| **Python 3.10+** | Основной язык |
| **Google Gemini 2.5 Flash** | LLM с Function Calling |
| **google-genai** | Официальный SDK Gemini |
| **WooCommerce REST API v3** | Данные магазина |
| **Click** | CLI-фреймворк |
| **python-dotenv** | Управление конфигурацией |

## 🚀 Установка

```bash
# Клонировать репозиторий
git clone https://github.com/igorshkov93/woo-copilot.git
cd woo-copilot

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt
```

## ⚙️ Настройка

1. Скопируйте пример конфигурации:
   ```bash
   cp .env.example .env
   ```

2. Заполните `.env` своими данными:
   ```env
   GOOGLE_API_KEY=ваш_ключ_gemini
   WOO_STORE_URL=https://ваш-магазин.com
   WOO_CONSUMER_KEY=ck_ваш_ключ
   WOO_CONSUMER_SECRET=cs_ваш_секрет
   ```

3. Получите ключи:
   - **Gemini API:** [Google AI Studio](https://aistudio.google.com/apikey)
   - **WooCommerce:** WordPress Admin → WooCommerce → Settings → Advanced → REST API

## 💻 Использование

```bash
# Проверить конфигурацию
python main.py config

# Топ товаров
python main.py ask "покажи топ-10 товаров за неделю"

# Поиск подозрительных заказов
python main.py ask "найди подозрительные заказы"

# Статистика магазина
python main.py ask "покажи статистику магазина"

# Генерация описания
python main.py ask "напиши описание нового товара: красная футболка из хлопка, размер M"
```

### Примеры вывода

```
$ python main.py ask "покажи топ-3 товара"

Вот топ-3 товара за неделю:

1. Savvy Shoulder Tote (ID: 2732) — Цена: 24, Продажи: 2
2. Push It Messenger Bag (ID: 2739) — Цена: 45, Продажи: 1
3. Overnight Duffle (ID: 2738) — Цена: 45, Продажи: 1
```

## 📁 Структура проекта

```
woo_copilot/
├── src/
│   ├── ai/
│   │   └── function_calling.py   # Логика Gemini Function Calling
│   ├── woocommerce/
│   │   ├── client.py             # WooCommerce API клиент
│   │   └── functions.py          # Функции для AI (tools)
│   └── cli/
│       └── main.py               # CLI интерфейс (Click)
├── main.py                       # Точка входа
├── requirements.txt              # Зависимости
├── .env.example                  # Пример конфигурации
└── README.md
```

## 🧩 Архитектура Function Calling

Ключевая особенность проекта — использование нативного Function Calling от Gemini. Python-функции передаются модели напрямую, а SDK автоматически строит схему из сигнатур и docstring-ов:

```python
available_functions = [
    get_top_products,
    find_suspicious_orders,
    get_product_stats,
    generate_product_description,
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_query,
    config=types.GenerateContentConfig(tools=available_functions),
)
```

Модель сама решает, какую функцию вызвать, с какими аргументами, и как оформить финальный ответ.

## 📝 Лицензия

MIT License — используйте свободно.

## 👤 Автор

**Igor Shkov** — AI Automation Developer

- GitHub: [@igorshkov93](https://github.com/igorshkov93)

---

*Проект создан в рамках портфолио по AI-автоматизации.*
