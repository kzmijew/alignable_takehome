import pandas as pd
from emailtools.settings.config import PGConnector
from loguru import logger
from sqlalchemy import text


class EmailAnalyzer():
    def __init__(self):
        self.pg_conn = PGConnector()
        self.engine = PGConnector.get_connection(self.pg_conn)
    
    def quick_summary(self) -> pd.DataFrame:
        query = text('SELECT * FROM alignable.email_stats;')
        df = pd.read_sql(query, self.engine)
        return(df)
    
    def get_total_emails_sent_by_id(self):
        query = text('SELECT mailing_id, count(DISTINCT sent_email_id) as sends FROM alignable.email_events_full_context GROUP BY 1;')
        output = pd.read_sql(query, self.engine)
        return output
    
    def get_opens_clicks_by_mailer(self, mailing_id):
        query = text(f'SELECT mailing_id, action, event_name FROM ')





