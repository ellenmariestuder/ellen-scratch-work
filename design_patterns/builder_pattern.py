'''
Issues without builder pattern:
 - repetetive
 - not super customizable

'''

class Guitar:
    '''
    '''
    # def __init__(self, body, fret_board, strings, keys, output_jack):
    #     self.body        = body
    #     self.fret_board  = fret_board
    #     self.strings     = strings
    #     self.keys        = keys
    #     self.output_jack = output_jack
    pass



# yamaha_acoustic = Guitar("body", "fret_board", "strings", "keys", None)
# telecaster = Guitar("body", "fret_board", "strings", "keys", "output_jack")


class GuitarBuilder:
    '''
    '''
    def new_guitar(self):
        self._guitar = Guitar()

    def create_basic_guitar(self):
        self._guitar.body       = "body"
        self._guitar.fret_board = "fret_board"
        self._guitar.strings    = "strings"
        self._guitar.keys       = "keys"

    def create_electric_guitar(self):
        self.create_basic_guitar()
        self._guitar.output_jack = "output_jack"

    def get_guitar(self):
        return self._guitar


class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_basic_guitar(self):
        self._builder.new_guitar()
        self._builder.create_basic_guitar()

    def build_electric_guitar(self):
        self._builder.new_guitar()
        self._builder.create_basic_guitar()
        self._builder.create_electric_guitar()

    def get_guitar(self):
        return self._builder.get_guitar()


director = Director(GuitarBuilder())

director.build_basic_guitar()
basic_guitar = director.get_guitar()
# electric_guitar = director.build_electric_guitar()

print(basic_guitar.fret_board)
# print(electric_guitar.output_jack)