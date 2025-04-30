from dataclasses import dataclass
from enum import StrEnum, Enum


@dataclass(frozen=True)
class WindowConstants:
    app_title: str = "Missions Manager"
    version: str = "1.0.0"
    platform: str = "win10/11"
    release: str = f"release{version}-{platform}"
    missions_title: str = "Elenco Missioni"
    achievements_title: str = "Elenco Achievements"
    console_width: int = 80
    console_height: int = 28
    window_title: str = f'{app_title} - {version} - {platform}'
    loading_title: str = """███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗          
████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║          
██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║          
██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║          
██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║          
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                       
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"""


class ClientColors:
    page_title: str = 'b white'
    panel_title: str = 'b slate_blue1'
    border: str = 'grey50'
    emphasis: str = 'b red'
    emphasis2: str = 'salmon1'
    emphasis3: str = 'sky_blue2'
    warning: str = 'white on light_slate_blue'


class ClientStates(Enum):
    MENU: int = 0
    MISSIONS: int = 1
    ACHIEVEMENTS: int = 2
    MISSION: int = 3


class Commands(StrEnum):
    QUIT: str = "quit"
    MISSIONS: str = "missioni"
    ACHIEVEMENTS: str = "achievements"
    BACK: str = "back"
    SELECT: str = "select"
    HOME: str = "home"


class ClientCommands:
    commands: dict[int, set[str]] = {
        ClientStates.MENU.value: (Commands.MISSIONS.value, Commands.ACHIEVEMENTS.value, Commands.QUIT.value),
        ClientStates.MISSIONS.value: (Commands.SELECT.value, Commands.BACK.value),
        ClientStates.ACHIEVEMENTS.value: set([Commands.BACK.value]),
        ClientStates.MISSION.value: (Commands.HOME.value, Commands.BACK.value)
    }

    KEY_BINDINGS: dict[str, str] = {
        Commands.QUIT: "q",
        Commands.MISSIONS: "m",
        Commands.ACHIEVEMENTS: "a",
        Commands.BACK: "b",
        Commands.SELECT: "s",
        Commands.HOME: "h"
    }
