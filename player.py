from enum import Enum

from pydantic import Field, AliasChoices

from list_aware_model import ListAwareModel


class Role(Enum):
    Batsman = "Batsman"
    Bowler = "Bowler"
    AllRounder = "AllRounder"

    def __repr__(self):
        return self.value


class Player(ListAwareModel):
    name: str
    teams: list[str] = Field(alias='Linked Teams', validation_alias=AliasChoices('teams', 'Linked Teams'))
    roles: list[Role] = Field(validation_alias=AliasChoices('Roles', 'roles'))
    fav_dict: dict[int, int] | None  # just for fun
