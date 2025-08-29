from logging import Handler

from telebot import TeleBot


class TgHandler(Handler):
    def __init__(self, bot_token: str, chat_id: int):
        Handler.__init__(self)
        if isinstance(chat_id, list | tuple | set | dict):
            raise TypeError(f"A chat_id value must be an integer, not {type(chat_id)}")
        self.bot_token = bot_token
        self.chat_id = chat_id

    def emit(self, record):
        bot = TeleBot(token=self.bot_token)
        bot.send_message(chat_id=self.chat_id, text=f"мы в пизде)\n{record}")
