class Phrase1:
    "Classe pour gérer les phrases."

    def initia(self, ma_phrase: str):
        "Inialiser une phrase manuellement"
        self.ma_phrase = ma_phrase

    def nb_lettres(self):
        "Obtenir le nombre de lettres dans la phrase."
        return len(self.ma_phrase)


p = Phrase1()
p.initia("Hello, World!")
print(p.nb_lettres())


class Phrase:
    "Classe pour gérer les phrases."

    def __init__(self, ma_phrase: str):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def nb_lettres(self):
        "Obtenir le nombre de lettres dans la phrase."
        return len(self.ma_phrase)

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):
        return mot in self.mots

    def __str__(self):
        return "\n".join(self.mots)


p = Phrase("Hello, World!")
print(p.nb_lettres())
print(len(p))
print("Hi" in p)  # False
print("Hello" in p)  # True
print(str(p))


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in cart")

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


cart = Cart()
cart.add("Laptop")
cart.add("Wireless mouse")
cart.add("Ergo keyboard")
cart.add("Monitor")

for item in cart:
    print(item, end=" ")  # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart))  # 4
print(cart[3])  # Monitor

print("Monitor" in cart)  # True
print("banana" in cart)  # False

cart.remove("Ergo keyboard")

print(cart.list_items())  # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove("banana")  # banana is not in cart
