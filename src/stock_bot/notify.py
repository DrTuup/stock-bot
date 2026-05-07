from stock_bot.settings import settings
from stock_bot.models import ETFInfo
import requests


def format_message_json(stock_info: ETFInfo) -> dict:
    """
    Format the stock information into a JSON payload suitable for Discord webhook.

    Args:
        stock_info (ETFInfo): An instance of ETFInfo containing stock information.

    Returns:
        dict: A dictionary formatted for Discord webhook.
    """
    return {
        "content": "",
        "embeds": [
            {
                "title": f"{stock_info.longName} ({stock_info.symbol})",
                "color": 2189312
                if stock_info.regularMarketChangePercent > 0
                else 16711680,
                "fields": [
                    {
                        "name": "Market Change (Percent)",
                        "value": f"{stock_info.regularMarketChange} ({stock_info.regularMarketChangePercent}%)",
                    },
                    {
                        "name": "Market Price",
                        "value": f"€{stock_info.regularMarketPrice:}",
                    },
                    {"name": "Day Low", "value": f"€{stock_info.dayLow}"},
                    {"name": "Day High", "value": f"€{stock_info.dayHigh}"},
                ],
                "author": {"name": "Yahoo Finance"},
            }
        ],
        "username": "Stock Bot",
        "avatar_url": f"{settings.avatar_url}",
        "attachments": [],
    }


def send_discord_notification(payload: dict):
    """
    Send a notification to Discord using the webhook URL.

    Args:
        payload (dict): The JSON payload to send to Discord.
    """

    response = requests.post(settings.discord_webhook_url, json=payload)
    if response.status_code != 204:
        raise Exception(
            f"Failed to send notification: {response.status_code} - {response.text}"
        )
