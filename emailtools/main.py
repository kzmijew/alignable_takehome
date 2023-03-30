import pandas as pd
from emailtools.settings.config import PGConnector
from loguru import logger
from sqlalchemy import text


class EmailAnalyzer():
    def __init__(self):
        self.pg_conn = PGConnector()
        self.engine = PGConnector.get_connection(self.pg_conn)
    
    def get_summary(self) -> pd.DataFrame:
        '''
        Gets summary of all email campaigns.
        '''
        query = text('SELECT * FROM alignable.email_campaign_engagement;')
        df = pd.read_sql(query, self.engine)
        logger.info(f'Retrieved {df.shape[0]} records.')
        return(df)
    
    def get_open_click_rates(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Gets open and click rate engagement.
        '''
        df['open_rate'] = round(df.opens / df.sends, 3)
        df['click_rate'] = round(df.clicks / df.sends, 3)
        df['click_to_open_rate'] = round(df.clicks / df.opens, 3)

        rate_cols = ['open_rate', 'click_rate', 'click_to_open_rate']
        logger.info('Click rates comparison by mailer:')
        return(df[rate_cols])

    def get_conversation_engagement(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Return conversation engagement totals.
        '''
        convo_cols = ['conversation_messages_sent', 'conversation_messages_sent_by_session']
        logger.info('Conversation engagement stats:')
        return(df[convo_cols])
        

    def get_connection_requests_per_100(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Gets connection requests per 100 emails sent.
        '''
        
        connection_cols = ['connection_requests_accepted', 
                           'connection_requests_accepted_by_session',
                           'connection_requests_sent',
                           'connection_requests_sent_by_session']
        
        df_connections = df[['sends'] + connection_cols].copy()
        df_connections['scaled'] = round(df_connections.sends / 100, 2)

        for col in connection_cols:
            scaled_col = col + '_scaled'
            df_connections[scaled_col] = round(df_connections[col] / df_connections['scaled'], 2)


        logger.info('Connection requests per email stats:')
        return(df_connections)
    
    def main(self) -> dict:
        '''
        Answers all questions from single function.
        '''

        questions_and_answers = {
            '1. What email has the highest unique open rate? Click rate? Click-to-open rate?': [],
            '2. What email drives the most conversation messages total?': [],
            '3. What email drives the most connection requests sent per 100 emails sent?': []
        }

        df = self.get_summary()
        df.set_index('mailing_id', inplace=True)

        df_open_click_rates = self.get_open_click_rates(df)
        df_conversation_engagement = self.get_conversation_engagement(df)
        df_connection_requests = self.get_connection_requests_per_100(df)

        # Question 1
        q1 = list(questions_and_answers.keys())[0]
        logger.info(q1)
        max_open, max_open_idx = df_open_click_rates['open_rate'].max(), df_open_click_rates['open_rate'].idxmax()
        max_click, max_click_idx = df_open_click_rates['click_rate'].max(), df_open_click_rates['click_rate'].idxmax()
        max_click_open_rate, max_click_open_rate_idx = df_open_click_rates['click_to_open_rate'].max(), df_open_click_rates['click_to_open_rate'].idxmax()

        questions_and_answers[q1].append(f'Email {max_open_idx} had the highest unique open rate at {round(max_open * 100, 1)}%.')
        questions_and_answers[q1].append(f'Email {max_click_idx} had the highest click rate at {round(max_click * 100, 1)}%.')
        questions_and_answers[q1].append(f'Email {max_click_open_rate_idx} had the highest click-to-open rate at {round(max_click_open_rate * 100, 1)}%.')

        # Question 2
        q2 = list(questions_and_answers.keys())[1]
        logger.info(questions_and_answers[q2])
        most_msg, most_msg_idx = df_conversation_engagement['conversation_messages_sent'].max(), df_conversation_engagement['conversation_messages_sent'].idxmax()

        questions_and_answers[q2].append(f'Email {most_msg_idx} had the most conversation messages at {most_msg}.')

        # Question 3
        q3 = list(questions_and_answers.keys())[2]
        logger.info(questions_and_answers[q3])

        scaled_conn_requests, scaled_conn_requests_idx = df_connection_requests['connection_requests_sent_scaled'].max(), df_connection_requests['connection_requests_sent_scaled'].idxmax() 

        questions_and_answers[q3].append(f'Email {scaled_conn_requests_idx} has the most connection requests per 100 emails at {scaled_conn_requests}.')

        return(questions_and_answers)


