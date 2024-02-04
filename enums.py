from enum import Enum


class Role(Enum):
    Batsman = "Batsman"
    Bowler = "Bowler"
    AllRounder = "AllRounder"
    Umpire = "Umpire"

    def __repr__(self):
        return self.value
