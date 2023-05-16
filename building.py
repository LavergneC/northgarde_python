from income import Income

class Building:
    def __init__(self, 
                 name : str, 
                 income: Income = None,
                 max_villagers : int = 0):
        self._income = income
        self._name = name
        self._max_villagers = max_villagers
        self._villagers_count = 0

    def __str__(self) -> str:
        output = self._name

        if self._max_villagers:
            output += '\n\t' + f'{self._villagers_count} villager'

            if self._villagers_count >= 2:
                output += 's'

            output += f' ({self._max_villagers} max)'

        if self._income:
            output += '\n\t' + str(self._income)

        return output + '\n'
    
    def add_villagers(self, count: int) -> bool:
        if self._villagers_count + count > self._max_villagers:
            return False
        
        self._villagers_count += count
        return True
    
    def remove_villagers(self, count: int) -> bool:
        if self._villagers_count - count < 0:
            return False
        
        self._villagers_count -= count
        return True