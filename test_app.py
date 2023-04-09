import unittest

import app
from logic import check_posted_data


class TestSnippet(unittest.TestCase):

    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_check_posted_data_first_set(self):
        # testing the check_posted_data method with different input sets

        print(f"Testing function - {check_posted_data.__name__} Set 1")

        data_list = [[{"x": 184, "y": 323}, "add", 200], [{"x": 143, "y": 0}, "division", 302], [{"x": 142}, "division",
                                                                                                 301]]

        for data in data_list:
            result = check_posted_data(data[0], data[1])

            self.assertEqual(result, data[2])

            print(f"Test data - {data}")

    def test_check_posted_data_second_set(self):
        print(f"Testing function - {check_posted_data.__name__} Set 2")
        data_list = [[{"x": 184, "y": 323}, "add", 200], [{"x": 143, "y": 0}, "division", 302], [{"y": 143}, "division",
                                                                                                 301]]

        for data in data_list:
            result = check_posted_data(data[0], data[1])

            self.assertEqual(result, data[2])

            print(f"Test data - {data}")

    def test_add(self):
        self.payload = {'x': 2, 'y':3}
        response = self.client.post('/add', json=self.payload)
        self.assertEqual(response.get_json(), {'Message': 5, 'Status Code': 200})
        self.payload = {"x": 143}
        response = self.client.post('/add', json=self.payload)
        self.assertEqual(response.get_json(), {'Message': "An error happened", 'Status Code': 301})
        

    def test_sub(self):        
        self.payload = {'x': 5, 'y':3}
        response = self.client.post('/subtract', json=self.payload)
        self.assertEqual(response.get_json(), {'Message': 2, 'Status Code': 200})
        self.payload = {"x": 143}
        response = self.client.post('/subtract', json=self.payload)
        self.assertEqual(response.get_json(), {'Message': "An error happened", 'Status Code': 301})

    def test_mul(self):        
        self.payload = {'x': 2, 'y':3}
        response = self.client.post('/multiply', json=self.payload)
        self.assertEqual(response.get_json(), {'Message': 6, 'Status Code': 200})
#         self.payload = {"x": 143}
#         response = self.client.post('/multiply', json=self.payload)
#         self.assertEqual(response.get_json(), {'Message': "An error happened", 'Status Code': 301})

#     def test_div(self):        
#         self.payload = {'x': 4, 'y':2}
#         response = self.client.post('/division', json=self.payload)
#         self.assertEqual(response.get_json(), {'Message': 2, 'Status Code': 200})
#         self.payload = {"x": 143}
#         response = self.client.post('/division', json=self.payload)
#         self.assertEqual(response.get_json(), {'Message': "An error happened", 'Status Code': 301})
#         self.payload = {"x": 143, "y": 0}
#         response = self.client.post('/division', json=self.payload)
#         self.assertEqual(response.get_json(), {'Message': "An error happened", 'Status Code': 302})

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(str(response.data.decode('UTF-8')), "Hello World!")


if __name__ == "__main__":
    unittest.main()
