# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, desc, items = []):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def getPossibleExits(self):
        exits = []
        if self.n_to != None:
            exits.append("n")
        if self.s_to != None:
            exits.append("s")
        if self.e_to != None:
            exits.append("e")
        if self.w_to != None:
            exits.append("w")
        return exits
