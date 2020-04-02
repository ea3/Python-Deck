import collections

# collections.namedtuple(typename, field_names[, verbose=False][, rename=False])
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))

for rank in FrenchDeck.ranks:
    print(rank)

for suit in FrenchDeck.suits:
    print(suit)


print(FrenchDeck.ranks)
print(FrenchDeck.suits)
capital = [(suit.capitalize(), rank.capitalize()) for suit in FrenchDeck.suits for rank in FrenchDeck.ranks]
print(capital)


cartas = [Card(rank, suit) for suit in deck.suits
          for rank in deck.ranks]
print(cartas)
print(cartas[-1])







