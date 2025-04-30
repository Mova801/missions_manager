from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from core.client.constants import WindowConstants, ClientColors
from core.elements.achievement import Achievement
from core.elements.mission import Mission


def elements_display_menu(console: Console, args: list) -> None:
    elements: list[Mission | Achievement] = args.pop()
    title: str = WindowConstants.achievements_title
    if len(elements) > 0 and type(elements[0]) is Mission:
        title = WindowConstants.missions_title
    # Display elements
    cols = [element.get_rich() for element in elements]
    console.print(Panel(Text(title, justify="center"), style="bold", border_style=ClientColors.border, expand=True))
    console.print(Columns(cols), justify="left")
    console.print('\n' * 3)
