# coding=utf-8
from ..utils import load_input
from collections import Counter

base_values = "0123456789TJQKA"
joker_values = "0J23456789TQKA"
hand_types =  (0, 2, 22, 3, 32, 4, 5)



def parse_hand(cards: str, joker: bool) -> tuple[int, tuple[int]]:
    hand_value = tuple((joker_values if joker else base_values).index(card)
                       for card in cards)

    if joker and "J" in cards:
        base_hand = "".join(c for c in cards if c != "J")

        best_card = (
            Counter(base_hand).most_common(1)[0][0] if len(base_hand) else "A"
        )

        cards = base_hand + best_card * (5 - len(base_hand))

    card_counts = Counter(cards).values()

    if 5 in card_counts:
        hand_type = 5
    elif 4 in card_counts:
        hand_type = 4
    elif 3 in card_counts:
        if 2 in card_counts:
            hand_type = 32
        else:
            hand_type = 3
    elif 2 in card_counts:
        if len(card_counts) == 3:
            hand_type = 22
        else:
            hand_type = 2
    else:
        hand_type = 0

    return hand_type, hand_value


def sorted_hands(hands: list[tuple[str, int]], joker: bool = False) -> list[tuple[str, int]]:
    return [hand_bid for _, hand_bid in sorted(
        (
            (parse_hand(hand, joker), (hand, bid)) for hand, bid in hands
        ),
        key=lambda i: (hand_types.index(i[0][0]), i[0][1])
    )]


if __name__ == "__main__":
    task_input = load_input(year=2023, day=7, group_lines=False)
    parsed_input = ((hand, int(bid)) for hand, bid in map(str.split, task_input))
    ranked_input = sorted_hands(parsed_input, joker=False)

    part1 = sum(i * hand_bid[1] for i, hand_bid in enumerate(ranked_input, start=1))
    print(f"Part 1: {part1}")

    ranked_input = sorted_hands(ranked_input, joker=True)
    part2 = sum(i * hand_bid[1] for i, hand_bid in enumerate(ranked_input, start=1))
    print(f"Part 2: {part2}")
