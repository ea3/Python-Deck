import collections
from random import choice

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
# Picking only the aces by slicing, starting at index 12 and skipping 13 cards.
# print(deck[12::13])

# How many cards? Use len() on the instance.
# print(len(deck))
# random card? Use choice on the instance. Remember to import Random.
# print(choice(deck))
# The First three elements.
# print(deck[:3])
# for card in reversed(deck):
#     print(card)
# Reversed the cards. Two different methods.
# for card in deck[::-1]:
#     print(card)
# print(Card('Q', 'hearts') in deck)
# Ranking cards: Ace is the highest, Spades, hearts, diamonds, clubs(lowest)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
print(len(suit_values))
print(type(suit_values))
print(suit_values)

print(">><<>><<>><<>><<>><<")


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)







# for card in deck:
#     print(card)

# for suit in FrenchDeck.suits:
#     print(suit)
#
#
# print(FrenchDeck.ranks)
# print(FrenchDeck.suits)
# capital = [(suit.capitalize(), rank.capitalize()) for suit in FrenchDeck.suits for rank in FrenchDeck.ranks]
# print(capital)
#
#
# cartas = [Card(rank, suit) for suit in deck.suits
#           for rank in deck.ranks]
# print(cartas)
# print(cartas[-1])
#






