class Otszaz():
    items: list[str] = []
    payments: dict[str, int] = {}

    def __init__(self, source: str) -> None:
        sourceFile = open(source, 'r', encoding='utf-8')
        for line in sourceFile:
            line = line.strip()
            if line == 'F':
                self.items.append(self.payments)
                self.payments = {}
            else:
                self.payments[line] = self.payments.get(line, 0) + 1
        sourceFile.close()
