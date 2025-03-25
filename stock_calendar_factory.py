from datetime import date

from stock_calendar_api import StockCalendarAPI
from stock_calendar_dummy import StockCalendarDummy


def create_stock_calendar(test_date="2025-03-25"):
    """
    Factory method to create a StockCalendar instance.
    It first tries the API implementation; if that fails, it falls back to the dummy implementation.
    """
    try:
        calendar = StockCalendarAPI()
        # Perform a simple test call to verify the API works.
        _ = calendar.get_after_market_announcements(test_date)
        print("Using StockCalendarAPI implementation.")
        return calendar
    except Exception as e:
        print(f"StockCalendarAPI failed with error: {e}. Falling back to StockCalendarDummy.")
        return StockCalendarDummy()

# Example usage:
if __name__ == "__main__":
    calendar = create_stock_calendar()
    today = date.today().isoformat()
    tickers = [stock["symbol"] for stock in calendar.get_combined_outside_session_announcements(today)]
    print("Tickers for today:", tickers)
