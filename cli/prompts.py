from __future__ import annotations

from getpass import getpass


def print_main_menu() -> None:
    print("\nInstagram terminal app")
    print("-" * 24)
    print("1) Login")
    print("q) Exit")


def read_menu_choice() -> str:
    return input("Select option: ").strip().lower()


def print_logged_menu(username: str) -> None:
    print(f"\nInside account: {username}")
    print("-" * 24)
    print("1) Show login status")
    print("b) Back to main menu")


def read_logged_menu_choice() -> str:
    return input("Logged menu option: ").strip().lower()


def ask_credentials() -> tuple[str, str]:
    username = input("Username: ").strip()
    password = getpass("Password: ")
    return username, password
