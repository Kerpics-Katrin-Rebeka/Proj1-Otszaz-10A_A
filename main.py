from otszaz import Otszaz


def main() -> None:
    otszaz: Otszaz = Otszaz('penztar.txt')

    print(f'2. task: \nNumber of payments: {len(otszaz.items)}')

    print(f'\n3. task: \nThe first buyer purchased {len(otszaz.items[0])} item(s)')

    print('\n4. task')
    order_input: int = int(input('Enter an order number! '))
    item_input: str = str(input('Enter the name of an item! '))
    number_input: int = int(input('Enter the number of purchases! '))

    print('\n5. task')
    was_bought: list[int] = []
    for i, otszaz.payments in enumerate(otszaz.items):
        if item_input in otszaz.payments:
            was_bought.append(i + 1)

    print(f'The number of the first purchase: {min(was_bought)}')
    print(f'The numver of the last purchase: {max(was_bought)}')
    print(f'This item was bought by {len(was_bought)} costumer(s).')

    def worth(piece: int):
        if piece == 0:
            return 0
        elif piece == 1:
            return 500
        elif piece == 2:
            return 950
        else:
            return (piece - 2) * 400 + 950

    print('\n6. task')
    print(f'You need to pay {worth(number_input)}Ft for {number_input} piece(s) of items.')

    print('\n7. feladat')
    for item, amount in otszaz.items[order_input - 1].items():
        print(amount, item)

if __name__ == "__main__":
    main()
