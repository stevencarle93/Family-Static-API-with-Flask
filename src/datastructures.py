
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._family_members = [{
            "id": self._generateId(),
            "first_name": "Richard",
            "last_name": self.last_name,
            "age": 34,
            "lucky_numbers": []
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        adding_family_member = {}

        if 'id' in member:
            member['id']
            adding_family_member['id'] = int(member['id'])
        else:
            adding_family_member['id'] = self._generateId()

        adding_family_member['first_name'] = str(member['first_name'])
        adding_family_member['last_name'] = self.last_name
        adding_family_member['age'] = int(member['age'])
        adding_family_member['lucky_numbers'] = member['lucky_numbers']

        self._family_members.append(adding_member)
        print(adding_member)

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._family_members

    def get_member(self, id):
        # fill this method and update the return
        for member in self._family_members:
            if member["id"] == int(id):
                return member

        return None

    # método para actualizar familiares
    def update_member(self, id, member):
        for member in range(len(self._family_members)):
            if self._family_members[member]["id"] == int(id):
                self._family_members[member].update(member)
                return {"done": True}

    def delete_member(self, id):
        # fill this method and update the return
        for member in range(len(self._family_members)):
            if self._family_members[member]["id"] == int(id):
                self._family_members.pop(member)
                return {"done": True}

        return None
