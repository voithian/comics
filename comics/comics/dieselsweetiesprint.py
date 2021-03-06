from comics.aggregator.crawler import CrawlerBase
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = "Diesel Sweeties (print)"
    language = "en"
    url = "http://www.dieselsweeties.com/"
    active = False
    start_date = "2007-01-01"
    end_date = "2008-08-14"
    rights = "Richard Stevens"


class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        pass  # Comic no longer published
