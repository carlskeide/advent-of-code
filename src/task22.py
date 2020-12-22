# coding=utf-8
from . import load_input


def combat(deck1, deck2):
    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.extend((card1, card2))

        else:
            deck2.extend((card2, card1))

    return deck1 or deck2


def score(deck):
    return sum(
        card * multiplier for multiplier, card
        in enumerate(reversed(deck), start=1)
    )


def recursive_combat(deck1, deck2, depth=1):
    cache = []

    print(f"starting game #{depth}")
    while deck1 and deck2:
        signature = (tuple(deck1), tuple(deck2))
        if signature in cache:
            print("infinite loop!")
            return (deck1, [])

        else:
            cache.append(signature)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        # print(f"{card1} vs {card2}")

        if len(deck1) >= card1 and len(deck2) >= card2:
            print("subgame")
            result = recursive_combat(deck1[:], deck2[:], depth=depth + 1)
            if result[0]:
                deck1.extend((card1, card2))

            else:
                deck2.extend((card2, card1))

        elif card1 > card2:
            deck1.extend((card1, card2))

        else:
            deck2.extend((card2, card1))

    print(f"ending game #{depth}")
    return (deck1, deck2)


if __name__ == "__main__":
    task_input = load_input(day=22, group_lines=True)
    deck1, deck2 = [
        [int(card) for card in deck.splitlines()[1:]] for deck in task_input
    ]

    # result = combat(deck1[:], deck2[:])
    # print(f"Part 1: {score(result)}")

    result = recursive_combat(deck1, deck2)
    print(f"Part 2: {result}")
