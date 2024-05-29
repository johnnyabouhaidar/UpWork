import logging
from telegram import Bot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def send_notification(bot_token, chat_id, message):
    """Send a notification to a Telegram chat."""
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

def main():
    """Main function to send notifications."""
    # Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
    bot_token = '7115985794:AAGFTZL0xV8SNg0n7EA7vOQQg7FDSXw1UVo'
    # Replace 'YOUR_CHAT_ID' with the ID of the chat or user you want to send notifications to
    chat_id = 'unknown777123'
    message = 'This is an automated notification from your Python script.'

    send_notification(bot_token, chat_id, message)

if __name__ == '__main__':
    main()