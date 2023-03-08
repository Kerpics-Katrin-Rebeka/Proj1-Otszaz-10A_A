from unittest import TestCase
from Purchase import Purchase


class TestPurchase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.purchase1: Purchase = Purchase(['toll', 'kefe'])
        cls.purchase2: Purchase = Purchase(['HB ceruza', 'ceruzaelem', 'csavarkulcs', 'ceruzaelem'])
        cls.purchase3: Purchase = Purchase(['doboz', 'filctoll', 'szatyor', 'colostok', 'doboz'])

    def test_num_of_items(self):
        self.assertEqual(self.purchase1.num_of_items, 2)
        self.assertEqual(self.purchase2.num_of_items, 4)
        self.assertEqual(self.purchase3.num_of_items, 9)

    def test_items(self):
        self.assertEqual(self.purchase1.things, {'toll': 1, 'kefe': 1})
        self.assertEqual(self.purchase2.things, {'HB ceruza': 1, 'ceruzaelem': 2, 'csavarkulcs': 1})
        self.assertEqual(self.purchase3.things, {'doboz': 2, 'filctoll': 1, 'szatyor': 1, 'colostok': 1})
