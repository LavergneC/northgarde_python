from villager import Villager
from tile import Tile
from building import Building

from income import Income_type
from income import Income

class Game:
    START_VILLAGER_COUNT = 4

    def __init__(self):
        villagers = []

        while len(villagers) < Game.START_VILLAGER_COUNT:
            villagers.append(Villager())

        starting_tile = Tile(slots_count=5)

        self._villagers = villagers
        self._tiles = [starting_tile]

        print(starting_tile)

    def first_strategie(self):
        scout_camp = Building(name="Scout camp", max_villagers=2)
        dock = Building(name='Shipyard', income=Income(Income_type.GOLD, 5), max_villagers=2)
        
        print("Asign 2 villger to dock", self.assign_villager(building=dock, villager_count=2))

        self._tiles[0].add_building(scout_camp)
        self._tiles[0].add_building(dock)

    def assign_villager(self, building: Building, villager_count: int) -> bool:
        if self.free_villager_count < villager_count:
            return False

        success = True
        while villager_count:
            villager_count -= 1
            success |= building.add_villager(self.get_free_villager())

        return success 

    @property
    def free_villager_count(self) -> int:
        count = 0

        for villager in self._villagers:
            if villager.free:
                count += 1

        return count
    
    def get_free_villager(self) -> Villager:
        if not self.free_villager_count:
            return None
        
        for villager in self._villagers:
            if villager.free:
                return villager

        return None
    
    def __str__(self) -> str:
        out = ""
        for tile in self._tiles:
            out += str(tile)

        return out
