from comics.aggregator.crawler import CrawlerBase
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = "InkTank"
    language = "en"
    url = "http://www.inktank.com/"
    active = False
    start_date = "2008-03-31"
    end_date = "2010-07-02"
    rights = "Barry T. Smith"


class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        pass  # Comic no longer published
