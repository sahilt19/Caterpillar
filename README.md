# Caterpillar

## Database Design and Development (CS4092) - Final Project
### Advait Vagerwal, Sahil Thakare, Samarth Prajapati

## ALSO: Programming Languages CS 3003 - Final Project
### Sahil Thakare

This database system is designed to support the operations of a stockbroker company. It manages users, stocks, portfolios, market orders, price history, and watchlists. The schema is built using a relational model with six interconnected tables.
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


### Server Side Logic in Python
A command-line Python application that connects to a MySQL database to manage a simple stock trading system.
It allows users to register, buy stocks, track portfolios, create watchlists, and view stock price history.

## Features
Register New Users — Add new traders to the database with personal details.

Buy Stocks — Select from available stocks and add them to a personal portfolio.

Watchlist Management — Track stocks without buying them.

View Price History — Retrieve historical prices for any stock in the system.

Portfolio Viewer — View all users’ holdings and purchase details.

Watchlist Viewer — See all watchlisted stocks and when they were added.

 ## Tech Stack
Language: Python 3.x

Database: MySQL (mysql-connector-python)

Libraries:

mysql.connector — for database connection

pandas — for tabular display of data

datetime — for date handling

## Project Structure
bash
Copy
Edit
caterpillar_server.py   # Main application file
Database Requirements
This app expects a MySQL database named caterpillar with the following tables:

Users

Stocks

Portfolios

Watchlist

StockPriceHistory

Each table must have appropriate fields as used in SQL queries within the script.
Make sure the database is preloaded with some stock records before running.

## Installation & Setup
Clone this project or copy the script into your project directory.

## Install dependencies:

bash
Copy
Edit
pip install mysql-connector-python pandas
Set up MySQL:

Create the caterpillar database.

Create required tables (Users, Stocks, etc.).

Update database credentials in caterpillar_server.py if needed:

python
Copy
Edit
host='localhost',
user='root',
password='root',
database='caterpillar'
Run the app:

bash
Copy
Edit
python caterpillar_server.py
Usage
Once started, the program will display a menu:

pgsql
Copy
Edit
1. Register New User
2. Buy Stock
3. Add to Watchlist
4. View Stock Price History
5. View All Portfolios
6. View All Watchlists
7. Exit
Follow the prompts to perform operations.

## Notes
Ensure MySQL server is running before launching the app.

The script uses incremental IDs for portfolios and watchlists.

All data changes are committed directly to the database.


