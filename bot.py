import telebot
import re
import random

# Твой токен
TOKEN = '8857992697:AAHTUwGbJnPcqZrI1okAfM-_RYkhnGACtmk'
bot = telebot.TeleBot(TOKEN)

# Наш шуточный курс: 3 рубля = 1 000 000 тенге
RUB_TO_KZT_RATE = 1000000 / 3

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
        "Привет! Я шуточный калькулятор.\n"
        "Курс: 3 рубля = 1 000 000 тенге.\n"
        "Напиши сумму в рублях, например: 100 руб"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    # Если написали "ремас" — отвечаем про уши и тегаем @Glebkq
    if 'ремас' in text:
        bot.reply_to(message, "Это у которого уши пиздец большие? @Glebkq")
        return
    
    # Если написали "король демонов" — отвечаем про вечный сон и тегаем @vladxxtth
    if 'король демонов' in text:
        bot.reply_to(message, "Это который спит вечно? @vladxxtth")
        return
    
    # Если написали "гарп" — отвечаем про чеченца и тегаем @jjillee
    if 'гарп' in text:
        bot.reply_to(message, "Это который чеченец? @jjillee")
        return
    
    # Если написали "мертвый" — отвечаем и тегаем @MePTBbIU123
    if 'мертвый' in text or 'мёртвый' in text:
        bot.reply_to(message, "Это ваще хуй пойми кто @MePTBbIU123")
        return
    
    # Проверяем, есть ли в сообщении слово "руб" или знак "₽"
    if not (re.search(r'руб', text) or '₽' in text):
        return  # Если нет — бот молчит
    
    # Ищем число
    match = re.search(r'(\d+[.,]?\d*)', text)
    if not match:
        bot.reply_to(message, "Напиши сумму, например: 100 руб")
        return
    
    amount = float(match.group(1).replace(',', '.'))
    tenge = amount * RUB_TO_KZT_RATE
    
    # Форматируем с копейками (2 знака после запятой)
    rub_formatted = f"{amount:,.2f}".replace(',', ' ').replace('.', ',')
    tenge_formatted = f"{tenge:,.2f}".replace(',', ' ').replace('.', ',')
    
    jokes = [
        "Это целое состояние!",
        "Хватит на пожизненный запас чая.",
        "Можно купить половину Казахстана.",
        "Курс честный, зуб даю.",
        "Тенге сегодня в ударе.",
    ]
    joke = random.choice(jokes)
    
    bot.reply_to(message,
        f"💰 {rub_formatted} руб ≈ {tenge_formatted} тенге\n"
        f"📈 Курс: 3 руб = 1 000 000 тенге\n"
        f"😄 {joke}"
    )

print("Бот запущен и работает...")
bot.polling(none_stop=True)
