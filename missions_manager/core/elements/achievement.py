from datetime import datetime
from rich.panel import Panel

from core.client.constants import ClientColors


class Achievement:
    def __init__(self, name: str, descr: str, unlocking_date: datetime = None) -> None:
        self.name = name
        self.description = descr
        self.unlocking_date = unlocking_date

    def get_rich(self) -> Panel:
        # handling status
        status: str = f"bloccato"
        new_label: str = f" [blink {ClientColors.emphasis}]NEW![/blink {ClientColors.emphasis}]"
        if self.unlocking_date is not None:
            status = f"sbloccato il {self.unlocking_date.strftime('%d/%m/%Y')}"
            new_label = ""
        return Panel(
            self.description,
            title=f"[{ClientColors.panel_title}]{self.name}[/{ClientColors.panel_title}]{new_label}",
            title_align="left",
            subtitle=status,
            width=39, height=4, border_style=ClientColors.border)
