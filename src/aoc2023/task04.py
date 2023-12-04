# coding=utf-8
from ..utils import load_input


def parse_cards(cards: list[str]) -> dict[int, int]:
    parsed = {}
    for card in cards:
        card, numbers = card.split(':')
        winners, candidates = (
            {int(num) for num in group.split()}
            for group in numbers.split('|')
        )
        parsed[int(card.split()[-1])] = len(winners & candidates)

    return parsed


def score(matches: int) -> int:
    return (1 * 2 ** (matches - 1)) if matches else 0


def score_recursive(cards: dict[int, int]) -> dict[int, int]:
    card_counts = {card: 1 for card in cards}
    for card, count in card_counts.items():
        for delta in range(1, cards[card] + 1):
            card_counts[card + delta] += count

    return card_counts


if __name__ == "__main__":
    task_input = load_input(year=2023, day=4, group_lines=False)
    parsed_input = parse_cards(task_input)

    part1 = sum(map(score, parsed_input.values()))
    print(f"Part 1: {part1}")

    part2 = sum(score_recursive(parsed_input).values())
    print(f"Part 2: {part2}")
