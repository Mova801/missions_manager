from rich.console import Console, Group
from rich.emoji import Emoji
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

import libs.platform
from core.client.constants import ClientColors


def missions_info(console: Console, args: list) -> None:
    mission = args.pop()
    # Display elements
    layout = Layout()
    layout.split(
        Layout(
            Panel(
                Text(f"Missione {mission.name}", justify='center'),
                style="bold",
                border_style="grey50"
            ),
            name="header", size=3
        ),
        Layout(ratio=1, name="main"),
    )

    # like icon (handling for Win10)
    like_icon: str = f'{Emoji('red_heart')} '
    osinfo: tuple[str, str] = libs.platform.get_platform()
    if osinfo == ("Windows", "10"):
        like_icon = "like"

    # like label
    if mission.likes is None:
        like_label = (f"La missione non è stata aperta a votazioni "
                      f"([b {ClientColors.emphasis3}]0[/b {ClientColors.emphasis3}] {like_icon}).")
    else:
        like_label = f"E' piaciuta a [b {ClientColors.emphasis3}]{mission.likes}[/b {ClientColors.emphasis3}] persone."

    # active period label
    if mission.ended:
        dates_label = f"Attiva dal [{ClientColors.warning}]{mission.start_date.strftime('%d/%m/%Y')}"\
                      f"[/{ClientColors.warning}] al [{ClientColors.warning}]{mission.end_date.strftime('%d/%m/%Y')}"\
                    f"[/{ClientColors.warning}] ([{ClientColors.emphasis3}]Completata[/{ClientColors.emphasis3}])."
    else:
        dates_label = f"Iniziata il [{ClientColors.warning}]{mission.start_date.strftime('%d/%m/%Y')}"\
                        f"[/{ClientColors.warning}] ([b red]In corso[/b red])."

    if mission.url is not None and osinfo == ("Windows", "10"):
        link_label = f'[b {ClientColors.emphasis3}]{mission.url}'
    elif mission.url is not None:
        link_label = f'[b {ClientColors.emphasis3} link={mission.url}]{mission.name}'
    else:
        link_label = '[red]Non disponibile.'

    team_label: str = ", ".join([f'{member}' for member in mission.team if mission.team is not None]) + '.'

    layout['main'].split(
        Layout(
            Panel(
                mission.description,
                title='[b blue]Lore',
                title_align='left',
                border_style=ClientColors.emphasis,
            ),
            name='body', ratio=3
        ),
        Layout(
            Panel(
                Group(
                    Padding(like_label),
                    Padding(dates_label),
                    # Text(),
                    # Rule("[b blue]Stato", style="grey50"),
                    # Padding(status_label),
                    Text(),
                    Rule("[b blue]Partecipanti", style=ClientColors.border),
                    Group(team_label),
                    Text(),
                    Rule("[b blue]Pagina Missione", style=ClientColors.border),
                    Padding(link_label),
                ),
                border_style=ClientColors.border,
                title='[b blue]Info'
            ),
            name='side',
        ),
        splitter='row'
    )
    console.print(layout)
