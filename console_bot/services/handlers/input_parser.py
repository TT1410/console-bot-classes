from console_bot.services.decorators import input_error
from console_bot.services.types import User
from .register_handlers import DICT_FUNC


def search_arguments(text: str):
    data = DICT_FUNC.get(text.lower())

    if data:
        return data, None
    
    command, *args = text.split(maxsplit=1)
    args = args[0] if args else None

    data = DICT_FUNC.get(command.lower())

    if not data:
        raise ValueError(f"Sorry, but there is no '{command}' command")

    return data, args


@input_error
def text_parsing(text: str) -> tuple:
    data, args = search_arguments(text)

    if not isinstance(data, dict):
        return data, None

    if not args:
        if data['quantity_arg'] == 1:
            raise ValueError("Enter user name")
        raise ValueError("Give me name and phone please")

    args = args.rsplit(maxsplit=1)

    args = args + [''] if (len(args) < 2) and (len(args) == data['quantity_arg']) else args

    user: User = data['arguments']

    try:
        _args = user(*args)
    except TypeError:
        raise ValueError("Please tell me your name and phone number, separated by a space")

    return data['function'], _args
    