from otszaz import Otszaz


def main() -> None:
    otszaz: Otszaz = Otszaz('penztar.txt')

    print(f'2. task: \nNumber of payments: {len(otszaz.items)}')


if __name__ == "__main__":
    main()