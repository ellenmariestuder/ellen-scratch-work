import abc

class AbcMusician(abc.ABC):
    @abc.abstractmethod
    def nationality(self):
        '''
        Returns musician's nationality

        Should query sf database

        use oauth to pass security
        '''
        NotImplemented

    @abc.abstractproperty
    def name(self):
        '''
        Return's title case of musician's name 

        (entered as instance parameter)
        '''
        NotImplemented


class Musician:
    def __init__(self, name):
        self._name = name

    @property 
    def name(self):
        return self._name.title()

    def nationality(self):
        # COMPLEX QUERIES
        return 'USA'



class JazzMusician(Musician):
    def __init__(self, name):
        super().__init__(name)

    def is_american(self):
        if self.nationality() == 'USA':
            return True
        else:
            return False

dizzy = JazzMusician('dizzy gillespie')
print(dizzy.name)
isinstance(dizzy, Musician)
# print(dizzy._name)
# print(dizzy.nationality())
# print(f"Is {dizzy.name} american? {dizzy.is_american()}")


class Singer:
    def __init__(self, name):
        self._name = name


# class Rapper(Musician):
#     def __init__(self, name):
#         super().__init__(name) #  <- initializes Musician class

#     # override 'nationality' method
#     def nationality(self, continent):
#         # COMPLEX QUERIES'
#         return 'France, ' + continent


# offset = Rapper('Kiari Kendrell Cephus')
# print(offset.name)
# print(offset.nationality())
