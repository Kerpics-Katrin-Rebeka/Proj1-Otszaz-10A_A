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
