from datetime import datetime, timedelta

from rich.console import Console, Group
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text

import libs
from core.client.constants import WindowConstants, ClientColors
from core.elements.notification import Notification


def main_menu(console: Console, args: list) -> None:
    message: str = args.pop()
    notifications: list[Notification] = args.pop()

    bullet_char: str = '✻'
    osinfo: tuple[str, str] = libs.platform.get_platform()
    if osinfo == ("Windows", "10"):
        bullet_char: str = '*'

    layout = Layout()
    layout.split(
        Layout(
            Panel(Text(WindowConstants.app_title, justify="center"), style="bold",
                  border_style=ClientColors.border,
                  title=WindowConstants.release, title_align="right"),
            name="header", size=3
        ),
        Layout(name="main"),
    )
    layout["main"].split(
        Layout(
            # New messages
            Panel.fit(
                f'[{ClientColors.emphasis}]{bullet_char}[/{ClientColors.emphasis}] {message}',
                title=f"[{ClientColors.panel_title}]Nuovi Messaggi",
                title_align="left",
                border_style=ClientColors.border
            ),
            # height=(max(len(message) // 40 + 2, len(notifications) + 2)
            name="body", ratio=2
        ),
        Layout(name="side"),
        splitter="row"
    )
    layout["side"].split(
        Layout(
            # Notifications
            Panel(Group(
                *[
                    Padding(
                        f" [light_slate_blue]■[/light_slate_blue] "
                        f"[{'blink ' if n.date + timedelta(days=3) > datetime.today() else ''}"
                        f"white][underline]{n.name}[/underline] "
                        f"{f'[{ClientColors.emphasis}](NEW!) ' if (n.date + timedelta(days=3)
                                                                   > datetime.today()) else ''}")
                    for n in notifications
                ]
            ), title=f"[{ClientColors.panel_title}]Notifiche",
                border_style=ClientColors.border,
                height=len(notifications) + 2),
        ),
        # Layout()
    )
    console.print(layout)
