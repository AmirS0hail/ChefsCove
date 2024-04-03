from src.entity import Entity

class Category(Entity):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.recipes = []
