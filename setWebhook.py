import telegram
import os



TOKEN = os.environ.get('TOKEN')
WEBHOOK = 'https://pardayevsamandar.pythonanywhere.com/api'
bot  = telegram.Bot(token=TOKEN)

info = bot.get_webhook_info

bot.deleteWebhook()

bot.setWebhook(WEBHOOK)

print(info)