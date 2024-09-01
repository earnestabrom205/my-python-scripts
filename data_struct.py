from datetime import datetime


def show_date() -> None:
    print('This is the current time:')
    print(datetime.now())

def greet(name: str) -> None:
    