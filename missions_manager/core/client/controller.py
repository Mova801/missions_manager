from time import sleep

from rich.console import Group
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich.live import Live
from rich.progress import Progress, TextColumn, SpinnerColumn
from rich.text import Text

from core.client import model
from core.client import interface
from core.client.constants import ClientStates, Commands, WindowConstants
from core.client.constants import ClientCommands
from core.states.states import CLIENT_STATES


class ClientController:
    def __init__(self) -> None:
        self.running = True
        self.view = interface.ClientInterface()
        self.model = model.ClientModel("https://xfish.pythonanywhere.com/")
        self.load_data()
        self.state = ClientStates.MENU

    def run(self) -> None:
        args: list = [self.model.get_notifications().copy(), self.model.get_message()]
        while self.running:
            # show current state
            self.view.clear_console()
            self.view.show_state(CLIENT_STATES[self.state], args)
            args.clear()

            # get input
            usr_choice: str = self.view.get_input(choices=ClientCommands.commands[self.state.value])

            # update model (update state)
            if self.state == ClientStates.MENU and usr_choice in ClientCommands.commands[self.state.value]:
                match usr_choice:
                    case Commands.MISSIONS.value:
                        self.state = ClientStates.MISSIONS
                        args.append(self.model.get_missions().copy())
                    case Commands.ACHIEVEMENTS.value:
                        self.state = ClientStates.ACHIEVEMENTS
                        args.append(self.model.get_achievements().copy())
                    case Commands.QUIT.value:
                        self.running = False
            elif self.state == ClientStates.MISSIONS and usr_choice in ClientCommands.commands[self.state.value]:
                match usr_choice:
                    case Commands.SELECT.value:
                        self.view.clear_console()
                        self.view.console.print(
                            Panel(
                                Text("Selezione missioni", justify="center"), style="bold", border_style="grey50"
                            )
                        )
                        mission_name: str = self.view.get_input(
                            "seleziona missione", set(self.model.get_missions_names()), True
                        )
                        self.state = ClientStates.MISSION
                        args.append(self.model.get_mission_by_name(mission_name))
                    case Commands.BACK.value:
                        self.state = ClientStates.MENU
                        args.append(self.model.get_notifications().copy())
                        args.append(self.model.get_message())
            elif self.state == ClientStates.ACHIEVEMENTS and usr_choice in ClientCommands.commands[self.state.value]:
                match usr_choice:
                    case Commands.BACK.value:
                        self.state = ClientStates.MENU
                        args.append(self.model.get_notifications().copy())
                        args.append(self.model.get_message())
            elif self.state == ClientStates.MISSION and usr_choice in ClientCommands.commands[self.state.value]:
                match usr_choice:
                    case Commands.HOME.value:
                        self.state = ClientStates.MENU
                        args.append(self.model.get_notifications().copy())
                        args.append(self.model.get_message())
                    case Commands.BACK.value:
                        self.state = ClientStates.MISSIONS
                        args.append(self.model.get_missions().copy())

    def load_data(self) -> None:
        progress = Progress(
            TextColumn("[b blue]{task.description}", justify="center"),
            SpinnerColumn(spinner_name='dots')
        )
        progress.add_task("Scaricando missioni")
        progress.add_task("Scaricando achievements")
        layout = Layout(
            Group(
                Padding(WindowConstants.loading_title, style='medium_purple'),
                Panel(progress, title="[b white]Caricamento dati", border_style="grey50",
                      height=len(progress.tasks) + 2)
            )
        )
        done: bool = False
        with Live(layout, refresh_per_second=10):
            while not done:
                for job in progress.tasks:
                    if not job.finished:
                        progress.advance(job.id)
                sleep(0.4)
                done = self.model.load_data()
                if done is None:
                    break
        if done is None:
            self.view.clear_console()
            self.view.console.print(
                Panel(
                    "Impossibile stabilire una connessione con il server.",
                    title="[b red]Errore",
                    title_align="left",
                    border_style="grey50", height=3
                )
            )
            self.view.console.print("\nPremi [yellow][Enter][/yellow] per uscire.")
            input()
            exit(0)
