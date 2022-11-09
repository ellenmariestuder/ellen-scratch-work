
class Musician:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
    
    def m_name(self):
        return self.name
    
    def m_genre(self):
        return self.genre
    
    def _popularity(self):
        pass

    def print_name_genre(self):
        print(f"Name: {self.m_name()}, Genre: {self.m_genre()}")


miles_davis = Musician('Miles Davis', 'Jazz')
miles_davis.print_name_genre()

class JazzMusician(Musician):
    def __init__(self, name, genre, instrument, albums):
        super().__init__(name, genre)
        self.instrument = instrument
        self.albums = albums
    
    def print_instrument(self):
        print(f"Instrument: {self.instrument}")

    def print_albums(self):
        print(f"Albums: {self.albums}")

miles_davis = JazzMusician('Miles Davis', 'Jazz', 'Trumpet', ['Birth of the Cool', 'Kind of Blue', 'Tutu'])
miles_davis.print_name_genre()
miles_davis.print_instrument()
miles_davis.print_albums()


class Singer(Musician):
    instrument = 'Voice'
    def __init__(self, name, genre, octaves):
        super().__init__(name, genre)
        self.octaves = octaves
    
    def print_octaves(self):
        print(f"Octave Range: {self.octaves}")

    @classmethod
    def print_instrument(cls):
        print(f"Instrument: {cls.instrument}")

beyonce = Singer('Beyoncé Knowles', 'Pop', 4)
beyonce.print_name_genre()
beyonce.print_instrument()
beyonce.print_octaves()

# class Composer(Musician):
# class Rapper(Musician):