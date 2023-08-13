import typing

from pydantic import BaseModel


class ListAwareModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        for key, model_field in self.model_fields.items():
            field_type_un_subscripted = typing.get_origin(model_field.annotation)
            if field_type_un_subscripted is not list:  # only list of items is entertained here, at least, as of now
                continue

            # field_type_un_subscripted is list, just check what, among all possible keys, contains the value
            possible_keys = [key] + (model_field.validation_alias.choices if model_field.validation_alias else [])
            for possible_key in possible_keys:
                value = data.get(possible_key, None)
                if value is not None and isinstance(value, str):
                    if not value:  # at this stage it simply means that it is an empty string
                        data[possible_key] = []  # the default value
                        break

                    if not model_field.annotation.__args__:
                        raise ValueError(f'type [{field_type_un_subscripted}] for [{key}] seems to be incomplete')

                    item_type = model_field.annotation.__args__[0]
                    if issubclass(item_type, str):
                        parsed_values = [item.strip() for item in value.split(',')]
                    else:  # item_type should be able to create an instance from the input, or might throw an error
                        parsed_values = [item_type(item.strip()) for item in value.split(',')]
                    data[possible_key] = parsed_values

        super().__init__(**data)
