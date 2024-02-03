from typing import Optional, get_origin, Any, Type

from pydantic import BaseModel


def split_into_list(cls: Type[BaseModel], data: dict[str, Any]) -> dict[str, Any]:
    for field_name, field_info in cls.model_fields.items():

        if get_origin(field_info.annotation) is not list:
            continue  # we are only interested in lists here

        va = field_info.validation_alias  # it can have multiple choices
        va_choices: Optional[list[str]] = getattr(va, "choices", None) if va else [va]

        # now, following should be the unique set of possible keys
        possible_keys = {pk for pk in [field_name, field_info.alias, *va_choices] if pk}

        for pk in possible_keys:
            field_value: Optional[str] = data.get(pk, None)

            if isinstance(field_value, str):  # even if the string is empty, it should return into list
                values = field_value.strip('[]').split(',')
                values = [value.strip() for value in values]
                data[pk] = [value for value in values if value]

    return data
