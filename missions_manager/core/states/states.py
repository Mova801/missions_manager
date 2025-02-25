from core.client.constants import ClientStates
from core.states import main_menu, elements_display, mission_info

CLIENT_STATES = {
    ClientStates.MENU: (lambda x, args: main_menu.main_menu(x, args)),
    ClientStates.MISSIONS: (lambda x, args: elements_display.elements_display_menu(x, args)),
    ClientStates.ACHIEVEMENTS: (lambda x, args: elements_display.elements_display_menu(x, args)),
    ClientStates.MISSION: (lambda x, args: mission_info.missions_info(x, args))
}
