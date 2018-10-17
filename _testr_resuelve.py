import unittest
from datetime import datetime
from test_resuelve import get_medium_date


class ResuelveTests(unittest.TestCase):


    def test_get_medium_date(self):
        self.assertEqual(get_medium_date("2017-01-01", "2017-12-31"),
                         datetime.strptime("2017-07-02", "%Y-%m-%d").date())


if __name__ == "__main__":
    unittest.main()