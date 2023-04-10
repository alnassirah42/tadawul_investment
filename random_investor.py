from investor import Investor


class randomInvestor(Investor):
    def __init__(self,name,init_deposit):
        super().__init__(name,init_deposit)
        
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

    # def step(self,symbol):
    #     self.buyLogic(symbol)
    #     stocks = symbol[symbol['date']==symbol.date.max()].iloc[0]
    #     stocks = {stocks['symbol'] : stocks['price']}
    #     self.updatePortfolio(stocks)
    #     self.calculateProfit(stocks)
