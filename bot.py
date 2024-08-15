import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import spacy

# Load Spacy NLP model
nlp = spacy.load("en_core_web_sm")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I'm your Wellness Bot. How can I help you today?",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("You can ask me for wellness tips, exercise advice, or diet suggestions!")

async def wellness_response(update: Update, context: CallbackContext):
    user_input = update.message.text
    doc = nlp(user_input)

    if "stress" in user_input.lower():
        response = "It sounds like you're feeling stressed. I recommend taking deep breaths and maybe a short walk."
    elif "energy" in user_input.lower():
        response = "For a boost of energy, try drinking water and eating a snack with protein and carbs!"
    elif "diet" in user_input.lower():
        response = "A balanced diet with fruits, vegetables, and lean proteins can help you stay healthy."
    else:
        response = "I can help with stress, energy, or diet. Let me know if you have questions on these topics!"

    await update.message.reply_text(response)

def main():
    application = Application.builder().token("7168442396:AAEyMOGGq8568GwauU8rhpoSVNe1SLRnOdo").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, wellness_response))

    application.run_polling()

if __name__ == '__main__':
    main()
