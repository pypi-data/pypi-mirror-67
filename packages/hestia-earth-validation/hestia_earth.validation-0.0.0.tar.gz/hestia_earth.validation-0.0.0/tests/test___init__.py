import unittest

from hestia_earth import validation


class TestValidation(unittest.TestCase):
    def test_validate_true(self):
        self.assertEqual(validation.validate({}), True)


if __name__ == '__main__':
    unittest.main()
