import telebot
from telebot import types
import sqlite3

BOT_TOKEN = '5668399105:AAFTHlM6VGpMRtavyxWo5zrq5ImlYdUYr5U'

DATABASE_PATH = 'database/database.db'
MAIN_TABLE_NAME = 'requests'

bot = telebot.TeleBot(BOT_TOKEN)
