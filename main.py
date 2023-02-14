def main() -> None:
    otszaz: list[Otszaz] = []
    with open('penztar.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines():
            otszaz.append(Otszaz(sor))


if __name__ == "__main__":
    main()
