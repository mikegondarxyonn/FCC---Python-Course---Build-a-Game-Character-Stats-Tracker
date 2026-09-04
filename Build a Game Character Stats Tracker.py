class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1


    def __str__(self):
        return(
            f"Name: {self._name}\n"
            f"Level: {self._level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self._mana}\n"
        )

    @property
    def name(self):
        return self._name
        pass
    
    @property
    def health(self):
        return self._health
        pass

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        if new_health >= 0 and new_health <= 100:
            self._health = new_health
        pass

    
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        if new_mana >= 0 and new_mana <= 50:
            self._mana = new_mana
        pass
    
    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self.name} leveled up to {self.level}!')
        return
