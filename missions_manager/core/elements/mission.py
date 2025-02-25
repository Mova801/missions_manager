from datetime import datetime

from rich.console import Group
from rich.emoji import Emoji
from rich.padding import Padding
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


class Mission:
    def __init__(self, name: str, descr: str, likes: int, url: str = None, start_date: datetime = None,
                 end_date: datetime = None, ended: bool = True, team: list[str] = None) -> None:
        self.name: str = name
        self.description: str = descr
        self.likes: int = likes
        self.url: str = url
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.ended: bool = ended
        self.team = team if team is not None else ['Nessuno']

    def get_rich(self) -> Panel:
        # handling status
        status: str = "[green]⬤ Completata[/green]"
        if self.end_date is None or self.end_date > datetime.now():
            status = "[blink b red]NEW![/blink b red]"
        start_date_str: str = ''
        end_date_str: str = ''
        # handling dates
        if self.start_date is not None:
            start_date_str = '[grey60]' + self.start_date.strftime("%d/%m/%Y")
            if self.end_date is not None and self.ended:
                end_date_str = '[grey50]-[/grey50]' + self.end_date.strftime("%d/%m/%Y") + '[/grey60]'
            else:
                start_date_str += '[grey50]-[/grey50](...)[/grey60]'

        dlen: int = 64
        descr: str = self.description[:dlen]
        descr += '...' if len(self.description) >= dlen else ''

        like_and_link: str = f'{self.likes}{Emoji("red_heart")}  ' if self.likes is not None else ''
        if self.url is not None:
            like_and_link += f'[b cornflower_blue]([link={self.url}]pagina missione[/link])[/b cornflower_blue]'
        return Panel(
            Group(
                Text(descr, overflow='crop'),
                Padding(like_and_link, (1, 0))
            ),
            title=f"[yellow]{self.name}[/yellow] {status}",
            title_align="left",
            subtitle=f"{start_date_str}{end_date_str}",
            width=30, height=7, border_style="grey50")
