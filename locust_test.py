from xlocust_bigquery.bq_client import BQClientUser
from locust import task,tag

class BQTaskSet(BQClientUser):
    @tag('Test BQ query')
    @task
    def execute_bq_query(self):
        client = self.client()
        data = self.query(client=client,query="SELECT * FROM `moonlit-poetry-327116.users.user-data` LIMIT 1000")
        print(data)
