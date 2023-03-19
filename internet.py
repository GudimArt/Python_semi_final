import requests


class InternetChecker:
    @staticmethod
    def check_internet():
        urls = ["http://httpbin.org/get",
                "http://example.com", "http://google.com"]
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                return True
            except:
                pass
        return False
