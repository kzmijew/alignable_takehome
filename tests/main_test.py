from emailtools.main import EmailAnalyzer

analyzer = EmailAnalyzer()

def test_get_summary():
    df = analyzer.get_summary()

    assert df.shape[0] == 2
    assert df.shape[1] == 16
    assert df.loc[df.mailing_id == 297147, 'sends'].values == 70067
    assert df.loc[df.mailing_id == 297161, 'sends'].values == 6701
    assert df.index.dtype == 'int64'
    assert df.columns.to_list() == ['mailing_id',
                          'mailer',
                          'action',
                          'sends',
                          'opens',
                          'clicks',
                          'connection_requests_accepted',
                          'connection_requests_accepted_by_session',
                          'connection_requests_sent',
                          'connection_requests_sent_by_session',
                          'recommendations_accepted',
                          'recommendations_accepted_by_session',
                          'recommendations_sent',
                          'recommendations_sent_by_session',
                          'conversation_messages_sent',
                          'conversation_messages_sent_by_session']

def test_get_open_click_rates():
    df = analyzer.get_summary()
    df2 = analyzer.get_open_click_rates(df)

    assert df2.shape[0] == 2
    assert df2.shape[1] == 3

def test_get_conversation_engagement():
    df = analyzer.get_summary()
    df2 = analyzer.get_conversation_engagement(df)

    assert df2.shape[0] == 2
    assert df2.shape[1] == 2

def test_get_connection_requests_per_100():
    df = analyzer.get_summary()
    df2 = analyzer.get_connection_requests_per_100(df)

    assert df2.shape[0] == 2
    assert df2.shape[1] == 10

def test_main():
    main_test = analyzer.main() 

    assert main_test is not None 
    assert type(main_test) == dict 
    assert len(list(main_test.keys())) == 3