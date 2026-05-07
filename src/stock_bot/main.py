from stock_bot.notify import format_message_json, send_discord_notification
from .fetch_stock_data import fetch_stock_data
from .logger import setup_logger
from .settings import settings

logger = setup_logger()


def main():
    logger.info(f"Starting stock data retrieval for {settings.stock}")
    try:
        stock_info = fetch_stock_data(settings.stock)
    except Exception as e:
        logger.error(f"Error fetching stock data: {e}")

    payload = format_message_json(stock_info)
    send_discord_notification(payload)
