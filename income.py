from enum import Enum

class Income_type(Enum):
    FOOD = 1
    WOOD = 2
    GOLD = 3
    STONE = 4
    IRON = 5

class Income:
    def __init__(self, income_type : Income_type,
                 income_per_villager : int)  -> None:
        self._income_type = income_type
        self._income_per = income_per_villager

    def set_income_per_villager(self, income_per: int):
        self._income_per = income_per

    def __str__(self) -> str:
        kind = ''
        if self._income_type == Income_type.FOOD:
            kind = 'food'
        elif self._income_type == Income_type.WOOD:
            kind = 'wood'
        elif self._income_type == Income_type.GOLD:
            kind = 'gold'
        elif self._income_type == Income_type.STONE:
            kind = 'stone'
        elif self._income_type == Income_type.IRON:
            kind = 'iron'

        output = f'Income of {self._income_per} {kind} per villager'
        return output

    @property
    def income_per(self):
        return self._income_per