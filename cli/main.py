import click 
from loguru import logger
from emailtools.main import EmailAnalyzer

@click.group("cli")
@click.pass_context 
@click.option('--verbose', is_flag=True, help='Print verbose help messages.')
def cli(ctx, verbose):
    '''
    Alignable email stats CLI. 
    '''
    if verbose:
        click.echo('Starting in verbose mode.')

@cli.command('run')
def run():
    '''
    Answers questions in plain text in the logger.
    '''
    analyzer = EmailAnalyzer() 
    q_and_a = analyzer.main()

    for question in list(q_and_a.keys()):
        click.echo(question)
        for answer in q_and_a[question]:
            click.echo('\t * ' + answer)

@cli.command('summary')
def summary():
    '''
    Displays summary of email data.
    '''
    analyzer = EmailAnalyzer() 
    summary = analyzer.get_summary()
    click.echo(summary)

@cli.command('click_open_rates')
def click_open_rates():
    '''
    Get click and open rates.
    '''
    analyzer = EmailAnalyzer() 
    df_summary = analyzer.get_summary()
    rates = analyzer.get_open_click_rates(df_summary)
    click.echo(rates)

@cli.command('conversation_engagement')
def conversation_engagement():
    '''
    Get conversations.
    '''
    analyzer = EmailAnalyzer() 
    df_summary = analyzer.get_summary()
    convos = analyzer.get_conversation_engagement(df_summary)
    click.echo(convos)

@cli.command('connection_requests')
def connection_requests():
    '''
    Get connections.
    '''
    analyzer = EmailAnalyzer() 
    df_summary = analyzer.get_summary()
    connections = analyzer.get_connection_requests_per_100(df_summary)
    click.echo(connections)

if __name__ == '__main__':
    cli(prog_name="cli")