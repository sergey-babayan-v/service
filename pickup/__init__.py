from .downloader import SiteDownloader
from .parser import Parser


def find_all_numbers(url):
    site_downloader = SiteDownloader()
    html = site_downloader.download(url)
    parser = Parser()
    numbers_set = parser.get_numbers(html)
    for number in numbers_set:
        print(number)