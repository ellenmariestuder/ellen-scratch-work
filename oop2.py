class Person:
    _planet = 'earth'
    
    def __init__(self, name, ssn, favorite_liqor):
        self.name = name
        self._ssn = ssn
        self.favorite_liqor = favorite_liqor
    
    def person_name(self):
        print(self.name)

    def person_details(self):
        print('name: ', self.name, 'age: ', self._ssn)

    def ssn(self):
        print('someone is printing ssn')
        return self._ssn

    def ssn_add_one(self):
        self._ssn = self.ssn()+1

    # def test_ssn(self):
       # self.assertEqual # <--- come back to this
    
    @classmethod
    def planet(cls):
        print('person planet')
        return cls._planet


anita = Person('anita', 333112222, 'mezcal')
# anita_ssn = anita._ssn
# print(anita_ssn)

current_ssn = anita.ssn()
print(current_ssn)
# print(anita.planet())
anita.ssn_add_one()
print(anita.ssn())


# print(anita.planet)
# anita.name = 'savanna'
# Person.planet = 'mars'
# print(anita.name)
# print(anita.planet)









# anthony = Person('anthony', 444556666, 'cachece')
# print(anthony.planet)
# print(anthony.name)


# new_list = ['whiskey', 'tequila']
# new_list = list(('whiskey', 'tequila'))
# print(new_list)

# x = int(5)
# print(x) 

# y = []
# print(type(y))