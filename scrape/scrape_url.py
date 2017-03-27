

class ScrapingEngine(object):
    def __init__(self, url=None):
        self.url = url
        self.data = None

    def pull_data_from_url(self):
        pass

    def get_data(self):
        return self.data


class DataAdapter(object):
    def __init__(self, scraping_engine=None):
        self.scraping_engine = scraping_engine

    def format_data(self):
        pass

    def build_data(self):
        pass

    def get_data(self):
        pass


class ScrapeFacade(object):
    def __init__(self, url=None):
        self.url = url

    def run(self):
        try:
            scraping_engine = ScrapingEngine(url=self.url)
            data_adapter = DataAdapter(scraping_engine=scraping_engine)
            return data_adapter.get_data()
        except:
            raise



