class ContactList():
    all_contacts = []
    friends = []
    coworkers = []
    
    def __init__(self, name, number) -> None:
        self._name = name
        self._number = number
        self._relation = None
        ContactList.all_contacts.append({'name': f'{self._name}', 'number': f'{self._number}'})

    def __str__(self) -> str:
        return f"{self._name}: {self._number}"

    @property
    def relation(self) -> str:
        return f"{self._relation}"
    
    @relation.setter
    def relation(self, relation) -> None:
        if(relation.lower() == 'friend'):
            ContactList.friends.append({'name': f'{self._name}', 'number': f'{self._number}'})
        elif(relation.lower() == 'coworker'):
            ContactList.coworkers.append({'name': f'{self._name}', 'number': f'{self._number}'})
        if(self._relation == None):
            self._relation = relation
        else:
            self._relation += f", {relation}"

    @staticmethod
    def contacts() -> None:
        print(f"\nAll Contacts:")
        print(sorted(ContactList.all_contacts, key=lambda x: x['name']))

    @staticmethod
    def my_friends() -> None:
        print(f"\nFriends:")
        print(sorted(ContactList.friends, key=lambda x: x['name']))
    
    @staticmethod
    def my_coworkers() -> None:
        print("\nCoworkers")
        print(sorted(ContactList.coworkers, key=lambda x: x['name']))

    @staticmethod
    def remove_contact(contact) -> str:
        for person in range(0, len(ContactList.all_contacts)):
            if(contact == ContactList.all_contacts[person]['name']):
                ContactList.all_contacts.pop(person)
                break
        
        for person in range(0, len(ContactList.friends)):
            if(contact == ContactList.friends[person]['name']):
                ContactList.friends.pop(person)
                break

        for person in range(0, len(ContactList.coworkers)):
            if(contact == ContactList.coworkers[person]['name']):
                ContactList.coworkers.pop(person)
                break
        
        return f"\n{contact} has been deleted"
    
    @staticmethod
    def find_shared_contacts() -> str:
        shared_list = []
        for i in ContactList.friends:
            if i in ContactList.coworkers:
                shared_list.append(i)
        print("\nFriends I work with:")
        print(sorted(shared_list, key=lambda x: x['name']))

    

# Driver Code #
alice = ContactList('Alice', '867-5309')
bob = ContactList('Bob', '555-5555')
carlos = ContactList('Carlos', '222-2222')
dave = ContactList('Dave', '123-4567')

alice.relation = "Friend"
alice.relation = "Coworker"
bob.relation = "Friend"
carlos.relation = "Coworker"
dave.relation = "Friend"
dave.relation = "Coworker"

ContactList.my_friends()
ContactList.my_coworkers()
ContactList.find_shared_contacts()
ContactList.contacts()
print("____________________________________________________________")
print(ContactList.remove_contact('Alice'))
print("____________________________________________________________")
ContactList.my_friends()
ContactList.my_coworkers()
ContactList.find_shared_contacts()
ContactList.contacts()