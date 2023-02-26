class Purchase():
    _items: dict[str, int] = {}

    @property
    def number_of_items(self) -> int:
        return sum(self._items.values())

    def __init__(self, items: list[str]) -> None:
        for e in items:
            if e in self._items:
                self._items[e] += 1
            else:
                self._items[e] = 1
