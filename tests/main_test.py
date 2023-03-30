from emailtools.main import EmailAnalyzer

analyzer = EmailAnalyzer()

def test_get_total_emails_sent_by_id():
    df = analyzer.get_total_emails_sent_by_id()

    assert df.shape[0] == 2
    assert df.loc[df.mailing_id == 297147, 'sends'].values == 70067
    assert df.loc[df.mailing_id == 297161, 'sends'].values == 6701

