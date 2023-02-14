from otszaz import Otszaz


def main() -> None:
    otszaz: Otszaz = Otszaz('penztar.txt')

    print(otszaz.items)


if __name__ == "__main__":
    main()