from enum import Enum
from typing import Any

from pydantic import Field, AliasChoices, BaseModel, model_validator, ConfigDict

import list_aware_model


class Role(Enum):
    Batsman = "Batsman"
    Bowler = "Bowler"
    AllRounder = "AllRounder"

    def __repr__(self):
        return self.value


class Player(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    teams: list[str] = Field(alias='Associated teams', validation_alias=AliasChoices('teams', 'Linked Teams'))
    roles: list[Role] = Field(validation_alias=AliasChoices('Roles', 'role'), default_factory=list)
    fav_dict: dict[int, int] | None  # just for fun

    # noinspection PyNestedDecorators
    @model_validator(mode='before')
    @classmethod
    def parse_lists(cls, data: dict[str, Any]) -> dict[str, Any]:
        return list_aware_model.split_into_list(cls, data)


if __name__ == '__main__':
    player_data = {'name': 'Sachin', 'teams': 'India', 'Linked Teams': 'Hindustan', 'roles': 'Bowler', 'fav_dict': None}
    print(Player(**player_data))
