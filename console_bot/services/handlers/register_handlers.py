from console_bot.services.types import User

DICT_FUNC = {}


def register_message_handler(func, commands: str | list, arguments: User = None, quantity_arg: int = 0):
    if isinstance(commands, str):
        commands = [commands]

    for command in commands:
        if arguments:
            DICT_FUNC.update({command: {'function': func, "arguments": arguments, "quantity_arg": quantity_arg}})
        else:
            DICT_FUNC[command] = func

    return func
