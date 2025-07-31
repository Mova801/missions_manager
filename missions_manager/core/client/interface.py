import os

import keyboard
from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import install

from core.client.constants import WindowConstants, ClientCommands

install(show_locals=True)


class ClientInterface:
    def __init__(self) -> None:
        self.console = Console(height=WindowConstants.console_height)
        self.prompt = Prompt()

    def clear_console(self) -> None:
        os.system('cls')

    def toggle_fullscreen(self) -> None:
        keyboard.press('f11')

    def show_state(self, state, args) -> None:
        state(self.console, args)

    def get_input(self, prompt: str = "command", choices: list[str] = None, use_indices: bool = False) -> str:
        choices = [] if choices is None else choices
        usr_choices: list[str | int]
        return_choices: list[str]
        formatted_choices: list[str]
        if use_indices:
            usr_choices = [str(i) for i, _ in enumerate(choices)]
            return_choices = [c for c in choices]
            formatted_choices = [f"[b white on light_slate_blue] {i} [/b white on light_slate_blue] "
                                 f"[b]{c.title()}[/b]" for i, c in enumerate(choices)]
        else:
            usr_choices = return_choices = [ClientCommands.KEY_BINDINGS.get(c) for c in choices]
            formatted_choices = [
                f"[b white on light_slate_blue] {ClientCommands.KEY_BINDINGS.get(c)} [/b white on light_slate_blue] "
                f"[b]{c.title()}[/b]" for c in choices]
        choices_str: str = " ".join(formatted_choices)
        self.console.print(choices_str)
        usr_in: str = self.prompt.ask(f"[grey50]{prompt}", choices=usr_choices, show_choices=False)

        if use_indices:
            return return_choices[int(usr_in)].lower()
        else:
            return list(
                filter(lambda key: ClientCommands.KEY_BINDINGS[key] == usr_in,
                       ClientCommands.KEY_BINDINGS)).pop().lower()
