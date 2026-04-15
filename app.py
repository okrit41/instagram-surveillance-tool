from __future__ import annotations

from auth.service import login_and_persist_session
from cli.prompts import (
    print_logged_menu,
    print_main_menu,
    read_logged_menu_choice,
    read_menu_choice,
)


def run_logged_menu(username: str) -> None:
    while True:
        print_logged_menu(username)
        option = read_logged_menu_choice()

        if option == "1":
            print(f"You are logged in as: {username}")
            continue

        if option == "b":
            break

        print("Invalid option. Use 1 or b.")


def run() -> None:
    """Main app loop. New features can be plugged in as menu options."""
    while True:
        print_main_menu()
        option = read_menu_choice()

        if option == "1":
            logged_username = login_and_persist_session()
            if logged_username is not None:
                run_logged_menu(logged_username)
            continue

        if option == "q":
            print("Bye")
            break

        print("Invalid option. Use 1 or q.")
