from __future__ import annotations

from getpass import getpass


def print_main_menu() -> None:
    print("\nInstagram terminal app")
    print("-" * 24)
    print("1) Login")
    print("q) Exit")


def read_menu_choice() -> str:
    return input("Select option: ").strip().lower()


def ask_credentials() -> tuple[str, str]:
    username = input("Username: ").strip()
    password = getpass("Password: ")
    return username, password
