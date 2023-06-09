"""
list of user defined investing strategies 

list of available investors: 
    1. lucky   : invests every month at the lowest price date
    2. unlucky : invests every month at the highest price date
    3. som     : invests every month at the beginning of the month 
    4. random  : invests every month at random date
    
    
    1. fixedAmountLucky   : invests every month at the lowest price date
    2. fixedAmountUnlucky : invests every month at the highest price date
    3. fixedAmountSom     : invests every month at the beginning of the month 
    4. fixedAmountRandom  : invests every month at random date

"""


from investor import Investor

class luckyInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['price'] == symbol['price'].min()].iloc[0]
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

#     def step(self,symbol):
#         self.buyLogic(symbol)
        
#         stocks = symbol[symbol['date']==symbol.date.max()].iloc[0]
#         stocks = {stocks['symbol'] : stocks['price']}
        
#         symbols_max_date = symbol.groupby(['symbol'],as_index=False)['date'].max()
#         symbols_max_date = symbols_max_date.merge(symbol,on=['symbol','date'])
#         stocks = {s:p for i,(s,p) in df.iloc[:5][['symbol','price']].iterrows()}
#         self.updatePortfolio(stocks)
#         self.calculateProfit(stocks)

class unluckyInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['price'] == symbol['price'].max()].iloc[0]
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class randomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class somInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['date'] == symbol['date'].min()].iloc[0]
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountLuckyInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['price'] == symbol['price'].min()].iloc[0]
        shares = stock_amount//buy_at['price']
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

#     def step(self,symbol):
#         self.buyLogic(symbol)
        
#         stocks = symbol[symbol['date']==symbol.date.max()].iloc[0]
#         stocks = {stocks['symbol'] : stocks['price']}
        
#         symbols_max_date = symbol.groupby(['symbol'],as_index=False)['date'].max()
#         symbols_max_date = symbols_max_date.merge(symbol,on=['symbol','date'])
#         stocks = {s:p for i,(s,p) in df.iloc[:5][['symbol','price']].iterrows()}
#         self.updatePortfolio(stocks)
#         self.calculateProfit(stocks)

class fixedAmountUnluckyInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['price'] == symbol['price'].max()].iloc[0]
        shares = stock_amount//buy_at['price']
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountRandomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]
        shares = stock_amount//buy_at['price']
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountRandomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]
        shares = stock_amount//buy_at['price']
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountRandomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]
        shares = stock_amount//buy_at['price']
        if shares < 1:
            return 
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountRandomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]
        shares = stock_amount//buy_at['price']
        if shares < 1:
            return 
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountSomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['date'] == symbol['date'].min()].iloc[0]
        shares = stock_amount//buy_at['price']
        if shares < 1:
            return 
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

class fixedAmountRandomInvestor(Investor):
    def __init__(self,name,init_deposit,verbose):
        super().__init__(name,init_deposit,verbose)
        
    def buyLogic(self,symbol,shares,stock_amount):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol.sample().iloc[0]

        shares = stock_amount//buy_at['price']
        if shares < 1:
            return 
        self.buy(buy_at['symbol'],
                 shares, # shares
                 buy_at['price'],
                 buy_at['date'])

