from unittest import TestCase

import api.utils as _utils


class TestUtils(TestCase):
    def test_validate_date_success(self):
        output = _utils.validate_date("2021-05-19", "2021-05-28")
        self.assertTrue(output)

    def test_validate_date_fail(self):
        output = _utils.validate_date("2021-05-19", None)
        self.assertFalse(output)

    def test_validate_date_fail_2(self):
        output = _utils.validate_date("21-05-19", "21-05-28")
        self.assertFalse(output)

    def test_validate_date_fail_3(self):
        output = _utils.validate_date("2021-05-28", "2021-05-19")
        self.assertFalse(output)

    def test_validate_date_fail_4(self):
        output = _utils.validate_date("2021-19-05", "2021-28-05")
        self.assertFalse(output)

    def test_validate_date_fail_5(self):
        with self.assertRaises(TypeError):
            _utils.validate_date("2021-05-19", 1234567890)
