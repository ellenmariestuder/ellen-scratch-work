from four_core import Musician, JazzMusician, Singer, Rapper, OperaSinger

# Base class
miles_davis = Musician('Miles Davis', 'Jazz')
miles_davis.print_name_genre()

# Inherited classes
miles_davis = JazzMusician('Miles Davis', 'Jazz', 'Trumpet', ['Birth of the Cool', 'Kind of Blue', 'Tutu'])
miles_davis.print_name_genre()
miles_davis.print_instrument()
miles_davis.print_albums()

beyonce = Singer('Beyoncé Knowles', 'Pop', 4)
beyonce.print_name_genre()
beyonce.print_instrument()
beyonce.print_octaves()

# Polymorphism
tyga = Rapper('Michael Ray Nguyen-Stevenson', 'Rap', 22898851)
tyga.print_popularity()

janai = OperaSinger('Janai Brugger', 'Opera', 11)
janai.print_popularity()
