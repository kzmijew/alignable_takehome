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


@cli.command('summary')
def summary():
    '''
    Displays summary of email data.
    '''
    analyzer = EmailAnalyzer() 
    summary = analyzer.quick_summary()

    click.echo(summary)

@cli.command('testing')
def testing():
    '''
    Test function.
    '''
    analyzer = EmailAnalyzer() 
    test = analyzer.get_total_emails_sent_by_id()

    click.echo(test)

if __name__ == '__main__':
    cli(prog_name="cli")