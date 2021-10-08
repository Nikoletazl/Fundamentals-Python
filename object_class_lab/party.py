class Party:
    def __init__(self):
        self.people = []

my_party = Party()

name = input()

while not name == "End":
    my_party.people.append(name)
    name = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")