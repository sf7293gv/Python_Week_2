from dataclasses import dataclass

@dataclass
class Student:
    name: str
    id: str
    gpa: float

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, gpa: {self.gpa}'
    
    
def main(): # store data in Student class using main method

    # when data passed into Student class, name/id/gpa will be stored
    # in the Student class based on their position in the variable's value
    alex = Student('Alex', 'ax123xa', 3.9)
    print(alex.name)
    print(alex.id)
    print(alex)

if __name__ == '__main__':
    main() # Call main method to store in the Student Class