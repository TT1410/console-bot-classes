from console_bot.services.decorators import input_error
from console_bot.services.types import User, ADDRESS_BOOK, Record, Phone


def hello() -> str:
    """
    Отвечает в консоль "How can I help you?"
    :return:
    """
    return "How can I help you?"


@input_error
def add_user(user: User) -> None:
    """
    По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
    Пользователь вводит команду add, имя и номер телефона, обязательно через пробел.
    :param user:
    :return:
    """
    if ADDRESS_BOOK.get(user.name):
        raise ValueError(f"Contact with the name {user.name} already exists. "
                         f"To add a new number to an existing contact, use the <change> command.")

    ADDRESS_BOOK.add_record(Record(**user.__dict__))


@input_error
def change_user(user: User) -> None:
    """
    По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
    Пользователь вводит команду change, имя и номер телефона, обязательно через пробел.
    :param user:
    :return:
    """
    if not ADDRESS_BOOK.get(user.name):
        raise KeyError(user.name)

    ADDRESS_BOOK[user.name].add_phone(user.phone)


@input_error
def user_phone(user: User) -> str:
    """
    По этой команде бот выводит в консоль номер телефона для указанного контакта.
    Пользователь вводит команду phone и имя контакта, чей номер нужно показать, обязательно через пробел.
    :param user:
    :return:
    """
    return ', '.join([str(x.value) for x in ADDRESS_BOOK[user.name].phones])


def show_all_users() -> str:
    """
    По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
    :return:
    """
    format_users = []

    for user in ADDRESS_BOOK.values():
        phones = ', '.join([str(x.value) for x in user.phones])
        format_users.append(f"{user.name.value:<10}: {phones}")

    return '\n'.join(format_users)


def close_bot() -> None:
    """
    По любой из команд: "good bye", "close", "exit",
    бот завершает свою роботу после того, как выведет в консоль "Good bye!".
    :return:
    """
    return "Good bye!"
