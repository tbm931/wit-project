from datetime import date

class Version:
    def __init__(self,message):
        self.message = message
        self.date = date.today()
        self.id = hash(self)