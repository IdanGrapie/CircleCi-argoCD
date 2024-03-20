import unittest
import requests

def is_site_reachable(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False

class TestWebsiteAvailability(unittest.TestCase):
    def test_site_reachable(self):
        self.assertTrue(is_site_reachable("http://web:80))


if __name__ == '__main__':
    unittest.main()

