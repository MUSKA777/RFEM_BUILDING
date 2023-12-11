from dataclasses import dataclass

@dataclass
class Book:
    '''Object for tracking physical books in a collection.'''
    name: str
    weight: float 
    shelf_id: int = 0


my_book = Book(name="annno", weight=10, shelf_id=5)
print(type(my_book.__class__.__name__))