import telebot
import re
import random
import os
import datetime
import logging
import pytz
from dotenv import load_dotenv

# ====== НАСТРОЙКИ ======
logging.basicConfig(level=logging.INFO)

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_TOKEN:
    raise ValueError("Токен не найден! Проверьте файл .env")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Новый золотой курс: 1 рубль = 5 тенге
RUB_TO_KZT_RATE = 5

# Часовой пояс Тюмени
YOUR_TZ = pytz.timezone('Asia/Yekaterinburg')

# ====== СТАРТ / ПОМОЩЬ ======
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
        "━━━━━━━━━━━━━━━━━━\n"
        "🤖  *ШУТОЧНЫЙ КАЛЬКУЛЯТОР*\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "💱  *Курс:* 1 рубль = 5 тенге\n\n"
        "📝  *Что я умею:*\n"
        "• Напиши `100 руб` — посчитаю тенге\n"
        "• Напиши `ремас` — отвечу про уши\n"
        "• Напиши `король демонов` — отвечу про сон\n"
        "• Напиши `гарп` — отвечу про него\n"
        "• Напиши `мертвый` — отвечу про непонятного\n"
        "• Напиши `миша` — отвечу про шпагиста\n\n"
        "━━━━━━━━━━━━━━━━━━",
        parse_mode='Markdown'
    )

# ====== ОБРАБОТКА СООБЩЕНИЙ ======
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    # --- РЕМАС (про уши) ---
    if 'ремас' in text:
        phrases = [
            "Это у которого уши пиздец большие? @Glebkq",
            "Это у которого уши как локаторы? @Glebkq",
            "Это у которого уши до Луны достают? @Glebkq",
            "Это у которого уши вместо крыльев? @Glebkq",
            "Это у которого уши больше головы? @Glebkq",
            "Это у которого уши как антенны? @Glebkq",
            "Это у которого уши ветром колышутся? @Glebkq",
            "Это у которого уши в двери не пролазят? @Glebkq",
            "Это у которого уши как у слона? @Glebkq",
            "Это у которого уши вместо радара? @Glebkq",
        ]
        bot.reply_to(message, random.choice(phrases))
        return

    # --- КОРОЛЬ ДЕМОНОВ ---
    if 'король демонов' in text:
        phrases = [
            "Это который спит вечно и нихуя не понимает? @vladxxtth",
            "Это который вечно спит и не вдупляет? @vladxxtth",
            "Это который спит и вообще ничего не соображает? @vladxxtth",
            "Это который вечно дрыхнет и не понимает, что происходит? @vladxxtth",
            "Это который спит и не понимает, где он вообще? @vladxxtth",
        ]
        bot.reply_to(message, random.choice(phrases))
        return

    # --- ГАРП ---
    if 'гарп' in text:
        phrases = [
            "Это смесь свиньи, обезьяны и чеченца? @jjillee",
            "Это который обезьяну трахал? @jjillee",
            "Это у которого голос как у чеченца и он обезьяну еще в жопу ебал? @jjillee",
            "Это у которого голос как у чеченца а он слону еще ухо оторвал @jjillee",
        ]
        bot.reply_to(message, random.choice(phrases))
        return

    # --- МЕРТВЫЙ ---
    if 'мертвый' in text or 'мёртвый' in text:
        phrases = [
            "Это ваще хуй пойми кто @MePTBbIU123",
            "Это вообще хуй пойми кто, даже не спрашивай @MePTBbIU123",
            "Это хуй пойми кто, но точно не человек @MePTBbIU123",
            "Это хуй пойми кто, я сам не понял @MePTBbIU123",
            "Это хуй пойми кто, но он мёртвый @MePTBbIU123",
        ]
        bot.reply_to(message, random.choice(phrases))
        return

    # --- МИША (шпагист) ---
    if 'миша' in text:
        phrases = [
            "Это который шпагист? @Mihass3",
            "Это который шпагой медведя убьёт? @Mihass3",
            "Это который шпагай хоть медведя завалит? @Mihass3",
            "Это который шпагист и этим всё сказано? @Mihass3",
            "Это который шпагой машет так, что медведь падает? @Mihass3",
            "Это который шпагист, каких поискать? @Mihass3",
            "Это который шпагой медведя насквозь проткнёт? @Mihass3",
            "Это который шпагист — медведь сам убегает? @Mihass3",
        ]
        bot.reply_to(message, random.choice(phrases))
        return

    # --- Калькулятор (если есть "руб" или "₽") ---
    if re.search(r'руб', text) or '₽' in text:
        match = re.search(r'(\d[\d\s]*[.,]?\d*)', text)
        if not match:
            bot.reply_to(message, "Напиши сумму, например: 100 руб")
            return
        amount = float(match.group(1).replace(' ', '').replace(',', '.'))
        if amount < 0:
            bot.reply_to(message, "Отрицательные суммы не принимаю 😄")
            return
        tenge = amount * RUB_TO_KZT_RATE
        rub_formatted = f"{amount:,.2f}".replace(',', ' ').replace('.', ',')
        tenge_formatted = f"{tenge:,.2f}".replace(',', ' ').replace('.', ',')

        # Текущее время по Тюмени
        now = datetime.datetime.now(YOUR_TZ).strftime("%H:%M:%S")

        # Золотые шутки
        jokes = [
            "ЗОЛОТАЯ ЕЛДА НАСТУПИЛА!",
            "Чингисхан одобряет этот курс!",
            "Тенге теперь на вес золота!",
            "Золотой запас пополнен!",
            "Курс честный, зуб даю.",
        ]
        joke = random.choice(jokes)

        # Золотое оформление
        answer = (
            "🌟✨━━━━━━━━━━━━━━━━━━✨🌟\n"
            "🏆  *ЗОЛОТАЯ ЕЛДА НАСТУПИЛА!*  🏆\n"
            "🌟✨━━━━━━━━━━━━━━━━━━✨🌟\n\n"
            "💰  *КУРС СТАЛ 1 РУБ = 5 ТЕНГЕ*  💰\n"
            "🔥  _НЕ ЗРЯ МЕНЯ ЧИНГИСХАН ПИСЮНИЛ!_  🔥\n\n"
            f"🕐  *Время сейчас:* {now}\n\n"
            f"💵  *Было:*  {rub_formatted} руб\n"
            f"🪙  *Стало:* {tenge_formatted} тенге\n\n"
            f"📊  *Курс:* 1 руб = 5 тенге\n\n"
            f"😄  _{joke}_\n"
            "🌟✨━━━━━━━━━━━━━━━━━━✨🌟"
        )

        bot.reply_to(message, answer, parse_mode='Markdown')
        return

logging.info("Бот запущен и работает...")
bot.polling(none_stop=True)
