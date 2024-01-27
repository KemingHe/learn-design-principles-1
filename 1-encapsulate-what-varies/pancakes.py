from typing import Protocol

class Pancake(Protocol):
    def cook() -> str:
        ...
    def plate() -> str:
        ...

# Duck-typing in action:
# no need to explicitly implement interface.
class ClassicPancake():
    def __init__(self, size):
        self.size = size
    def cook():
        return 'Classic Pancake cooked!'
    def plate():
        return 'Classic Pancake plated!'
    def p_type():
        return 'Classic'

class ChocolatePancake():
    def __init__(self, shape):
        self.shape = shape
    def cook():
        return 'Chocolate Pancake cooked!'
    def plate():
        return 'Chocolate Pancake plated!'
    def p_shape(self):
        return self.shape

class BananaPancake():
    def __init__(self):
        pass
    def cook():
        return 'Banana Pancake cooked!'
    def plate():
        return 'Banana Pancake plated!'
    def p_ready():
        return True
