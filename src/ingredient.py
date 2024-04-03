from src.entity import Entity

class Ingredient(Entity):
  def __init__(self, id, name, quantity):
    super().__init__(id, name)
    self.id = id
    self.name = name
    self.quantity = quantity
    self.recipe_id = None
    