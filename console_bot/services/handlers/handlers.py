from console_bot.services.decorators import input_error
from console_bot.services.types import Command, ADDRESS_BOOK, Record, Phone


def hello() -> str:
    """
    Отвечает в консоль "How can I help you?"
    :return:
    """
    return "How can I help you?"


@input_error
def add_user(command: Command) -> str:
    """
    По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
    Пользователь вводит команду add, имя и номер телефона, обязательно через пробел.
    :param command:
    :return:
    """
    if ADDRESS_BOOK.get(command.username):
        raise ValueError(f"Contact with the name {command.username} already exists. "
                         f"To add a new number to an existing contact, use the <change> command.")

    ADDRESS_BOOK.add_record(Record(command.username, command.value))

    return f"Successfully created a new contact '{command.username}'"


@input_error
def add_phone(command: Command) -> str:
    """
    По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
    Пользователь вводит команду change, имя и номер телефона, обязательно через пробел.
    :param command:
    :return:
    """
    if not ADDRESS_BOOK.get(command.username):
        raise KeyError(command.username)

    phone = ADDRESS_BOOK[command.username].add_phone(command.value)

    return f"Contact phone number {command.username} '{phone.value}' successfully added"


@input_error
def change_phone(command: Command) -> str:
    """
    По этой команде бот заменяет старый номер телефона новым для существующего контакта.
    Пользователь вводит команду change-phone, имя и новый номер телефона, обязательно через пробел.
    Далее пользователю будет предложено выбрать из списка номер, который необходимо заменить новым.
    :param command:
    :return:
    """
    if not ADDRESS_BOOK.get(command.username):
        raise KeyError(command.username)

    print(user_phone(command))

    while True:
        try:
            index = int(input("Enter the index number of the phone from the list you want to replace\n"
                              "enter 0 to cancel: "))
        except TypeError:
            continue
        else:
            break

    if not index:
        return

    old_phone, new_phone = ADDRESS_BOOK[command.username].replace_phone(index, command.value)

    return f"Contact phone number {command.username} '{old_phone.value}' " \
           f"has been successfully replaced by '{new_phone.value}'"


@input_error
def remove_phone(command: Command) -> str:
    """
    По этой команде бот удаляет номер телефона существующего контакта.
    Пользователь вводит команду change, имя и номер телефона, который необходимо удалить обязательно через пробел.
    Пользователь может не вводить номер телефона, тогда ему будет предложено выбрать номер из списка.
    :param command:
    :return:
    """
    if not ADDRESS_BOOK.get(command.username):
        raise KeyError(command.username)

    index = None

    if command.value:
        try:
            _phone = str(int(command.value))

            for num, phone in enumerate(ADDRESS_BOOK[command.username].phones, 1):
                if _phone in str(phone.value):
                    index = num
                    break

        except TypeError:
            pass

    while not index:
        print(user_phone(command))

        try:
            index = int(input("Enter the index number of the phone from the list you want to replace: "))
        except TypeError:
            continue
        else:
            break

    if index == 0:
        return

    old_phone = ADDRESS_BOOK[command.username].remove_phone(1)

    return f"Contact phone number {command.username} '{old_phone.value}' deleted successfully"


@input_error
def user_phone(command: Command) -> str:
    """
    По этой команде бот выводит в консоль номера телефонов для указанного контакта.
    Пользователь вводит команду phone и имя контакта, чьи номера нужно показать, обязательно через пробел.
    :param command:
    :return:
    """
    return (f"Phone numbers of {command.username}\n\t" +
            "\n\t".join([f"{num}. {x.value}" for num, x in enumerate(ADDRESS_BOOK[command.username].phones, 1)]))


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


def help_command() -> str:
    return


def close_bot() -> str:
    """
    По любой из команд: "good bye", "close", "exit",
    бот завершает свою роботу после того, как выведет в консоль "Good bye!".
    :return:
    """
    return "Good bye!"
