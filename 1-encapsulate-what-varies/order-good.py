from pancakes import *
    
# Now separate creation and serving pancakes,
# (encapsulate pancake creation)
# in order to keep creation flexible,
# while serving static.
def make_pancake(what_type) -> Pancake:
    pancake = None
    if what_type == 'Classic':
        pancake = ClassicPancake('medium')
    elif what_type == 'Chocolate':
        pancake = ChocolatePancake('round')
    elif what_type == 'Banana':
        pancake = BananaPancake()
    return pancake

def order_pancake(what_type):
    pancake = make_pancake(what_type)
    if pancake:
        print(pancake.cook())
        print(pancake.plate())
    else:
        print("We don't have such type of pancake, sorry.")
    