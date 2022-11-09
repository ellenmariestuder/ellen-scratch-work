# Base Class
class Musician:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def m_name(self):
        return self.name

    def m_genre(self):
        return self.genre

    def _popularity(self): # <----- Abstraction
        pass

    def print_name_genre(self): # <----- Encapsulation
        print(f"Name: {self.m_name()}, Genre: {self.m_genre()}")

    def print_popularity(self): # <----- Encapsulation
        print(f"{self.name}'s popularity level is: {self._popularity()}")

# Inherited Classes
class JazzMusician(Musician):
    def __init__(self, name, genre, instrument, albums):
        super().__init__(name, genre)
        self.instrument = instrument
        self.albums = albums

    def print_instrument(self):
        print(f"Instrument: {self.instrument}")

    def print_albums(self):
        print(f"Albums: {self.albums}")


class Singer(Musician):
    instrument = 'Voice' # <----- Class Variable
    def __init__(self, name, genre, octaves):
        super().__init__(name, genre)
        self.octaves = octaves

    def print_octaves(self):
        print(f"Octave Range: {self.octaves}")

    @classmethod  # <----- Class Method
    def print_instrument(cls):
        print(f"Instrument: {cls.instrument}")

class Rapper(Musician):
    def __init__(self, name, genre, monthly_streams):
        super().__init__(name, genre)
        self.monthly_streams = monthly_streams

    def _popularity(self): # <----- Polymorphism
        if self.monthly_streams >= 50000000:
            return 'Extremely High'
        elif self.monthly_streams >= 15000000:
            return 'High'
        elif self.monthly_streams >= 1000000:
            return 'Medium'
        else:
            return 'Low'

class OperaSinger(Musician):
    def __init__(self, name, genre, starring_roles):
        super().__init__(name, genre)
        self.starring_roles = starring_roles

    def _popularity(self): # <----- Polymorphism
        if self.starring_roles >= 20:
            return 'High'
        elif self.starring_roles >= 10:
            return 'Medium'
        else:
            return 'Low'

