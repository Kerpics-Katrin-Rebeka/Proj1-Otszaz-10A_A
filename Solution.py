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

    def money_needed(self, input_number: int) -> int:
        if input_number == 0:
            return 0
        elif input_number == 1:
            return 500
        elif input_number == 2:
            return 950
        else:
            return (input_number - 2) * 400 + 950

    def this_was_bought(self, input_order: int) -> dict[str, int]:
        return self._purchases[input_order - 1].things

    def print_twb(self, input_order: int) -> str:
        for key, value in self.this_was_bought(input_order).items():
            print(key, value)

    # def lol(self) -> dict[str, int]:
    #     return self._purchases[1].things

    # def create_file(self):
    #     destination_file = open('osszeg.txt', 'w', encoding='utf-8')
    #     for i, Purchase.items in enumerate(self._purchases):
    #         print(i + 1, ': ', sum(map(money_needed, purchases.payments.values())), sep='', file=destination_file)