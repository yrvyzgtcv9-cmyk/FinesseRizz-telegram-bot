from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8519112526:AAHepLk-2OR2OFuDAORlQyL9JP888RISlYk"

async def start(update, context):
    keyboard = [[InlineKeyboardButton("PRÊTE !", callback_data="prete")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(
        photo="https://i.pinimg.com/736x/2f/c4/5a/2fc45ab7090b279c996bea09afe3e6e4.jpg",
        caption="Saint-Valentin\nÇa Te Dis ? 💕\n\nOu préfères-tu que je te dise ?",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button(update, context):
    query = update.callback_query
    try:
        await query.answer()  # Essaie de répondre
    except:
        pass  # Ignore "query too old"
    
    choice = query.data
    responses = {
        "prete": "💘 Choisis ton date timide dev web !",
        "cosy": "💻 *Cosy Coding* : Netflix & code 🌙 Parfait pour nous !",
        "balade": "🌅 *Balade Romantique* : Vieux-Port Marseille GPS 43.29695, 5.38107",
        "diner": "🍷 *Dîner Port* : MuCEM vue calanques ❤️ Réserve ?"
    }
    text = responses.get(choice, "Choix reçu !")
    keyboard = [] if choice in ["cosy", "balade", "diner"] else [  # Cache boutons après choix
        [InlineKeyboardButton("💕 Date Cosy Coding", callback_data="cosy")],
        [InlineKeyboardButton("🌅 Balade Marseille", callback_data="balade")],
        [InlineKeyboardButton("🍷 Dîner Port", callback_data="diner")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
