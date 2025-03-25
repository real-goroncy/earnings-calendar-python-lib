from datetime import datetime, timedelta

from stock_calendar_base import StockCalendarBase


class StockCalendarDummy(StockCalendarBase):
    """
    Dummy implementation that simulates a stock calendar using fixed data.
    """

    def get_after_market_announcements(self, date: str) -> list:
        # Simulated after-market announcements (>= 16:00:00)
        dummy_data = [
            {"symbol": "DUMMY1", "time": "16:05:00", "date": date, "title": "Dummy Company 1"},
            {"symbol": "DUMMY2", "time": "16:30:00", "date": date, "title": "Dummy Company 2"}
        ]
        return [stock for stock in dummy_data if stock["time"] >= "16:00:00"]

    def get_pre_market_announcements(self, date: str) -> list:
        # Simulated pre-market announcements (< 09:30:00)
        dummy_data = [
            {"symbol": "DUMMY3", "time": "08:00:00", "date": date, "title": "Dummy Company 3"},
            {"symbol": "DUMMY4", "time": "08:15:00", "date": date, "title": "Dummy Company 4"}
        ]
        return [stock for stock in dummy_data if stock["time"] < "09:30:00"]

    def get_combined_outside_session_announcements(self, market_close_date: str) -> list:
        after_market = self.get_after_market_announcements(market_close_date)
        dt = datetime.strptime(market_close_date, "%Y-%m-%d")
        next_day = (dt + timedelta(days=1)).strftime("%Y-%m-%d")
        pre_market = self.get_pre_market_announcements(next_day)
        return after_market + pre_market

# Example usage:
if __name__ == "__main__":
    dummy_calendar = StockCalendarDummy()
    test_date = "2025-03-25"
    print("Dummy after-market announcements on", test_date)
    print(dummy_calendar.get_after_market_announcements(test_date))
    print("Dummy pre-market announcements on", test_date)
    print(dummy_calendar.get_pre_market_announcements(test_date))
    print("Dummy combined outside-session announcements for market close on", test_date)
    print(dummy_calendar.get_combined_outside_session_announcements(test_date))
