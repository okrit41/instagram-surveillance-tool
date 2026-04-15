from __future__ import annotations

from cli.prompts import ask_credentials
from session.storage import build_client, save_session


def login_and_persist_session() -> str | None:
    username, password = ask_credentials()
    client = build_client()

    try:
        client.login(username, password)
    except Exception as error:
        print(f"Login failed: {type(error).__name__}: {error}")
        return None

    save_session(client)
    account = client.account_info()

    print("Login successful. Session saved in session.json")
    print(f"Logged in as: {account.username}")
    # Return the entered username to keep control-flow stable for submenu routing.
    return username
