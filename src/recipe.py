from src.entity import Entity

class Recipe(Entity):
  def __init__(self, id, name, description, category_id):
    super().__init__(id, name)
    self.description = description
    self.category_id = category_id
    self.ingredients = []
