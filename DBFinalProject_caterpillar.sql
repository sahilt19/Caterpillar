show databases;
create database caterpillar;
use caterpillar;

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    date_joined DATE
);

-- 2. Stocks Table
CREATE TABLE Stocks (
    stock_id INT PRIMARY KEY,
    ticker_symbol VARCHAR(10) UNIQUE,
    company_name VARCHAR(100),
    sector VARCHAR(50),
    market VARCHAR(50)
);

-- 3. Portfolios Table
CREATE TABLE Portfolios (
    portfolio_id INT PRIMARY KEY,
    user_id INT,
    stock_id INT,
    quantity INT,
    average_buy_price DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

-- 4. MarketOrders Table
CREATE TABLE MarketOrders (
    order_id INT PRIMARY KEY,
    user_id INT,
    stock_id INT,
    order_type VARCHAR(10), -- 'BUY' or 'SELL'
    quantity INT,
    price DECIMAL(10,2),
    order_status VARCHAR(20), -- 'PENDING', 'EXECUTED', 'CANCELLED'
    timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

-- 5. StockPriceHistory Table
CREATE TABLE StockPriceHistory (
    history_id INT PRIMARY KEY,
    stock_id INT,
    date DATE,
    open_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    high_price DECIMAL(10,2),
    low_price DECIMAL(10,2),
    volume BIGINT,
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

-- 6. Watchlist Table
CREATE TABLE Watchlist (
    watchlist_id INT PRIMARY KEY,
    user_id INT,
    stock_id INT,
    added_on DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

-- 1. Users
INSERT INTO Users (user_id, full_name, email, phone_number, address, date_joined)
VALUES
  (1, 'Alice Smith',   'alice.smith@example.com',   '555-1234', '123 Maple St, Anytown, USA', '2025-01-15'),
  (2, 'Bob Johnson',   'bob.johnson@example.com',   '555-5678', '456 Oak Ave, Othercity, USA', '2025-02-20'),
  (3, 'Charlie Davis', 'charlie.davis@example.com', '555-9012', '789 Pine Rd, Smalltown, USA','2025-03-10');

-- 2. Stocks
INSERT INTO Stocks (stock_id, ticker_symbol, company_name,          sector,                market)
VALUES
  (1, 'AAPL',  'Apple Inc.',            'Technology',            'NASDAQ'),
  (2, 'MSFT',  'Microsoft Corporation', 'Technology',            'NASDAQ'),
  (3, 'GOOGL', 'Alphabet Inc.',         'Communication Services','NASDAQ');

-- 3. Portfolios
INSERT INTO Portfolios (portfolio_id, user_id, stock_id, quantity, average_buy_price)
VALUES
  (1, 1, 1,  50, 150.00),   -- Alice holds 50 AAPL at $150.00
  (2, 2, 2,  20, 250.50),   -- Bob holds 20 MSFT at $250.50
  (3, 3, 3,  15, 2700.00);  -- Charlie holds 15 GOOGL at $2,700.00

-- 4. MarketOrders
INSERT INTO MarketOrders (order_id, user_id, stock_id, order_type, quantity, price,   order_status, timestamp)
VALUES
  (1, 1, 1, 'BUY',  10, 155.00, 'PENDING',  '2025-08-05 10:15:00'),
  (2, 2, 2, 'SELL',  5, 260.75, 'EXECUTED', '2025-08-04 14:30:00'),
  (3, 3, 3, 'BUY',   8, 2725.50,'PENDING',  '2025-08-06 09:45:00');

-- 5. StockPriceHistory
INSERT INTO StockPriceHistory (history_id, stock_id, date,       open_price, close_price, high_price, low_price, volume)
VALUES
  (1, 1, '2025-08-04', 153.00,      154.50,      155.00,     152.50,    100000000),
  (2, 2, '2025-08-04', 258.00,      259.80,      261.00,     257.25,     50000000),
  (3, 3, '2025-08-04', 2680.00,     2710.25,     2725.00,    2675.00,     1500000);

-- 6. Watchlist
INSERT INTO Watchlist (watchlist_id, user_id, stock_id, added_on)
VALUES
  (1, 1, 2, '2025-08-02'),  -- Alice is watching MSFT
  (2, 2, 3, '2025-08-03'),  -- Bob is watching GOOGL
  (3, 3, 1, '2025-08-05');  -- Charlie is watching AAPL

-- Trial commands
select * from Users;
select * from StockPriceHistory;
select * from Stocks;


-- (15 points) SQL Queries: Write at least one multi-table query. Example: Show 
-- the names of customers along with the names of the products they purchased 
-- where product price > $100. 
SELECT DISTINCT
  s.company_name, s.ticker_symbol, sector
FROM
  Users AS u
  JOIN Portfolios AS p ON u.user_id = p.user_id
  JOIN Stocks AS s      ON p.stock_id = s.stock_id
WHERE
  u.full_name = 'Alice Smith';

