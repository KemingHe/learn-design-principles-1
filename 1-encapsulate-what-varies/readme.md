# Encapsulates What Varies

Code blob A has two sub parts: A.1 and A.2, where A.1 might change in the future, while A.2 never changes. In this case we should separate A instead of keeping it as one. We can encapsulate the changing A.1 part so future modification of A.1 leaves A.2 completely unaffected.

## How to use this example:

- [pancakes.py](./pancakes.py) declare Pancake Protocol and all concrete types of pancakes
- [order-bad.py](./order-bad.py) demonstrates the non-encapsulated order method, bad for updates
- [order-good.py](./order.good.py) demonstrates the encapsulated order method, just need to update make_pancake to update whole order method
