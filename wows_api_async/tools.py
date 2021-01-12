from math import ceil
from typing import List, Callable, Type

from pydantic import BaseModel


def avg(items: List[int], round_to = 1) -> float:
    return round(sum(items) / len(items), round_to)


def split_list(list_: list, limit: int) -> list:
    """
    >>> split_list([1,2,3,4,5,6,7], 3)
    [[1, 2, 3], [4, 5, 6], [7]]
    >>> split_list([1,2,3,4,5,6,7], 2)
    [[1, 2], [3, 4], [5, 6], [7]]
    >>> split_list([1,2,3], 4)
    [[1, 2, 3]]
    """

    chunks = int(ceil(len(list_) / limit))

    return [list_[i * limit:(i * limit) + limit] for i in range(chunks)]


def dict_key_transform(data: dict, transform: Callable) -> dict:
    return {transform(k): v for k, v in data.items()}


def generate_model_field_list(model: Type[BaseModel]) -> List[str]:
    res = []
    for name, field in model.__fields__.items():
        if issubclass(field.type_, BaseModel):
            res += [f'{name}.{n}' for n in generate_model_field_list(field.type_)]
        else:
            res.append(name)

    return res


def stringize(int_list: List[int]) -> str:
    return ','.join(map(str, int_list))


def chunk_list(lst: list, n: int) -> list:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
