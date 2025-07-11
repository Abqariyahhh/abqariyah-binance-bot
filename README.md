# Binance Futures CLI Bot (Mock Version)

👤 Developed by: Abqariyah  
📁 Project Name: `Abqariyah_binance_bot`  
🧪 Mode: Mock Simulation (No real Binance API used – safe for testing)

---

## 🚀 Features Implemented

| Feature            | Description                                                    |
|--------------------|----------------------------------------------------------------|
| ✅ Market Orders    | Buy/sell instantly at market price                             |
| ✅ Limit Orders     | Place orders at a specific price                               |
| ✅ Stop-Limit Orders | Trigger a limit order when a stop price is hit (bonus feature) |
| ✅ Input Validation | Checks symbol and quantity format                              |
| ✅ Structured Logging | All actions stored in `bot.log` with timestamps              |
| ✅ CLI Support      | Run all orders via terminal commands                           |

---

## 🛠️ Setup Instructions

### 1. Clone or unzip the project
git clone https://github.com/Abqariyahhh/abqariyah-binance-bot
cd Abqariyah_binance_bot

### 2. Create your `.env` file
Since mock mode is enabled by default, you can skip API keys.  
But here's the format for future use:
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key


### 3. Install dependencies
```bash
pip install -r requirements.txt

▶️ How to Run Each Module

1. Market Order
python src/market_orders.py SYMBOL SIDE QUANTITY
Example:
python src/market_orders.py BTCUSDT BUY 0.01

2. Limit Order
python src/limit_orders.py SYMBOL SIDE QUANTITY PRICE
Example:
python src/limit_orders.py BTCUSDT SELL 0.01 60000

3. Stop-Limit Order
python src/advanced/stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE
Example:
python src/advanced/stop_limit.py BTCUSDT SELL 0.01 58000 57900

📦 Project Folder Structure
Abqariyah_binance_bot/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── validate.py
│   ├── utils.py
│   └── advanced/
│       └── stop_limit.py
├── .env
├── bot.log
├── README.md
└── report.pdf

🧪 Mock Mode Notes
This bot currently runs in mock mode for safety and testing.

🟢 Use this while your Binance Testnet API is not active.
🔴 To switch to live mode later, go to get_client(mock=True) → change to mock=False.

✅ Notes
No real money is involved — this is fully safe for testing
You can integrate TWAP or OCO orders later for bonus features