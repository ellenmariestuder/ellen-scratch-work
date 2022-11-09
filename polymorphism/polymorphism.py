from inheritance.inheritance import Musician

class Rapper(Musician):
    def __init__(self, name, genre, monthly_streams):
        super().__init__(name, genre)
        self.monthly_streams = monthly_streams
    
    def _popularity(self):
        if self.monthly_streams >= 50000000:
            return 'Extremely High'
        elif self.monthly_streams >= 15000000:
            return 'High'
        elif self.monthly_streams >= 1000000:
            return 'Medium'
        else:
             return 'Low'
    
    def print_popularity(self):
        print(f"{self.name}'s popularity level is: {self._popularity}")

tyga = Rapper('Michael Ray Nguyen-Stevenson', 'Rap', 22898851)
tyga.print_popularity()     

class OperaSinger(Musician):
    def __init__(self, name, genre, starring_roles):
        super().__init__(name, genre)
        self.starring_roles = starring_roles
    
    def _popularity(self):
        if self.starring_roles >= 10:
            return 'High'
        if self.starring_roles >= 5:
            return 'Medium',
        else:
            return 'Low'