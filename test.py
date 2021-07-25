class Person:
    def __init__(self, name,age,tribe):
        self.name = name
        self.age = age
        self.tribe = tribe

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}. I am {} years old. I am {} by tribe".format(self.name, self.age, self.tribe)
    def __str__(self):
        return "This is {} greeting function".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Kolawole","23","yoruba")
# Call the greeting method
print(some_person.greeting())

print(some_person)

