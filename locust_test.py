from xlocust_bigquery.bq_client import BQClientUser
from locust import task,tag

class BQTaskSet(BQClientUser):
    @tag('Test BQ query')
    @task
    def execute_bq_query(self):
        self.query("SELECT * FROM `moonlit-poetry-327116.users.user-data` LIMIT 1000")
