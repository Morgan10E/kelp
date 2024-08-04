from django.core.management.base import BaseCommand

def get_user_agrees(default: str = "n") -> bool:
    for i in range(5):
        user_input = input().strip().lower()
        if user_input == "":
            user_input = default
        if user_input == "n" or user_input == "y":
            return user_input == "y"
        print("Please enter 'y' or 'n' (without the quotes)")
    print(f"You goofed the entry so many times we're just going to use the default ({default})")
    return default == "y"


def print_success(command: BaseCommand, message: str):
    command.stdout.write(
        command.style.SUCCESS(message)
    )


def print_warning(command: BaseCommand, message: str):
    command.stdout.write(
        command.style.WARNING(message)
    )


def print_error(command: BaseCommand, message: str):
    command.stdout.write(
        command.style.ERROR(message)
    )
