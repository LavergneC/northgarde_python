from villager import Villager
from tile import Tile
from building import Building

from income import Income_type
from income import Income

villagers = []
START_VILLAGER_COUNT = 4

while len(villagers) < START_VILLAGER_COUNT:
    villagers.append(Villager())

starting_tile = Tile(5)

scout_camp = Building(name="Scout camp", max_villagers=2)
dock = Building(name='Shipyard', income=Income(Income_type.GOLD, 5), max_villagers=2)

dock.add_villagers(2)

starting_tile.add_building(scout_camp)
starting_tile.add_building(dock)

print(starting_tile)
