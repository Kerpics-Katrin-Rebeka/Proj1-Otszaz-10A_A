from Solution import Solution


def main() -> None:
    sol: Solution = Solution('penztar.txt')
    print(f'2. feladat: \nA fizetések száma: {sol.num_of_payments}')
    print(f'\n3. feladat: \nAz első vásárló {sol.items_bought(1)} darab árucikket vásárolt.')

    print('\n4. feladat:')
    input_order: int = int(input('Adja meg egy vásárlás sorszámát! '))
    # input_item: str = str(input('Adja meg egy árucikk nevét! '))
    input_number: int = int(input('Adja meg a vásárolt darabszámot! '))

    print('\n5. feladat:')
    # print(f'Yehet: {sol.was_bought(input_item)}')

    # print('\n5. task')
    # was_bought: list[int] = []
    # for i, purchases.payments in enumerate(purchases.items):
    #     if item_input in purchases.payments:
    #         was_bought.append(i + 1)

    # print(f'The number of the first purchase: {min(was_bought)}')
    # print(f'The numver of the last purchase: {max(was_bought)}')
    # print(f'This item was bought by {len(was_bought)} costumer(s).')

    print('\n6. feladat:')
    print(f'{input_number} darab vételekor fizetendő: {sol.money_needed(input_number)}')

    print('\n7. feladat')
    print(sol.print_twb(input_order))

    # destination_file = open('sum.txt', 'w')
    # for i, purchases.payments in enumerate(purchases.items):
    #     print(i + 1, ': ', sum(map(worth, purchases.payments.values())), sep='', file=destination_file)


if __name__ == "__main__":
    main()
