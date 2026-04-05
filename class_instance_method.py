class Phrase:
    ma_phrase = "Hello, world"

    def initiate(self, ma_phrase):
        self.ma_phrase = ma_phrase


p1 = Phrase() # Crée une instance de la classe Phrase

print(Phrase) # <class '__main__.Phrase'>
print(p1) # <__main__.Phrase object at 0x...>

print(Phrase.__dict__) # {'ma_phrase': 'Hello, world'}
print(vars(Phrase)) # {'ma_phrase': 'Hello, world'}
print(vars(p1)) # {}

print(p1.ma_phrase) # Hello, world
print(Phrase.ma_phrase) # Hello, world

Phrase.mots = Phrase.ma_phrase.split()
print(Phrase.mots) # ['Hello,', 'world']
print(p1.ma_phrase) # Hello, world

print(vars(Phrase)) # {'ma_phrase': 'Hello, world', 'mots': ['Hello,', 'world']}
print(vars(p1)) # {}

p2 = Phrase() # Crée une instance de la classe Phrase
p2.initiate("Good morning") # Initialise l'instance p2 avec la phrase "Good morning"

print(p2.ma_phrase) # Good morning
print(vars(p2)) # {'ma_phrase': 'Good morning'}
