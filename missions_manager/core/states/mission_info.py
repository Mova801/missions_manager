from rich.console import Console, Group
from rich.emoji import Emoji
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


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

    # like label
    if mission.likes is None:
        like_label = f"La missione non è stata aperta a votazioni ([b cyan]0[/b cyan] {Emoji('red_heart')} )."
    else:
        like_label = f"E' piaciuta a [b cyan]{mission.likes}[/b cyan] persone."

    # active period label
    dates_label: str = f"Attiva dal [black on yellow]{mission.start_date.strftime('%d/%m/%Y')}[/black on yellow] al "
    if mission.ended:
        dates_label += f"[black on yellow]{mission.end_date.strftime('%d/%m/%Y')}"
    else:
        dates_label += "..."

    status_label: str = '[green]⬤[/green] Completata' if mission.ended else '[b red]⬤[/b red] In corso'
    if mission.url is not None:
        link_label = f'[b cyan link={mission.url}]{mission.name}'
    else:
        link_label = '[red]Non disponibile'

    team_label: str = ", ".join([f'{member}' for member in mission.team if mission.team is not None])

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
                    Rule("[b blue]Info", style="grey50"),
                    Padding(like_label),
                    Padding(dates_label),
                    Text(),
                    Rule("[b blue]Stato", style="grey50"),
                    Padding(status_label),
                    Text(),
                    Rule("[b blue]Partecipanti", style="grey50"),
                    Group(team_label),
                    Text(),
                    Rule("[b blue]Pagina Missione", style="grey50"),
                    Padding(link_label),
                ),
                border_style='grey50',
            ),
            name='side',
        ),
        splitter='row'
    )
    console.print(layout)
