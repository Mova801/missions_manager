from datetime import datetime
from rich.panel import Panel


class Achievement:
    def __init__(self, name: str, descr: str, unlocking_date: datetime = None) -> None:
        self.name = name
        self.description = descr
        self.unlocking_date = unlocking_date

    def get_rich(self) -> Panel:
        # handling status
        status: str = "[indian_red]bloccato[/indian_red]"
        new_label: str = " [blink b red]NEW![/blink b red]"
        if self.unlocking_date is not None:
            status = f"[slate_blue1]sbloccato il {self.unlocking_date.strftime('%d/%m/%Y')}[/slate_blue1]"
            new_label = ""
        return Panel(
            self.description,
            title=f"[yellow]{self.name}[/yellow]{new_label}",
            title_align="left",
            subtitle=status,
            width=39, height=4, border_style="grey50")
