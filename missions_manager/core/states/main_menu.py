from datetime import datetime, timedelta

from rich.console import Console, Group
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.text import Text

from core.client.constants import WindowConstants
from core.elements.notification import Notification


def main_menu(console: Console, args: list) -> None:
    message: str = args.pop()
    notifications: list[Notification] = args.pop()

    layout = Layout()
    layout.split(
        Layout(
            Panel(Text(WindowConstants.app_title, justify="center"), style="bold", border_style="grey50",
                  title="v-0.0.1", title_align="right"),
            name="header", size=3
        ),
        Layout(name="main"),
    )
    layout["main"].split(
        Layout(
            # New messages
            Panel(message, title="[bold blue]Nuovi Messaggi", title_align="left", border_style="grey50",
                  height=(max(5, len(notifications) + 2))),
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
                        f"[{'blink ' if n.date + timedelta(days=3) > datetime.today() else ''}"
                        f"yellow] ■ [underline]{n.name}[/underline] {'[b red](NEW!) ' if (n.date + timedelta(days=3)
                                                                                          > datetime.today()) else ''}")
                    for n in notifications
                ],
                Padding("[blink yellow] ■ [underline]achievements[/underline] [bold red](NEW!)")
            ), title="[bold blue]Notifiche", border_style="grey50", height=len(notifications) + 2),
        ),
        # Layout()
    )
    console.print(layout)
