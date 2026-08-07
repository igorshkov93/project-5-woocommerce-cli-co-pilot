# 🤖 WooCommerce CLI Co-pilot

> AI co-pilot for the command line that manages your WooCommerce store through natural-language queries. Powered by Google Gemini with Function Calling.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange.svg)](https://ai.google.dev/)
[![WooCommerce](https://img.shields.io/badge/WooCommerce-REST_API_v3-purple.svg)](https://woocommerce.github.io/woocommerce-rest-api-docs/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**🌐 Language:** **English** · [Русский](#-русский) · [Українська](#-українська)

---

## 📖 About

**WooCommerce CLI Co-pilot** is a command-line tool that lets you manage a WooCommerce store by asking questions in plain human language. Instead of digging through the admin panel or writing API requests by hand, you just say what you need — and the AI decides which function to call, hits the real store API, and returns a ready-to-use answer.

The project demonstrates a core concept of modern AI automation — **Function Calling**: the language model doesn't "make up" data, it calls real functions and works with actual store data.

## ✨ Features

- 🗣️ **Natural language** — commands without any special syntax
- 📊 **Product analytics** — top sales, store statistics
- 🔍 **Anomaly detection** — flagging suspicious orders
- ✍️ **Content generation** — selling SEO product descriptions
- 🔌 **Real API** — direct WooCommerce REST API v3 integration
- 🤖 **Function Calling** — Gemini automatically picks the right function

## 🏗️ How it works

```
User → CLI → Gemini (Function Calling) → WooCommerce API → Answer
                     ↓
         AI decides which function to call
```

1. You enter a request in natural language
2. Gemini analyzes it and picks the right function
3. The function calls the real WooCommerce API
4. The model receives the data and formats a clear answer

## 🛠️ Tech stack

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core language |
| **Google Gemini 2.5 Flash** | LLM with Function Calling |
| **google-genai** | Official Gemini SDK |
| **WooCommerce REST API v3** | Store data |
| **Click** | CLI framework |
| **python-dotenv** | Configuration management |

## 🚀 Installation

```bash
git clone https://github.com/igorshkov93/project-5-woocommerce-cli-co-pilot.git
cd project-5-woocommerce-cli-co-pilot

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## ⚙️ Configuration

1. Copy the config example:
   ```bash
   cp .env.example .env
   ```

2. Fill in `.env` with your data:
   ```env
   GOOGLE_API_KEY=your_gemini_key
   WOO_STORE_URL=https://your-store.com
   WOO_CONSUMER_KEY=ck_your_key
   WOO_CONSUMER_SECRET=cs_your_secret
   ```

3. Get your keys:
   - **Gemini API:** [Google AI Studio](https://aistudio.google.com/apikey)
   - **WooCommerce:** WordPress Admin → WooCommerce → Settings → Advanced → REST API

## 💻 Usage

```bash
# Check configuration
python main.py config

# Top products
python main.py ask "show top-10 products for the week"

# Find suspicious orders
python main.py ask "find suspicious orders"

# Store statistics
python main.py ask "show store statistics"

# Generate a description
python main.py ask "write a description for a new product: red cotton t-shirt, size M"
```

### Sample output

```
$ python main.py ask "show top-3 products"

Here are the top-3 products for the week:

1. Savvy Shoulder Tote (ID: 2732) — Price: 24, Sales: 2
2. Push It Messenger Bag (ID: 2739) — Price: 45, Sales: 1
3. Overnight Duffle (ID: 2738) — Price: 45, Sales: 1
```

## 📁 Project structure

```
woo_copilot/
├── src/
│   ├── ai/
│   │   └── function_calling.py   # Gemini Function Calling logic
│   ├── woocommerce/
│   │   ├── client.py             # WooCommerce API client
│   │   └── functions.py          # Functions for the AI (tools)
│   └── cli/
│       └── main.py               # CLI interface (Click)
├── main.py                       # Entry point
├── requirements.txt              # Dependencies
├── .env.example                  # Config example
└── README.md
```

## 🧩 Function Calling architecture

The key feature of the project is Gemini's native Function Calling. Python functions are passed to the model directly, and the SDK automatically builds the schema from signatures and docstrings:

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

The model decides which function to call, with which arguments, and how to format the final answer.

## 📝 License

MIT License — use freely.

## 👤 Author

**Igor Gorshkov** — moving toward AI Automation Expert.

Former Crocoblock support agent (JetEngine, JetFormBuilder, JetSmartFilters and other WordPress/WooCommerce plugins), now transitioning into AI automation and building a portfolio of practical AI-agent and automation projects.

- GitHub: [@igorshkov93](https://github.com/igorshkov93)

---

# 🇷🇺 Русский

> AI-ассистент для командной строки, который управляет вашим WooCommerce-магазином через запросы на естественном языке. Работает на Google Gemini с Function Calling.

**🌐 Язык:** [English](#-woocommerce-cli-co-pilot) · **Русский** · [Українська](#-українська)

## 📖 О проекте

**WooCommerce CLI Co-pilot** — это инструмент командной строки, который позволяет управлять интернет-магазином на WooCommerce, задавая вопросы обычным человеческим языком. Вместо того чтобы вручную копаться в админке или писать API-запросы, вы просто говорите, что нужно — а AI сам решает, какую функцию вызвать, ходит в реальный API магазина и возвращает готовый ответ.

Проект демонстрирует ключевую концепцию современной AI-автоматизации — **Function Calling**: языковая модель не «выдумывает» данные, а вызывает реальные функции и работает с настоящими данными магазина.

## ✨ Возможности

- 🗣️ **Естественный язык** — команды без специального синтаксиса
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
git clone https://github.com/igorshkov93/project-5-woocommerce-cli-co-pilot.git
cd project-5-woocommerce-cli-co-pilot

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

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

### Пример вывода

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

**Игорь Горшков** — двигаюсь в сторону AI Automation Expert.

В прошлом — агент службы поддержки Crocoblock (JetEngine, JetFormBuilder, JetSmartFilters и другие плагины для WordPress/WooCommerce), сейчас перехожу в сферу AI-автоматизации и собираю портфолио из практических проектов с AI-агентами и автоматизацией.

- GitHub: [@igorshkov93](https://github.com/igorshkov93)

---

# 🇺🇦 Українська

> AI-асистент для командного рядка, який керує вашим WooCommerce-магазином за допомогою запитів природною мовою. Працює на Google Gemini з Function Calling.

**🌐 Мова:** [English](#-woocommerce-cli-co-pilot) · [Русский](#-русский) · **Українська**

## 📖 Про проєкт

**WooCommerce CLI Co-pilot** — це інструмент командного рядка, який дозволяє керувати інтернет-магазином на WooCommerce, ставлячи запитання звичайною людською мовою. Замість того щоб вручну копирсатися в адмінці чи писати API-запити, ви просто кажете, що потрібно — а AI сам вирішує, яку функцію викликати, звертається до реального API магазину й повертає готову відповідь.

Проєкт демонструє ключову концепцію сучасної AI-автоматизації — **Function Calling**: мовна модель не «вигадує» дані, а викликає реальні функції та працює зі справжніми даними магазину.

## ✨ Можливості

- 🗣️ **Природна мова** — команди без спеціального синтаксису
- 📊 **Аналітика товарів** — топ продажів, статистика магазину
- 🔍 **Пошук аномалій** — виявлення підозрілих замовлень
- ✍️ **Генерація контенту** — продавальні SEO-описи товарів
- 🔌 **Реальний API** — пряма інтеграція з WooCommerce REST API v3
- 🤖 **Function Calling** — автоматичний вибір потрібної функції моделлю Gemini

## 🏗️ Як це працює

```
Користувач → CLI → Gemini (Function Calling) → WooCommerce API → Відповідь
                        ↓
            AI сам обирає, яку функцію викликати
```

1. Ви вводите запит природною мовою
2. Gemini аналізує його й обирає відповідну функцію
3. Функція звертається до реального WooCommerce API
4. Модель отримує дані та форматує зрозумілу відповідь

## 🛠️ Технологічний стек

| Технологія | Призначення |
|------------|-------------|
| **Python 3.10+** | Основна мова |
| **Google Gemini 2.5 Flash** | LLM з Function Calling |
| **google-genai** | Офіційний SDK Gemini |
| **WooCommerce REST API v3** | Дані магазину |
| **Click** | CLI-фреймворк |
| **python-dotenv** | Керування конфігурацією |

## 🚀 Встановлення

```bash
git clone https://github.com/igorshkov93/project-5-woocommerce-cli-co-pilot.git
cd project-5-woocommerce-cli-co-pilot

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## ⚙️ Налаштування

1. Скопіюйте приклад конфігурації:
   ```bash
   cp .env.example .env
   ```

2. Заповніть `.env` своїми даними:
   ```env
   GOOGLE_API_KEY=ваш_ключ_gemini
   WOO_STORE_URL=https://ваш-магазин.com
   WOO_CONSUMER_KEY=ck_ваш_ключ
   WOO_CONSUMER_SECRET=cs_ваш_секрет
   ```

3. Отримайте ключі:
   - **Gemini API:** [Google AI Studio](https://aistudio.google.com/apikey)
   - **WooCommerce:** WordPress Admin → WooCommerce → Settings → Advanced → REST API

## 💻 Використання

```bash
# Перевірити конфігурацію
python main.py config

# Топ товарів
python main.py ask "покажи топ-10 товарів за тиждень"

# Пошук підозрілих замовлень
python main.py ask "знайди підозрілі замовлення"

# Статистика магазину
python main.py ask "покажи статистику магазину"

# Генерація опису
python main.py ask "напиши опис нового товару: червона футболка з бавовни, розмір M"
```

### Приклад виводу

```
$ python main.py ask "покажи топ-3 товари"

Ось топ-3 товари за тиждень:

1. Savvy Shoulder Tote (ID: 2732) — Ціна: 24, Продажі: 2
2. Push It Messenger Bag (ID: 2739) — Ціна: 45, Продажі: 1
3. Overnight Duffle (ID: 2738) — Ціна: 45, Продажі: 1
```

## 📁 Структура проєкту

```
woo_copilot/
├── src/
│   ├── ai/
│   │   └── function_calling.py   # Логіка Gemini Function Calling
│   ├── woocommerce/
│   │   ├── client.py             # WooCommerce API клієнт
│   │   └── functions.py          # Функції для AI (tools)
│   └── cli/
│       └── main.py               # CLI інтерфейс (Click)
├── main.py                       # Точка входу
├── requirements.txt              # Залежності
├── .env.example                  # Приклад конфігурації
└── README.md
```

## 🧩 Архітектура Function Calling

Ключова особливість проєкту — використання нативного Function Calling від Gemini. Python-функції передаються моделі напряму, а SDK автоматично будує схему із сигнатур і docstring-ів:

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

Модель сама вирішує, яку функцію викликати, з якими аргументами, і як оформити фінальну відповідь.

## 📝 Ліцензія

MIT License — використовуйте вільно.

## 👤 Автор

**Ігор Горшков** — рухаюся в бік AI Automation Expert.

У минулому — агент служби підтримки Crocoblock (JetEngine, JetFormBuilder, JetSmartFilters та інші плагіни для WordPress/WooCommerce), зараз переходжу у сферу AI-автоматизації та збираю портфоліо з практичних проєктів з AI-агентами й автоматизацією.

- GitHub: [@igorshkov93](https://github.com/igorshkov93)

---

*Portfolio project on AI automation · Проект для портфолио по AI-автоматизации · Проєкт для портфоліо з AI-автоматизації*
