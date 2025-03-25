import requests
from datetime import datetime, timedelta

from stock_calendar_base import StockCalendarBase


class StockCalendarAPI(StockCalendarBase):
    BASE_URL = "https://api.stocktwits.com/api/2/discover/earnings_calendar"

    def _fetch_data(self, date_from: str, date_to: str) -> dict:
        params = {"date_from": date_from, "date_to": date_to}
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MyApp/1.0)"}
        response = requests.get(self.BASE_URL, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}")
        return response.json()

    def get_after_market_announcements(self, date: str) -> list:
        data = self._fetch_data(date, date)
        results = []
        if "earnings" in data and date in data["earnings"]:
            for stock in data["earnings"][date].get("stocks", []):
                if stock.get("time", "") >= "16:00:00":
                    results.append(stock)
        return results

    def get_pre_market_announcements(self, date: str) -> list:
        data = self._fetch_data(date, date)
        results = []
        if "earnings" in data and date in data["earnings"]:
            for stock in data["earnings"][date].get("stocks", []):
                if stock.get("time", "") < "09:30:00":
                    results.append(stock)
        return results

    def get_combined_outside_session_announcements(self, market_close_date: str) -> list:
        dt = datetime.strptime(market_close_date, "%Y-%m-%d")
        next_day = (dt + timedelta(days=1)).strftime("%Y-%m-%d")

        data = self._fetch_data(market_close_date, next_day)
        results = []

        if "earnings" in data and market_close_date in data["earnings"]:
            for stock in data["earnings"][market_close_date].get("stocks", []):
                if stock.get("time", "") >= "16:00:00":
                    results.append(stock)

        if "earnings" in data and next_day in data["earnings"]:
            for stock in data["earnings"][next_day].get("stocks", []):
                if stock.get("time", "") < "09:30:00":
                    results.append(stock)

        return results

# Example usage:
if __name__ == "__main__":
    calendar = StockCalendarAPI()
    test_date = "2025-03-25"

    print("After-market announcements on", test_date)
    print(calendar.get_after_market_announcements(test_date))

    print("\nPre-market announcements on", test_date)
    print(calendar.get_pre_market_announcements(test_date))

    print("\nCombined outside-session announcements for market close on", test_date)
    print(calendar.get_combined_outside_session_announcements(test_date))
