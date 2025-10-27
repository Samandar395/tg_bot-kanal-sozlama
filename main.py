import telebot

# 🔑 BOT TOKENINGNI BU YERGA QO'Y (BotFather'dan olgan token)
BOT_TOKEN = "7379852050:AAGfXE3KtRsvBUpwlnvzbCTcPknYhIdE1_w"

# 📢 KANAL USERNAME (kanaling ochiq bo‘lishi shart va @ bilan boshlansin)
CHANNEL_ID = "@dls_yangiliklari_n","@kotta_bolacha"

bot = telebot.TeleBot(BOT_TOKEN)

# /start buyrug'i
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    try:
        # foydalanuvchini kanalga obuna bo‘lganligini tekshirish
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            bot.send_message(
                message.chat.id,
                "✅ Siz kanalga obuna bo‘lgansiz!\nEndi botdan foydalanishingiz mumkin."
            )
        else:
            send_subscribe_message(message)
    except:
        send_subscribe_message(message)

# Kanalga obuna bo‘lish tugmasi va tekshirish
def send_subscribe_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # 📢 Kanalga o‘tish havolasi
    btn = telebot.types.InlineKeyboardButton(
        "📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID[1:]}")
    # ✅ Obuna bo‘ldim tugmasi
    check = telebot.types.InlineKeyboardButton(
        "✅ Obuna bo‘ldim", callback_data="check")
    markup.add(btn)
    markup.add(check)
    bot.send_message(
        message.chat.id,
        "❗️Avval kanalga obuna bo‘ling, keyin “✅ Obuna bo‘ldim” tugmasini bosing:",
        reply_markup=markup
    )

# ✅ Obuna bo‘ldim tugmasini bosganda ishlaydi
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_subscription(call):
    user_id = call.from_user.id
    member = bot.get_chat_member(CHANNEL_ID, user_id)
    if member.status in ['member', 'administrator', 'creator']:
        bot.send_message(
            call.message.chat.id,
            "🎉 Rahmat! Endi botdan foydalanishingiz mumkin."
        )
    else:
        bot.answer_callback_query(
            call.id,
            "❗️Hali obuna bo‘lmagansiz!",
            show_alert=True
        )

print("✅ Bot ishga tushdi...")
bot.infinity_polling()
