from __future__ import annotations

from auth.service import login_and_persist_session
from cli.prompts import print_main_menu, read_menu_choice


def run() -> None:
    """Main app loop. New features can be plugged in as menu options."""
    while True:
        print_main_menu()
        option = read_menu_choice()

        if option == "1":
            login_and_persist_session()
            continue

        if option == "q":
            print("Bye")
            break

        print("Invalid option. Use 1 or q.")
