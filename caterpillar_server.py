import mysql.connector
import pandas as pd
from datetime import datetime, date
import sys

class SimpleStockTradingApp:
    def __init__(self):
        """Initialize database connection"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='caterpillar'
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connected to Caterpillar Stock Database")
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            sys.exit(1)

    def close_connection(self):
        """Close database connection"""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def display_menu(self):
        """Display main menu"""
        print("\n" + "=============================================")
        print("SIMPLE STOCK TRADING APP")
        print("=====================================================")
        print("1. Register New User")
        print("2. Buy Stock")
        print("3. Add to Watchlist")
        print("4. View Stock Price History")
        print("5. View All Portfolios")
        print("6. View All Watchlists")
        print("7. Exit")
        print("====================================================")

    def register_user(self):
        """Register a new user"""
        print("\n--- REGISTER NEW USER ---")
        
        try:
            # Get user details
            user_id = input("Enter User ID: ")
            full_name = input("Enter Full Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            
            # Insert user
            query = """INSERT INTO Users (user_id, full_name, email, phone_number, address, date_joined) 
                      VALUES (%s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(query, (user_id, full_name, email, phone, address, date.today()))
            self.connection.commit()
            
            print(f"User {full_name} registered successfully!")
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def buy_stock(self):
        """Buy stock and add to portfolio"""
        print("\n--- BUY STOCK ---")
        
        try:
            # Show available stocks
            print("Available Stocks:")
            self.cursor.execute("SELECT stock_id, ticker_symbol, company_name, sector FROM Stocks")
            stocks = self.cursor.fetchall()
            
            if not stocks:
                print("No stocks available in database")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(stocks)
            print(df.to_string(index=False))
            
            # Get user input
            user_id = input("\nEnter your User ID: ")
            stock_id = input("Enter Stock ID to buy: ")
            quantity = input("Enter quantity: ")
            price = input("Enter price per share: ")
            
            # Add to portfolio
            portfolio_id = self.get_next_portfolio_id()
            query = """INSERT INTO Portfolios (portfolio_id, user_id, stock_id, quantity, average_buy_price) 
                      VALUES (%s, %s, %s, %s, %s)"""
            self.cursor.execute(query, (portfolio_id, user_id, stock_id, quantity, price))
            self.connection.commit()
            
            print("Stock added to portfolio successfully!")
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def add_to_watchlist(self):
        """Add stock to watchlist"""
        print("\n--- ADD TO WATCHLIST ---")
        
        try:
            # Show available stocks
            print("Available Stocks:")
            self.cursor.execute("SELECT stock_id, ticker_symbol, company_name FROM Stocks")
            stocks = self.cursor.fetchall()
            
            if not stocks:
                print("No stocks available in database")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(stocks)
            print(df.to_string(index=False))
            
            # Get user input
            user_id = input("\nEnter your User ID: ")
            stock_id = input("Enter Stock ID to add to watchlist: ")
            
            # Add to watchlist
            watchlist_id = self.get_next_watchlist_id()
            query = """INSERT INTO Watchlist (watchlist_id, user_id, stock_id, added_on) 
                      VALUES (%s, %s, %s, %s)"""
            self.cursor.execute(query, (watchlist_id, user_id, stock_id, date.today()))
            self.connection.commit()
            
            print("Stock added to watchlist successfully!")
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def view_price_history(self):
        """View stock price history"""
        print("\n--- STOCK PRICE HISTORY ---")
        
        try:
            # Show available stocks
            print("Available Stocks:")
            self.cursor.execute("SELECT stock_id, ticker_symbol, company_name FROM Stocks")
            stocks = self.cursor.fetchall()
            
            if not stocks:
                print("No stocks available in database")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(stocks)
            print(df.to_string(index=False))
            
            stock_id = input("\nEnter Stock ID to view price history: ")
            
            # Get price history
            query = """SELECT date, open_price, close_price, high_price, low_price, volume 
                      FROM StockPriceHistory 
                      WHERE stock_id = %s 
                      ORDER BY date DESC"""
            self.cursor.execute(query, (stock_id,))
            history = self.cursor.fetchall()
            
            if not history:
                print("No price history found for this stock")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(history)
            print(f"\nPrice History for Stock ID {stock_id}:")
            print(df.to_string(index=False))
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_portfolio(self):
        """View all portfolios"""
        print("\n--- ALL PORTFOLIOS ---")
        
        try:
            # Get all portfolios with stock details
            query = """
                SELECT s.ticker_symbol, s.company_name, p.quantity, p.average_buy_price
                FROM Portfolios p
                JOIN Stocks s ON p.stock_id = s.stock_id
                ORDER BY s.ticker_symbol
            """
            self.cursor.execute(query)
            portfolios = self.cursor.fetchall()
            
            if not portfolios:
                print("No portfolios found in database")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(portfolios)
            print("All Portfolios in Database:")
            print(df.to_string(index=False))
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_watchlist(self):
        """View all watchlists"""
        print("\n--- ALL WATCHLISTS ---")
        
        try:
            # Get all watchlists with stock details
            query = """
                SELECT s.ticker_symbol, s.company_name, w.added_on
                FROM Watchlist w
                JOIN Stocks s ON w.stock_id = s.stock_id
                ORDER BY w.added_on DESC
            """
            self.cursor.execute(query)
            watchlists = self.cursor.fetchall()
            
            if not watchlists:
                print("No watchlists found in database")
                return
            
            # Convert to pandas DataFrame for better display
            df = pd.DataFrame(watchlists)
            print("All Watchlists in Database:")
            print(df.to_string(index=False))
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_next_portfolio_id(self):
        """Get next available portfolio ID"""
        self.cursor.execute("SELECT MAX(portfolio_id) FROM Portfolios")
        result = self.cursor.fetchone()
        return (result['MAX(portfolio_id)'] or 0) + 1

    def get_next_watchlist_id(self):
        """Get next available watchlist ID"""
        self.cursor.execute("SELECT MAX(watchlist_id) FROM Watchlist")
        result = self.cursor.fetchone()
        return (result['MAX(watchlist_id)'] or 0) + 1

    def run(self):
        """Main application loop"""
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.buy_stock()
            elif choice == '3':
                self.add_to_watchlist()
            elif choice == '4':
                self.view_price_history()
            elif choice == '5':
                self.view_portfolio()
            elif choice == '6':
                self.view_watchlist()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        
        self.close_connection()

if __name__ == "__main__":
    app = SimpleStockTradingApp()
    app.run()
