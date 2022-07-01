class Party:
    def __init__(self):
        self.people = []

party_people = Party().people

user_input = input()

while user_input != "End":
    party_people.append(user_input)
    user_input = input()

print(f"Going: {', '.join(party_people)}")
print(f"Total: {len(party_people)}")
