from rich.console import Console, Group
from rich.emoji import Emoji
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

import libs.platform


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
        like_label = f"La missione non è stata aperta a votazioni ([b cyan]0[/b cyan] {like_icon})."
    else:
        like_label = f"E' piaciuta a [b cyan]{mission.likes}[/b cyan] persone."

    # active period label
    dates_label: str = f"Attiva dal [black on yellow]{mission.start_date.strftime('%d/%m/%Y')}[/black on yellow] al "
    if mission.ended:
        dates_label += f"[black on yellow]{mission.end_date.strftime('%d/%m/%Y')}[/black on yellow]"
    else:
        dates_label += "..."
    dates_label += ' ([green]Completata[/green]).' if mission.ended else ' ([b red]In corso[/b red]).'

    if mission.url is not None and osinfo == ("Windows", "10"):
        link_label = f'[b cyan]{mission.url}'
    elif mission.url is not None:
        link_label = f'[b cyan link={mission.url}]{mission.name}'
    else:
        link_label = '[red]Non disponibile'

    team_label: str = ", ".join([f'{member}' for member in mission.team if mission.team is not None]) + '.'

    layout['main'].split(
        Layout(
            Panel(
                mission.description,
                title='[b blue]Lore',
                title_align='left',
                border_style='b red',
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
                    Rule("[b blue]Partecipanti", style="grey50"),
                    Group(team_label),
                    Text(),
                    Rule("[b blue]Pagina Missione", style="grey50"),
                    Padding(link_label),
                ),
                border_style='grey50',
                title='[b blue]Info'
            ),
            name='side',
        ),
        splitter='row'
    )
    console.print(layout)
