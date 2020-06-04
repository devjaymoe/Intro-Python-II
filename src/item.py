class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f' Item Name: {self.name},\n Description: {self.description}'

    def on_take(self):
        return f'{self.name} has been added to your inventory!'
    
    def on_drop(self):
        return f'You dropped the {self.name}'