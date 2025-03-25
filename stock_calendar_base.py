from abc import ABC, abstractmethod

class StockCalendarBase(ABC):
    @abstractmethod
    def get_after_market_announcements(self, date: str) -> list:
        """
        Returns stocks with earnings announcements outside the regular session,
        specifically those after market close (>= 16:00:00) on the given date.
        """
        pass

    @abstractmethod
    def get_pre_market_announcements(self, date: str) -> list:
        """
        Returns stocks with earnings announcements outside the regular session,
        specifically those before market open (< 09:30:00) on the given date.
        """
        pass

    @abstractmethod
    def get_combined_outside_session_announcements(self, market_close_date: str) -> list:
        """
        Returns stocks with earnings announcements outside the regular session.
        It combines after-market announcements (>= 16:00:00) on the market_close_date
        and pre-market announcements (< 09:30:00) on the following day.
        """
        pass
