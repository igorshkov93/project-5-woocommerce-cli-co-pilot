import click
import os
from dotenv import load_dotenv
from src.ai.function_calling import process_with_function_calling
from colorlog import ColoredFormatter
import logging

load_dotenv()

# Настройка логирования с цветом
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        '%(log_color)s[%(levelname)s]%(reset)s %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
        }
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logger()

@click.group()
def cli():
    """WooCommerce CLI Co-pilot - AI помощник для магазина"""
    pass

@cli.command()
@click.argument('query')
def ask(query: str):
    """Задай вопрос на естественном языке"""
    logger.info(f"Запрос: {query}")
    
    try:
        result = process_with_function_calling(query)
        click.echo("\n" + "="*50)
        click.echo(result)
        click.echo("="*50 + "\n")
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        click.echo(f"❌ Ошибка: {str(e)}", err=True)

@cli.command()
def config():
    """Проверить конфигурацию"""
    click.echo("📋 Проверка конфигурации:\n")
    
    checks = {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
        'WOO_STORE_URL': os.getenv('WOO_STORE_URL'),
        'WOO_CONSUMER_KEY': os.getenv('WOO_CONSUMER_KEY'),
        'WOO_CONSUMER_SECRET': os.getenv('WOO_CONSUMER_SECRET'),
    }
    
    for key, value in checks.items():
        if value:
            masked = value[:5] + '*' * (len(value) - 10) + value[-5:]
            click.echo(f"✅ {key}: {masked}")
        else:
            click.echo(f"❌ {key}: НЕ УСТАНОВЛЕН")

if __name__ == '__main__':
    cli()
