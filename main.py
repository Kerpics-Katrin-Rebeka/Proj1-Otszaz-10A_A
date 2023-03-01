from Solution import Solution


def main() -> None:
    sol: Solution = Solution('penztar.txt')
    print(f'2. feladat: \nA fizetések száma: {sol.num_of_payments}')
    print(f'\n3. feladat: \nAz első vásárló {sol.items_bought(1)} darab árucikket vásárolt.')

    print('\n4. feladat:')
    input_order: int = int(input('Adja meg egy vásárlás sorszámát! '))
    input_item: str = str(input('Adja meg egy árucikk nevét! '))
    input_number: int = int(input('Adja meg a vásárolt darabszámot! '))

    print('\n5. feladat:')
    print(f'Az első vásárlás sorszáma: {sol.min_was_bought(input_item)}')
    print(f'Az utolsó vásárlás sorszáma: {sol.max_was_bought(input_item)}')
    print(f'{sol.total_was_bought(input_item)} vásárlás során vettek belőle.')

    print('\n6. feladat:')
    print(f'{input_number} darab vételekor fizetendő: {sol.money_needed(input_number)}')

    print('\n7. feladat')
    print(sol.print_twb(input_order))

    print('\n8.feladat')
    sol.file_writing()


if __name__ == "__main__":
    main()
