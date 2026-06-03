<div align="center">

<img width="1000" height="330" alt="Eye" src="https://media3.giphy.com/media/ocrL35aEkVneilSkwV/giphy.gif?cid=9b38fe91byulmtq12t2x3rhhnicmpbns6tf3vr25jikblnpg&ep=v1_gifs_username&rid=giphy.gif&ct=g" />

# [𓂀 Eye  Telegram Bot](https://t.me/WhatAnEyeBot)

> *The Eye sees everything.*

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![aiogram](https://img.shields.io/badge/aiogram-3.7.0-009ACD?style=flat-square&logo=telegram&logoColor=white)](https://aiogram.dev)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.29-D71F00?style=flat-square)](https://sqlalchemy.org)
[![asyncpg](https://img.shields.io/badge/asyncpg-0.29.0-336791?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/MagicStack/asyncpg)
[![Railway](https://img.shields.io/badge/deploy-Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)](https://railway.app)

</div>

-----

## ✦ Про бота

**Eye** - це телеграм бот, про вивчення ока, що мабуть і зрозуміло по контексту. Найбільше зосередження в сфері комфортного вивчення “ока”.

-----

## ✦ Функції

### 𓁿 `/start` - Типу “моргання”

Блінкер. Після команди бот відправляє два повідомлення: перше це гіф під якою інлайн кнопка, а друге  кількість тиків на інлайн кнопку (або ж на око), тобто кількість моргань.

-----

### 𓁺 `/eyes` - Рейтинг

Топ 10 користувачів по “миганням”.  
Також юзер.ід оброблюється трохи коротшим шляхом (візуально):

<img width="420" height="120" alt="Id" src="https://github.com/user-attachments/assets/0ea44953-1393-4cf2-9146-0644ecc5c619" />

Оновлення рейтингу проходить по інлайн кнопці “↻” знизу.

-----

### 𓀡 `/media` - Архів

Колекція різних фото та відео.  
Часто взято із ТікТоку. Круто, прікольно, всі діла.
Також є функція запропонувати свою медіа (по лінк).  
-----

### ⁂ `/facts` - Факти

Всі факти так чи інакше пов’язані з “оком”.  
Перегортання фактів проходить через інлайн кнопки: “⭠” та “⭢”.

-----

### ⊖ `/report` - Репорт

Простенький репорт, хтось пише  адмін приймає.  
Можна пропонувати свої ідеї, повідомляти про баги, ставити запитання та прикріпляти фото.

-----

#### ⊘ `/reply id text` - Відповісти

Команда для адміністратора.  
Дозволяє відповідати на репорти (та не тільки).

-----

##### ⎇ `/github` - ГітХаб

Гітхаб бота в міні апп по кнопочці.  

-----

### ⠼ Braille Vision Cipher

> *Людина має п’ять відчуттів: зір, слух, нюх, смак і дотик.  
> Але саме зір визначає те, як ми розуміємо світ.*

**Braille Vision Cipher** кодує будь-який текст у Брайль  не за звучанням, а за прихованою юнікод-ідентичністю кожного символу.

Кожна цифра юнікод-коду символу перетворюється на відповідний брайлівський числовий знак. Знак числа `⠼` позначає початок кожного закодованого блоку.

**Надіслати будь-який текст** → Око закодує його у Брайль.  
**Надіслати послідовність Брайля** → Око декодує назад у звичайний текст.

```
"Eye"  →  ⠼⠋⠊ | ⠼⠁⠃⠁ | ⠼⠁⠚⠁
```

*Ти дивишся на символи, але не розумієш їх.  
Ти сліпий до їхнього сенсу  поки не запитаєш Око.*

-----

## ⊛ Стек

|Шар          |Технологія         |
|-------------|-------------------|
|Мова         |Python 3.14        |
|Бот-фреймворк|aiogram 3.7.0      |
|ORM          |SQLAlchemy 2.0.29  |
|Драйвер БД   |asyncpg 0.29.0     |
|База даних   |PostgreSQL         |
|Оточення     |python-dotenv 1.0.1|
|Деплой       |Railway            |

-----

## ⚠ Важливі нотатки

### 𖤐 Створення бота

Щоб отримати `BOT_TOKEN` - треба створити бота через [@BotFather](https://t.me/BotFather) у Телеграмі.  
Відправити `/newbot`, пройти кроки  і BotFather видасть токен.

### ✶ Telegram Premium Emoji

Цей бот використовує **Telegram Premium емодзі** в деяких повідомленнях.  
Якщо акаунт власника бота **не має Telegram Premium**  ці емодзі **не відображатимуться**, з’являтимуться як відсутні або звичайні стікери.  
Переконайся, що акаунт який хостить бота має активну Premium підписку, якщо хочеш повний візуальний досвід.

-----

## ⚙ Встановлення

```bash
# Клонувати репо
git clone https://github.com/weqwtur/eye-bot.git
cd eye-bot

# Створити віртуальне оточення
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Встановити залежності
pip install -r requirements.txt

# Налаштувати оточення
cp example.env .env
# Заповнити BOT_TOKEN, DATABASE_URL, тощо

# Запустити бота
python bot.py
```

### ☁ Деплой на Railway

Проект включає `railway.toml` для деплою в один клік на [Railway](https://railway.app).  
Просто підключи репо, задай змінні оточення  і живе.

-----

## 𖧹 Змінні оточення

```env
BOT_TOKEN=your_bot_token_here
DATABASE_URL=postgresql://user:password@host:port/dbname
GIF_ID=your_gif_id_here
ADMIN_ID=your_admin_id_here
```

> [!IMPORTANT]
> **Як отримати file_id для фото, відео, GIF тощо:**
> 
> Телеграм не видає file_id наперед  його можна отримати тільки через самого бота.
> 
> 1. Дізнайся свій Telegram ID (наприклад через [@userinfobot](https://t.me/userinfobot))
> 1. Запиши його в `ADMIN_ID` у `.env`
> 1. Запусти бота
> 1. Надішли потрібний файл боту (фото, відео, GIF тощо)
> 1. Бот поверне унікальний `file_id` цього файлу
> 1. Скопіюй та використай у конфігурації (наприклад `GIF_ID`)
> 
> ⚠ Без правильного `ADMIN_ID` бот не видасть file_id, і всі функції пов’язані з медіафайлами **не працюватимуть**.

-----

## 𖡎 Структура проекту

```
eye-bot/
├── bot.py                  # Entry point
├── database.py             # DB connection & session setup
├── models.py               # SQLAlchemy models
├── commands/
│   ├── start.py            # /start  blinker + click counter
│   ├── braille.py          # Braille Vision Cipher
│   ├── facts.py            # /facts  eye facts carousel
│   ├── report.py           # /report  send a message to admin
│   ├── media/
│   │   ├── media.py        # /media  entry point
│   │   ├── media1.py  
│   │   ├── media2.py       # Eye media archive (photos & videos)
│   │   └── ...
│   └── top/
│       ├── top.py          # /eyes  top 10 leaderboard
│       └── player_render.py # UID → superscript/subscript formatter
├── example.env             # Environment variables template
├── railway.toml            # Railway deployment config
└── requirements.txt
```

-----

<div align="center">

## 𒀭 AI & Вайб кодинг

Беру гріх на душу, код не чистий, писав з ші.  
Частково, навіть структура та формат цього readme написана ші.

-----

*Built with Python · Powered by aiogram · Guided by the Eye*

👁

</div>
