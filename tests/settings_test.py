from emailtools.settings import config

pg_connector = config.PGConnector()

def test_connection():
    assert pg_connector.get_connection() is not None