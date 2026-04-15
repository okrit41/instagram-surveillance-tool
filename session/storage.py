from __future__ import annotations

from pathlib import Path

from instagrapi import Client

SESSION_FILE = Path("session.json")


def build_client() -> Client:
    client = Client()

    if SESSION_FILE.exists():
        # Reuse previous session settings when available.
        client.load_settings(str(SESSION_FILE))

    return client


def save_session(client: Client) -> None:
    client.dump_settings(str(SESSION_FILE))
