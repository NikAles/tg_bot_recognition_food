# Telegram Bot - Food Recognition & Nutrition Analysis

Телеграм-бот, который определяет, есть ли на фото еда, и предоставляет информацию о блюде: название, калорийность и БЖУ (белки, жиры, углеводы) на 100 грамм.
Бот использует **Google Gemini AI** для анализа изображений.

---

## Основные возможности

* Принимает фото через Telegram.
* Определяет, есть ли еда на изображении.
* Если еда найдена:

  * Показывает название блюда.
  * Выводит средние значения **КБЖУ**.
* Работает через прокси (поддержка указания прокси-сервера).

---

## Архитектура проекта

```
.
├── bot.py                 # Точка входа, запуск бота
├── loader.py              # Инициализация бота и диспетчера
├── app/
│   ├── handlers.py        # Обработчики команд и фото
│   ├── googlemodel.py     # Класс для взаимодействия с Google Gemini AI
│   ├── api_key_google.txt # API ключ для Google Gemini
│   └── proxy.txt          # Настройки прокси
└── bot_tg/
    └── tg_bot_recognition_food/
        └── api_key.txt    # API ключ для Telegram бота
```

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/NikAles/tg_bot_recognition_food.git
cd tg_bot_recognition_food
```

### 2. Создайте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Настройте ключи и прокси

* **Telegram API Key:**

  * Создайте бота через [@BotFather](https://t.me/BotFather).
  * Поместите токен в файл:

    ```
    bot_tg/tg_bot_recognition_food/api_key.txt
    ```

* **Google Gemini API Key:**

  * Получите ключ на [Google AI Studio](https://aistudio.google.com/).
  * Добавьте ключ в файл:

    ```
    app/api_key_google.txt
    ```

* **Proxy (Если вы находитесь в России):**

  * Укажите данные прокси в файле:

    ```
    app/proxy.txt
    ```
  * Формат: `login:password@host:port`

### 5. Запуск бота

```bash
python bot.py
```

---

## Пример работы

**Вход:**

* Пользователь отправляет фото блюда в Telegram.

**Выход:**

![Выход](bot_tg\tg_bot_recognition_food\answer.PNG)

Бот также вернёт изображение с этим текстом в подписи.

---

## Используемые технологии

* [Python 3.11+](https://www.python.org/)
* [Aiogram](https://docs.aiogram.dev/) - Telegram Bot API.
* [Google Gemini AI](https://ai.google.dev/) - анализ изображений и генерация текста.
* [Asyncio](https://docs.python.org/3/library/asyncio.html) - асинхронность.
