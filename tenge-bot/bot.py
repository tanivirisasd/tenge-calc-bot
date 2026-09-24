import telebot
import re
import random
import os
import datetime

# ====== НАСТРОЙКИ ======
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8857992697:AAHTUwGbJnPcqZrI1okAfM-_RYkhnGACtmk')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Шуточный курс: 3 рубля = 1 000 000 тенге
RUB_TO_KZT_RATE = 1000000 / 3

# ====== СТАРТ / ПОМОЩЬ ======
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
        "━━━━━━━━━━━━━━━━━━\n"
        "🤖  *ШУТОЧНЫЙ КАЛЬКУЛЯТОР*\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "💱  *Курс:* 3 рубля = 1 000 000 тенге\n\n"
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
        match = re.search(r'(\d+[.,]?\d*)', text)
        if not match:
            bot.reply_to(message, "Напиши сумму, например: 100 руб")
            return
        amount = float(match.group(1).replace(',', '.'))
        tenge = amount * RUB_TO_KZT_RATE
        rub_formatted = f"{amount:,.2f}".replace(',', ' ').replace('.', ',')
        tenge_formatted = f"{tenge:,.2f}".replace(',', ' ').replace('.', ',')

        # Текущее время
        now = datetime.datetime.now().strftime("%H:%M:%S")

        jokes = [
            "Это целое состояние!",
            "Хватит на пожизненный запас чая.",
            "Можно купить половину Казахстана.",
            "Курс честный, зуб даю.",
            "Тенге сегодня в ударе.",
        ]
        joke = random.choice(jokes)

        answer = (
            "━━━━━━━━━━━━━━━━━━\n"
            "💱  *КОНВЕРТАЦИЯ ВАЛЮТ*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🕐  *Время сейчас:* {now}\n\n"
            f"💵  *Было:*  {rub_formatted} руб\n"
            f"💰  *Стало:* {tenge_formatted} тенге\n\n"
            f"📊  *Курс:* 3 руб = 1 000 000 тенге\n\n"
            f"😄  _{joke}_\n"
            f"⚡  _А во время золотой эры курс был вообще другой!_\n"
            "━━━━━━━━━━━━━━━━━━"
        )

        bot.reply_to(message, answer, parse_mode='Markdown')
        return

print("Бот запущен и работает...")
bot.polling(none_stop=True)
