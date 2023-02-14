from otszaz import Otszaz


def main() -> None:
    otszaz: Otszaz = Otszaz('penztar.txt')

    print(f'2. task: \nNumber of payments: {len(otszaz.items)}')

    print(f'3. task: \nThe first buyer purchased {len(otszaz.items[0])} item(s)')

    print('4. task')
    order_input: int = int(input('Enter an order number! '))
    item_input: str = str(input('Enter the name of an item! '))
    number_input: int = int(input('Enter the number of purchases! '))


if __name__ == "__main__":
    main()
