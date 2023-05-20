from income import Income
from villager import Villager

class Building:
    def __init__(self, 
                 name : str, 
                 income: Income = None,
                 max_villagers : int = 2):
        self._income = income
        self._name = name
        self._max_villagers = max_villagers
        self._asigned_villagers = []

    @property
    def villagers_count(self) -> int:
        return len(self._asigned_villagers)

    def __str__(self) -> str:
        output = self._name

        if self._max_villagers:
            output += '\n\t' + f'{self.villagers_count} villager'

            if self.villagers_count >= 2:
                output += 's'

            output += f' ({self._max_villagers} max)'

        if self._income:
            output += '\n\t' + str(self._income)

        return output + '\n'
    
    def add_villager(self, villager: Villager) -> bool:
        if villager in self._asigned_villagers:
            return False
        
        if villager in self._asigned_villagers:
            return False
        
        if not villager.free:
            return False
        
        if self.villagers_count >= self._max_villagers:
            return False
        
        self._asigned_villagers.append(villager)
        villager.set_free(False)

        return True

    def remove_villager(self, villager: Villager = None) -> bool:
        if not self.villagers_count:
            return False

        if villager is None:
            villager = self._asigned_villagers[0]
        
        if villager not in self._asigned_villagers:
            return False
            
        self._asigned_villagers.remove(villager)
        villager.setFree(True)

        return True