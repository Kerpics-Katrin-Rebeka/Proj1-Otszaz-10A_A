from Purchase import Purchase


class Solution:
    _purchases: list[Purchase] = []

    @property
    def num_of_payments(self) -> int:
        return len(self._purchases)

    def __init__(self, source: str) -> None:
        sourceFile = open(source, 'r', encoding='utf-8')
        items: list[str] = []
        for line in sourceFile:
            line = line.strip()
            if line == "F":
                self._purchases.append(Purchase(items))
                items.clear()
            else:
                items.append(line)

    def items_bought(self, number_of_purchase: int) -> int:
        return self._purchases[number_of_purchase - 1].num_of_items

    def _was_bought(self, item_input: str) -> list[int]:
        was_bought: list[int] = []
        for i, self._purchases[0] in enumerate(self._purchases):
            if item_input in self._purchases[i].things:
                was_bought.append(i + 1)
        return was_bought

    def min_was_bought(self, item_input: str) -> int:
        return min(self._was_bought(item_input))

    def max_was_bought(self, item_input: str) -> int:
        return max(self._was_bought(item_input))

    def total_was_bought(self, item_input: str) -> int:
        return len(self._was_bought(item_input))

    def money_needed(self, input_number: int) -> int:
        if input_number == 0:
            return 0
        elif input_number == 1:
            return 500
        elif input_number == 2:
            return 950
        else:
            return (input_number - 2) * 400 + 950

    def _this_was_bought(self, input_order: int) -> dict[str, int]:
        return self._purchases[input_order - 1].things

    def print_twb(self, input_order: int) -> None:
        for key, value in self._this_was_bought(input_order).items():
            print(key, value)

    def file_writing(self) -> None:
        destination_file = open('osszeg.txt', 'w', encoding='utf-8')
        for i, self._purchases[0] in enumerate(self._purchases):
            print(i + 1, ': ', sum(map(self.money_needed, self._purchases[i].things.values())), sep='', file=destination_file)
