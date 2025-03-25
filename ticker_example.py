from stock_calendar_factory import create_stock_calendar


def get_ticker_list_from_announcements(announcements: list) -> list:
    # Extract and return the list of ticker symbols from the announcements.
    return sorted(stock["symbol"] for stock in announcements)


if __name__ == "__main__":
    # Use the factory to create an instance of StockCalendar (API or Dummy)
    calendar = create_stock_calendar()
    test_date = "2025-03-24"
    print("Using implementation:", type(calendar).__name__)

    # Retrieve after-market announcements and extract tickers.
    after_market = calendar.get_after_market_announcements(test_date)
    tickers_after = get_ticker_list_from_announcements(after_market)
    print("After-market tickers on", test_date, ":", tickers_after)

    # Retrieve pre-market announcements and extract tickers.
    pre_market = calendar.get_pre_market_announcements(test_date)
    tickers_pre = get_ticker_list_from_announcements(pre_market)
    print("Pre-market tickers on", test_date, ":", tickers_pre)

    # Retrieve combined outside-session announcements and extract tickers.
    combined = calendar.get_combined_outside_session_announcements(test_date)
    tickers_combined = get_ticker_list_from_announcements(combined)
    print("Combined outside-session tickers for market close on", test_date, ":", tickers_combined)
