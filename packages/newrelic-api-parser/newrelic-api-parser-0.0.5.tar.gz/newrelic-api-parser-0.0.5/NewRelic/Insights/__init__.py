from NewRelic.Base import BaseNewRelic
from NewRelic import Config
from urllib import parse

class Insights(BaseNewRelic):

    def __init__(self, query_key):
        super().__init__()
        self.BASE_URI = Config.BASE_INSIGHTS_URI
        self.headers['X-Query-Key'] = query_key

    def query(self, account_id, nrql):
        """
        return the insights query data
        """
        url = self.BASE_URI + '/accounts/' + str(account_id) +'/query?nrql=' + parse.quote(nrql)
        return self.get_data(url)