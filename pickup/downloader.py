import requests


class SiteDownloader:

    def download(self, url):
        response = requests.get(url)
        return response.text
