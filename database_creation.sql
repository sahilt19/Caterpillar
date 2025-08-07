-- 1. Users Table
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
