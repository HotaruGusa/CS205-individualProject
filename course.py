class Course:

    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
        self.registrations = set()

    def to_string(self):
        s = self.name  + ', professor: '+ self.professor + "registration = " + str(len(self.register))
        return s

    def get_name(self):
        return self.name

    
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash((self.name, self.professor))

    def do_registration(self, student):
        self.registrations.add(student)

    def get_registrations(self):
        return list(self.registrations)
