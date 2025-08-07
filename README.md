# Caterpillar

## Database Design and Development (CS4092) - Final Project
### Advait Vagerwal, Sahil Thakare, Samarth Prajapati

This database system is designed to support the operations of a stock broker company. It manages users, stocks, portfolios, market orders, price history, and watchlists. The schema is built using a relational model with six interconnected tables.
##  Database Tables

### 1. `Users`
Stores information about clients using the brokerage services.

**Fields:**
- `user_id` (INT, Primary Key)
- `full_name` (VARCHAR)
- `email` (VARCHAR, Unique)
- `phone_number` (VARCHAR)
- `address` (TEXT)
- `date_joined` (DATE)


### 2. `Stocks`
Contains details about the stocks available for trading.

**Fields:**
- `stock_id` (INT, Primary Key)
- `ticker_symbol` (VARCHAR, Unique)
- `company_name` (VARCHAR)
- `sector` (VARCHAR)
- `market` (VARCHAR)


### 3. `Portfolios`
Represents the holdings of each user.

**Fields:**
- `portfolio_id` (INT, Primary Key)
- `user_id` (INT, Foreign Key → Users)
- `stock_id` (INT, Foreign Key → Stocks)
- `quantity` (INT)
- `average_buy_price` (DECIMAL)


### 4. `MarketOrders`
Tracks buy/sell orders placed by users.

**Fields:**
- `order_id` (INT, Primary Key)
- `user_id` (INT, Foreign Key → Users)
- `stock_id` (INT, Foreign Key → Stocks)
- `order_type` (VARCHAR) — `'BUY'` or `'SELL'`
- `quantity` (INT)
- `price` (DECIMAL)
- `order_status` (VARCHAR) — `'PENDING'`, `'EXECUTED'`, `'CANCELLED'`
- `timestamp` (DATETIME)


### 5. `StockPriceHistory`
Stores historical price data for each stock.

**Fields:**
- `history_id` (INT, Primary Key)
- `stock_id` (INT, Foreign Key → Stocks)
- `date` (DATE)
- `open_price` (DECIMAL)
- `close_price` (DECIMAL)
- `high_price` (DECIMAL)
- `low_price` (DECIMAL)
- `volume` (BIGINT)


### 6. `Watchlist`
Tracks stocks that users are monitoring.

**Fields:**
- `watchlist_id` (INT, Primary Key)
- `user_id` (INT, Foreign Key → Users)
- `stock_id` (INT, Foreign Key → Stocks)
- `added_on` (DATE)


## Relationships

- Each **User** can have multiple **Portfolios**, **MarketOrders**, and **Watchlist** entries.
- Each **Stock** can appear in multiple **Portfolios**, **MarketOrders**, **Watchlists**, and **PriceHistory** records.


## Usage

This schema can be used to:
- Track user investments and trading activity.
- Monitor stock performance over time.
- Enable users to place and manage market orders.
- Provide personalized watchlists for stock tracking.


