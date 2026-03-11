people = [
    {
        "name": "zlice",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "dob",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "aharlie",
        "age": 35,
        "city": "Chicago"
    }

]
"""
def f(person):
    return person["age"]
"""


# Using lambda to sort the list of people by age
people.sort(key =lambda person:person ["name"])
print(people)