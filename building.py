from income import Income

class Building:
    def __init__(self, income_type: Income):
        self._income_type = income_type

    def set_income_per_villager(self, income_per: int):
        self._income_per = income_per