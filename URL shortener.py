import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://myurlshortener.com/"

    def shorten_url(self, long_url):
        if long_url in self.url_map:
            return self.url_map[long_url]

        short_url = self.generate_short_url()
        self.url_map[long_url] = short_url
        return short_url

    def generate_short_url(self):
        short_url = ''.join(random.choice(self.chars) for _ in range(6))
        return self.base_url + short_url

# Usage Example
url_shortener = URLShortener()

long_url1 = input("Enter the link :")


long_url2 = "https://www.example.com/guides/getting-started"
short_url2 = url_shortener.shorten_url(long_url2)
print("Short URL 2:", short_url2)
