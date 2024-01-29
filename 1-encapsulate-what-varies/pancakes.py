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
    def cook(self):
        return 'Classic Pancake cooked!'
    def plate(self):
        return 'Classic Pancake plated!'
    def p_type(self):
        return 'Classic'

class ChocolatePancake():
    def __init__(self, shape):
        self.shape = shape
    def cook(self):
        return 'Chocolate Pancake cooked!'
    def plate(self):
        return 'Chocolate Pancake plated!'
    def p_shape(self):
        return self.shape

class BananaPancake():
    def __init__(self):
        pass
    def cook(self):
        return 'Banana Pancake cooked!'
    def plate(self):
        return 'Banana Pancake plated!'
    def p_ready(self):
        return True
