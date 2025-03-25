# 📅 Stock Calendar Library

A simple, pluggable Python library to retrieve earnings announcements **outside regular trading hours** — specifically **after market close** and **before market open**. Useful for traders who want to react to events before the next trading session starts.

---

## 🔧 Features

- Unified interface via `StockCalendarBase`
- Two interchangeable implementations:
  - **`StockCalendarAPI`** – fetches real earnings data from Stocktwits API
  - **`StockCalendarDummy`** – provides mock data for testing
- Intelligent fallback with a factory method
- Ready-to-use ticker extractor

---

## 🏗️ Structure

```
.
├── stock_calendar_base.py      # Abstract base class
├── stock_calendar_api.py       # Real API-based implementation
├── stock_calendar_dummy.py     # Dummy/mock implementation
├── stock_calendar_factory.py   # Factory with fallback logic
├── ticker_example.py           # Usage example with ticker extraction
```

---

## 🚀 Quick Start

```bash
pip install requests
```

```python
from stock_calendar_factory import create_stock_calendar

calendar = create_stock_calendar()
tickers = calendar.get_combined_outside_session_announcements("2025-03-25")
for stock in tickers:
    print(stock["symbol"], stock["time"])
```

Or just run:

```bash
python ticker_example.py
```

---

## 📘 Example Output

```
After-market tickers on 2025-03-24 : ['AAPL', 'MSFT']
Pre-market tickers on 2025-03-24 : ['GOOG', 'AMZN']
Combined outside-session tickers for market close on 2025-03-24 : ['AAPL', 'MSFT', 'GOOG', 'AMZN']
```

---

## 🧪 Testing Without an API

If the real API fails, the factory automatically falls back to `StockCalendarDummy`, so your code still runs but will spit out nonsense :P.

---

## 🛠️ Requirements

- Python 3.8+
- `requests` (for API-based use)

---

## 📄 License

MIT License
