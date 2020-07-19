
from abc import ABC


class Component(ABC):

    def __init__(self, health, damage):
        self._health = health
        self._damage = damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self):
        self._damage = damage
