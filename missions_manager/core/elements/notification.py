from datetime import datetime


class Notification:
    def __init__(self, name: str, date: datetime = None) -> None:
        self.name = name
        self.date = date
