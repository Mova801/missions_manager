import requests
from datetime import datetime

from core.elements.notification import Notification
from core.elements.achievement import Achievement
from core.elements.mission import Mission


class ClientModel:
    def __init__(self, server_url: str = 'http://localhost:5000') -> None:
        self.server_url = server_url
        self.missions: list[Mission] = []
        self.achievements: list[Achievement] = []
        self.notifications: list[Notification] = []
        self.message: str = ''

    def load_data(self) -> bool | None:
        try:
            with requests.get(f'{self.server_url}/client_primitives/retrieve_data/') as response:
                print(response.headers.get('Content-length'))
        except requests.exceptions.ConnectionError:
            return None
        for mission in response.json()['missions']:
            self.missions.append(
                Mission(
                    name=mission['name'],
                    descr=mission['description'],
                    likes=mission['likes'],
                    url=mission['url'],
                    start_date=datetime.strptime(mission['start_date'], '%d/%m/%Y')
                    if mission['start_date'] is not None else None,
                    end_date=datetime.strptime(mission['end_date'], '%d/%m/%Y')
                    if mission['end_date'] is not None else None,
                    ended=mission['ended'],
                    team=mission['team']
                )
            )
        for achievement in response.json()['achievements']:
            self.achievements.append(
                Achievement(
                    name=achievement['name'],
                    descr=achievement['description'],
                    unlocking_date=datetime.strptime(achievement['unlocking_date'], '%d/%m/%Y')
                    if achievement['unlocking_date'] is not None else None,
                )
            )
        for notification in response.json()['notifications']:
            self.notifications.append(
                Notification(
                    name=notification['name'],
                    date=datetime.strptime(notification['date'], '%d/%m/%Y')
                    if notification['date'] is not None else None
                )
            )

        self.missions.sort(key=lambda m: m.start_date, reverse=True)

        self.achievements.sort(
            key=lambda a: datetime.now() if a.unlocking_date is None else a.unlocking_date,
            reverse=True
        )
        self.message = response.json()['message']
        return True

    def get_message(self) -> str:
        return self.message

    def get_notifications(self) -> list[Notification]:
        return self.notifications

    def get_achievements_names(self) -> list[str]:
        return [a.name for a in self.achievements]

    def get_achievements(self) -> list[Achievement]:
        return self.achievements

    def get_missions_names(self) -> list[str]:
        return [m.name for m in self.missions]

    def get_missions(self) -> list[Mission]:
        return self.missions

    def get_mission_by_name(self, name: str) -> Mission | None:
        for mission in self.missions:
            if mission.name.lower() == name.lower():
                return mission
        return None
