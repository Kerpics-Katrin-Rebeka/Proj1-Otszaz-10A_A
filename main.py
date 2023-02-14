from otszaz import Otszaz


def main() -> None:
    otszaz: Otszaz = Otszaz('penztar.txt')

    print(f'2. task: \nNumber of payments: {len(otszaz.items)}')

    print(f'3. task: \nThe first buyer purchased {len(otszaz.items[0])} item(s)')


if __name__ == "__main__":
    main()
