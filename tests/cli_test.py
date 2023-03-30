from click.testing import CliRunner
from cli import main 
from loguru import logger

def test_summary():
    runner = CliRunner()
    result = runner.invoke(main.run)
    assert result.exit_code == 0
    assert not result.exception
