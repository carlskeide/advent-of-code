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


if __name__ == "__main__":
    task_input = load_input(day=22, group_lines=True)
    decks = [
        [int(card) for card in deck.splitlines()[1:]] for deck in task_input
    ]

    result = combat(*decks)
    print(f"Part 1: {score(result)}")

    part2 = ""
    print(f"Part 2: {part2}")
