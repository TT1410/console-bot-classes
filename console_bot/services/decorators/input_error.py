
def input_error(func):
    def inner(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"{e}\n")
        except KeyError as e:
            print(f"User {e} not found\n")
        except IndexError as e:
            print(f"{e}\n")

    return inner
