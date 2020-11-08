class Student:

    def __init__(self, name, gender, netid):
        self.name = name
        self.gender = gender
        self.netid = netid

    def to_string(self):
        s = "student's name: " + self.name + ", gender: " + self.gender + ", netid: " + netid
        return s

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.gender == other.gender

    def __hash__(self):
        return hash((self.name, self.gender))

