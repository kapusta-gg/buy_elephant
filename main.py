from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    message = update.message.text
    update.message.reply_text(message)


def main():
    TOKEN = '1011660638:AAH3bzd1hwVqf9dXQsz2s1DpiDfoJQO_MgA'
    #REQUEST_KWARGS = {
    #    'proxy_url': 'socks5://127.0.0.1:9150'
    #}
    updater = Updater(TOKEN, use_context=True,)
                      #request_kwargs=REQUEST_KWARGS

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
