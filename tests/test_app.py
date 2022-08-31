from unittest import TestCase


class TestAPI(TestCase):
    def setUp(self):
        from api.app import create_app
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_get_latest_day(self):
        req = self.app.get('/latest')
        self.assertEqual(req.status_code, 200)

    def test_get_latest_day_2(self):
        req = self.app.get('/latest')
        self.assertIn('Date', req.json[0])

    def test_get_latest_day_avg(self):
        req = self.app.get('/latest/average')
        self.assertEqual(req.status_code, 200)

    def test_get_latest_day_avg_2(self):
        req = self.app.get('/latest/average')
        self.assertIn('Average', req.json[0])

    def test_get_historical(self):
        req = self.app.get('/historical', query_string={
            "from": "2021-05-19",
            "to": "2021-05-28",
        })
        self.assertEqual(req.status_code, 200)

    def test_get_historical_2(self):
        req = self.app.get('/historical', query_string={
            "from": "2021-05-19",
            "to": "2021-05-28",
        })
        self.assertIn('Date', req.json[0])

    def test_get_historical_3(self):
        req = self.app.get('/historical', query_string={
            "from": "2021-05-19",
        })
        self.assertEqual(req.status_code, 400)

    def test_get_historical_4(self):
        req = self.app.get('/historical', query_string={
            "from": "2021-05-19",
        })
        self.assertIn('error', req.json)

    def test_get_historical_5(self):
        req = self.app.get('/historical', query_string={
            "to": "2021-05-19",
        })
        self.assertEqual(req.status_code, 400)

    def test_get_historical_6(self):
        req = self.app.get('/historical', query_string={
            "to": "2021-05-19",
        })
        self.assertIn('error', req.json)

    def test_get_historical_7(self):
        req = self.app.get('/historical', query_string={})
        self.assertIn('error', req.json)

    def test_get_historical_avg(self):
        req = self.app.get('/historical/average', query_string={
            "from": "2021-05-19",
        })
        self.assertEqual(req.status_code, 400)

    def test_get_historical_avg_2(self):
        req = self.app.get('/historical/average', query_string={
            "from": "2021-05-19",
        })
        self.assertIn('error', req.json)

    def test_get_historical_avg_3(self):
        req = self.app.get('/historical/average', query_string={
            "to": "2021-05-28",
        })
        self.assertEqual(req.status_code, 400)

    def test_get_historical_avg_4(self):
        req = self.app.get('/historical/average', query_string={
            "to": "2021-05-28",
        })
        self.assertIn('error', req.json)

    def test_get_avg_highest(self):
        req = self.app.get('/average/highest')
        self.assertEqual(req.status_code, 200)

    def test_get_avg_highest_2(self):
        req = self.app.get('/average/highest')
        self.assertIn('Average', req.json[0])

    def test_get_avg_lowest(self):
        req = self.app.get('/average/lowest')
        self.assertEqual(req.status_code, 200)

    def test_get_avg_lowest_2(self):
        req = self.app.get('/average/lowest')
        self.assertIn('Average', req.json[0])
