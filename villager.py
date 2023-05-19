class Villager:
    def __init__(self):
        self._free = True
        self._heath = 100

    def set_free(self, free: bool):
        self._free = free

    @property
    def free(self):
        return self._free
