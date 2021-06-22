import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import covidCommands
import logging

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, ctx):
    ctx.bot.send_message(chat_id=update.effective_chat.id, text="I'm Eirin. Nice to meet you.")


def unknown(update, ctx):
    ctx.bot.send_message(chat_id=update.effective_chat.id, text="Sorry. That is not a valid command")


def daily_infections(update, ctx):
    ctx.bot.send_message(chat_id=update.effective_chat.id, text=covidCommands.daily_infections(), parse_mode='HTML')


def vaccinations_update(update, ctx):
    ctx.bot.send_message(chat_id=update.effective_chat.id, text=covidCommands.vaccinations_update())


def cluster_update(update, ctx):
    ctx.bot.send_message(chat_id=update.effective_chat.id, text=covidCommands.cluster_update(), parse_mode='HTML')


def main():
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('daily', daily_infections))
    dispatcher.add_handler(CommandHandler(['vaccination', 'vaccinations', 'vac'], vaccinations_update))
    dispatcher.add_handler(CommandHandler(['clusters', 'cluster'], cluster_update))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()


if __name__ == '__main__':
    main()


