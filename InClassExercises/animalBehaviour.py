class Animal:
    voice = ''
    behave = ''
    animal_type = ''


    def __init__(self, animal_type, voice, behave):
        self.voice = voice
        self.behave = behave
        self.animal_type = animal_type

#first way to do this
    def cat(self):
        print(f"The {self.animal_type} sounds {self.voice} and behaves  {self.behave}")

    def dog(self):
        print(f"The {self.animal_type} sounds {self.voice} and behaves  {self.behave}")



c = Animal('Cat', 'Meow', 'Sneak')
d = Animal('Dog', 'Bark', 'guard')

#can also be written like this
print(f"The type2 {c.animal_type} sounds {c.voice} and behaves  {c.behave}")
print(f"The type3 {d.animal_type} sounds {d.voice} and behaves  {d.behave}")


c.cat()
d.dog()





#print(f"The Dog sounds {self.voice} and behaves  {self.behave}")
