from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start_handler(update, context):
    update.message.reply_text(
        'I am removing voice messages in group chats! Just add me to chat as admin and give me permissions to remove '
        'messages.')


def voice_handler(update, context):
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)


TOKEN = "1098876314:AAGqN-rBZLkO6ZoDnNzOuFMq33_1PtAjyCU"

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.voice, voice_handler))
dispatcher.add_handler(CommandHandler("start", start_handler))


updater.start_polling()
updater.idle()

