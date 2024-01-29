from typing import Protocol

class Vehicle(Protocol):
    def start_engine(self) -> str:
        ...
    
class Car():
    def __init__(self, car_type: str, car_year: int):
        self.car_type = car_type
        self.car_year = car_year
        
    def start_engine(self) -> str:
        if self.car_year < 0:
            return 'Too old to start!'
        else:
            return 'Car engine starting...'
        
    def get_info(self, num: int) -> list[str]:
        if num < 1:
            return []
        elif num == 1:
            return [self.car_type]
        else:
            return [self.car_type, str(self.car_year)]
        
class Person():
    def __init__(self, person_sex: str, person_age: int):
        self.person_sex = person_sex
        self.person_age = person_age
        
    def walk(self) -> str:
        if self.person_age < 0:
            return 'This person cannot walk.'
        else:
            return 'This person tried to walk.'

class AllMighty():
    def __init__(self):
        ...
    
    def create_vehicle(self, obj: Vehicle) -> None:
        #print(obj.start_engine())
        pass

def main() -> None:
    new_all_mighty = AllMighty()
    new_car = Car('sedan', 1999)
    new_person = Person('female', 32)
    
    '''
    Duck-typing:
    Car class implements start_engine();
    therefore Car instance is an (implicit) Vehicle obj.
    
    Person class does not implement start_engine();
    therefore Person instance is not a Vehicle obj.
    
    No explicit implementation needed. Code is flexible.
    '''
    new_all_mighty.create_vehicle(new_car)
    # Below call will err:
    new_all_mighty.create_vehicle(new_person)

if __name__ == '__main__':
    main()
    