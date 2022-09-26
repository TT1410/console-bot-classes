from console_bot.services.types import User
from .input_parser import text_parsing
from .register_handlers import register_message_handler
from .handlers import hello, add_user, change_user, user_phone, show_all_users, close_bot


__all__ = [
    "text_parsing"
]


register_message_handler(hello, 'hello')
register_message_handler(add_user, 'add', User, 2)
register_message_handler(change_user, 'change', User, 2)
register_message_handler(user_phone, 'phone', User, 1)
register_message_handler(show_all_users, 'show all')
register_message_handler(close_bot, ["good bye", "close", "exit"])
