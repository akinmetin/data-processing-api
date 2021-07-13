from unittest import TestCase


class TestDataProcessor(TestCase):
    def setUp(self):
        from data_processor import DataProcessor
        self.data_processor = DataProcessor()

    def test_get_latest_day(self):
        output = self.data_processor.get_latest_day()
        self.assertTrue(type(output) is list)

    def test_get_latest_day_2(self):
        output = self.data_processor.get_latest_day()
        self.assertTrue(type(output[0]) is dict)

    def test_get_latest_day_3(self):
        output = self.data_processor.get_latest_day()
        self.assertEqual(list(output[0].keys()),
                         ["Date", "Open", "High", "Low",
                          "Close", "Adj Close", "Volume"])

    def test_get_latest_day_average(self):
        output = self.data_processor.get_latest_day_average()
        self.assertTrue(type(output) is list)

    def test_get_latest_day_average_2(self):
        output = self.data_processor.get_latest_day_average()
        self.assertTrue(type(output[0]) is dict)

    def test_get_latest_day_average_3(self):
        output = self.data_processor.get_latest_day_average()
        self.assertEqual(len(output[0].keys()), 2)

    def test_get_latest_day_average_4(self):
        output = self.data_processor.get_latest_day_average()
        self.assertEqual(list(output[0].keys()), ["Date", "Average"])

    def test_get_historical_data(self):
        output = self.data_processor.get_historical_data("2021-05-19", "2021-05-28")
        self.assertTrue(type(output) is list)

    def test_get_historical_data_2(self):
        output = self.data_processor.get_historical_data("2021-05-19", "2021-05-28")
        self.assertTrue(type(output[0]) is dict)

    def test_get_historical_data_3(self):
        output = self.data_processor.get_historical_data("2021-05-19", "2021-05-28")
        self.assertEqual(len(output), 8)

    def test_get_historical_data_4(self):
        output = self.data_processor.get_historical_data("2021-05-22", "2021-05-28")
        self.assertIn('error', output)

    def test_get_historical_data_average(self):
        output = self.data_processor.get_historical_data_average("2021-05-20", "2021-05-24")
        self.assertTrue(type(output) is list)

    def test_get_historical_data_average_2(self):
        output = self.data_processor.get_historical_data_average("2021-05-20", "2021-05-24")
        self.assertTrue(type(output[0]) is dict)

    def test_get_historical_data_average_3(self):
        output = self.data_processor.get_historical_data_average("2021-05-20", "2021-05-24")
        self.assertEqual(len(output), 3)

    def test_get_historical_data_average_4(self):
        output = self.data_processor.get_historical_data_average("2021-05-20", "2021-05-24")
        self.assertEqual(list(output[0].keys()), ["Date", "Average"])

    def test_get_historical_data_average_5(self):
        output = self.data_processor.get_historical_data_average("2021-05-22", "2021-05-28")
        self.assertIn('error', output)

    def test_get_average_highest(self):
        output = self.data_processor.get_average_highest()
        self.assertTrue(type(output) is list)

    def test_get_average_highest_2(self):
        output = self.data_processor.get_average_highest()
        self.assertTrue(type(output[0]) is dict)

    def test_get_average_highest_3(self):
        output = self.data_processor.get_average_highest()

        self.assertEqual(list(output[0].keys()),
                         ["Date", "Open", "High", "Low",
                          "Close", "Adj Close", "Volume",
                          "Average"])

    def test_get_average_lowest(self):
        output = self.data_processor.get_average_lowest()
        self.assertTrue(type(output) is list)

    def test_get_average_lowest_2(self):
        output = self.data_processor.get_average_lowest()
        self.assertTrue(type(output[0]) is dict)

    def test_get_average_lowest_3(self):
        output = self.data_processor.get_average_lowest()
        self.assertEqual(list(output[0].keys()),
                         ["Date", "Open", "High", "Low",
                          "Close", "Adj Close", "Volume",
                          "Average"])
