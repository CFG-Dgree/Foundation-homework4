import unittest

from simple_shop import (
    InsufficientFundsError,
    AttemptError,
    validate_option,
    validate_funds,
    process_purchase,
    shop_simulation
)

class ShopSimulationTests(unittest.TestCase):
    def test_validate_option_valid(self):
        items = {
            'table': 80,
            'bed': 160,
            'storage box': 15,
            'mirror': 25
        }
        option = 'bed'
        result = validate_option(option, items)
        self.assertTrue(result)

    def test_validate_option_invalid(self):
        items = {
            'table': 80,
            'bed': 160,
            'storage box': 15,
            'mirror': 25
        }
        option = 'chair'
        with self.assertRaises(ValueError):
            validate_option(option, items)

    def test_validate_funds_sufficient(self):
        option = 'table'
        customer_money = 100
        items = {
            'table': 80,
            'bed': 160,
            'storage box': 15,
            'mirror': 25
        }
        validate_funds(option, customer_money, items)  # Should not raise an error

    def test_validate_funds_insufficient(self):
        option = 'bed'
        customer_money = 100
        items = {
            'table': 80,
            'bed': 160,
            'storage box': 15,
            'mirror': 25
        }
        with self.assertRaises(InsufficientFundsError):
            validate_funds(option, customer_money, items)

    def test_process_purchase(self):
        option = 'storage box'
        customer_money = 50
        items = {
            'table': 80,
            'bed': 160,
            'storage box': 15,
            'mirror': 25
        }
        updated_money = process_purchase(option, customer_money, items)
        expected_money = 35
        self.assertEqual(updated_money, expected_money)


if __name__ == '__main__':
    unittest.main()
