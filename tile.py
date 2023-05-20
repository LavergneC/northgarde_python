from building import Building 

class Tile:
    def __init__(self, slots_count: int):
        self._slots_count = slots_count
        self._slots_used = 0
        self._buildings = []

    def add_building(self, building: Building) -> bool :
        if self._slots_used >= self._slots_count:
            return False
        
        self._slots_used += 1
        self._buildings.append(building)

    def __str__(self) -> str:
        output = ''
        for building in self._buildings:
            output += str(building) + '\n'

        return output
