from investor import Investor


class luckyInvestor(Investor):
    def __init__(self,name,init_deposit):
        super().__init__(name,init_deposit)
        
    def buyLogic(self,symbol):
        """
        the price of symbol for a whole month, 
        lucky investor will always pick the day with the lowest price
        """
        buy_at = symbol[symbol['price'] == symbol['price'].min()].iloc[0]
        self.buy(buy_at['symbol'],
                 30, # shares
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
