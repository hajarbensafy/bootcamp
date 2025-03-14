class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(member)

# Create an instance of the Family class
family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

# Test the methods
family.born(name='Jack', age=0, gender='Male', is_child=True)
print(family.is_18('Michael'))
family.family_presentation()