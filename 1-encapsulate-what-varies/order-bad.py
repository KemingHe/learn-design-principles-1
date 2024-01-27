from pancakes import *
    
# Bad implementation of order_pancake
# because pancake creation code 
# will change in the future,
# yet serving pancake won't.
def order_pancake(what_type=None) -> None:
    pancake = None
    if what_type == 'Classic':
        pancake = ClassicPancake('medium')
    elif what_type == 'Chocolate':
        pancake = ChocolatePancake('round')
    elif what_type == 'Banana':
        pancake = BananaPancake()
    
    if pancake:
        print(pancake.cook())
        print(pancake.plate())
    else:
        print("We don't have such type of pancake, sorry.")
