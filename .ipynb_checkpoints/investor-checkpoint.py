import numpy as np 
import pandas as pd 
#

class Investor:
    def __init__(self,name,init_deposit,verbose=False):
        self.name = name 
        self.init_deposit = init_deposit
        self.verbose = verbose
        self.current_money = init_deposit
        self.profit = [0] 
        self.stocks = {}
        self.amount_spent = 0 
        self.portfolio = [self.current_money];
        self.stock_profit = {}
        self.transaction_history = pd.DataFrame(
                columns=['date','symbol','action','shares','price','total','dca'])

    def __str__(self):
        return f"""
name          : {self.name}
money held    : {self.current_money:,.2f}
amount spent  : {self.amount_spent}
stocks        : {list(self.stocks.keys())}
profit        : {self.profit[-1]}

    """ + "\n" + '-'*40 + "\n" + self.transaction_history.__str__()

    def depositMoney(self,amount):
        """
        deposit amount to current_money
        """
        self.current_money+=amount; 

    def withdrawMoney(self,amount):
        """
        withdraw amount to current_money
        """
        if self.current_money > amount:
            self.current_money -=amount
        else: 
            if self.verbose:
                print(f'there is not enough money to withdraw {amount}')
            amount = 0 
        return amount 

    def updatePortfolio(self,stocks):
        """
        update overall investor's portfolio, with the 
        current prices of each of their stocks 
        """
        current_portfolio = self.current_money
        for symbol,shares in self.stocks.items():
            price = stocks[symbol] ## update to current price of share 
            current_portfolio += price*shares
        self.portfolio.append(current_portfolio)

    def calculateProfit(self,stocks):
        running_profit = 0
        for symbol,shares in self.stocks.items():
            
            current_price = stocks[symbol]
            price = self.transaction_history[self.transaction_history["symbol"]==symbol]['price']
            shares = self.transaction_history[self.transaction_history["symbol"]==symbol]['shares']
            avg_cost = (price*shares).sum()/shares.sum()
            shares = shares.sum()

            self.stock_profit[symbol] = {'profit/share': current_price - avg_cost ,
                                         'profit' : (current_price - avg_cost)*shares,
                                         'pct' : np.round((current_price - avg_cost)/avg_cost,2)
                                        }

            running_profit += (current_price - avg_cost)*shares
        self.profit.append({'total profit': running_profit,
                            'profit pct': np.round(running_profit/self.amount_spent,2)})

    def logTransaction(self,symbol,shares,price,date,action):

        price_h = self.transaction_history[self.transaction_history["symbol"]==symbol]['price']
        shares_h = self.transaction_history[self.transaction_history["symbol"]==symbol]['shares']
        avg_cost = ((price_h*shares_h).sum() + price*shares)/(shares_h.sum()+shares)

        self.transaction_history = self.transaction_history.append(
                {'date'   :date,
                 'symbol' :symbol,
                 'action' :action,
                 'shares' :shares,
                 'price'  :price,
                 'total'  :shares*price,
                 'dca'    :avg_cost
                 },ignore_index=True)

    def buy(self,symbol,shares,price,date=None):
        """
        buy #{shares} from symbol at {price} 
        """
        if self.current_money > shares*price: 
            self.amount_spent = self.amount_spent + shares*price; 
            self.stocks[symbol] = self.stocks.get(symbol,0) + shares 
            self.current_money = self.current_money - shares*price;
            self.logTransaction(symbol,shares,price,date,action='buy')
            
        else: 
            if self.verbose:
                print("not enough money in wallet")
                print(f"wallet: {self.current_money}, needed = {shares*price}")
        
    def sell(self,symbol,shares,price,date=None):
        """
        sell #{shares} from symbol at {price} 
        """
        self.stocks[symbol] = self.stocks.get(symbol,0) - shares 
        self.current_money = self.current_money + shares*price;
        self.logTransaction(symbol,shares,price,date,action='sell')

    def step(self,symbol):
        self.buyLogic(symbol)
                
        symbols_and_prices = symbol.groupby(['symbol'],as_index=False)['date'].max()
        symbols_and_prices = symbols_and_prices.merge(symbol,on=['symbol','date'])
        stocks = {int(s):p for i,(s,p) in symbols_and_prices[['symbol','price']].iterrows()}
        
        self.updatePortfolio(stocks)
        self.calculateProfit(stocks)

    def buyLogic(self,symbol):
        """
        decides whether to buy or not
        input: symbol
        """
        pass 

    def sellLogic(self,symbol):
        """
        decides whether to sell or not
        input: symbol
        """
        pass 


