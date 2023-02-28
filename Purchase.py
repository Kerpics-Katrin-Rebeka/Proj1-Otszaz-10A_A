class Purchase():
    _items: dict[str, int]

    @property
    def num_of_items(self) -> int:
        return sum(self._items.values())

    @property
    def things(self) -> dict[str, int]:
        return self._items

    def __init__(self, items: list[str]) -> None:
        self._items = {}
        for e in items:
            if e in self._items:
                self._items[e] += 1
            else:
                self._items[e] = 1
