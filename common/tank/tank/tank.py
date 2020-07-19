from .component import Component


class Tank(Component):

    def __init__(self, health, damage, strategy):
        super().__init__(health, damage)
        self.strategy = strategy

    def as_dict(self):
        return dict(
            health=self.health,
            damage=self.damage
        )

    def get_next_move(self, context):
        self.strategy.get_next_move(context)
