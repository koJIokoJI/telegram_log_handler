import logging

from tg_handler import TgHandler

logger = logging.getLogger(__name__)

tg_handler = TgHandler(bot_token="bot_token", chat_id=1234567890)
tg_handler.setLevel(logging.ERROR)

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s",
    handlers=[logging.StreamHandler(), tg_handler],
)
