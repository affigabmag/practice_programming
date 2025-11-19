#   - Starts with a dictionary stocks mapping 4 ticker symbols to prices.                                                                                                                                                  
#   - Prompt the user for a ticker (or set a variable).                                                                                                                                                                    
#   - If it exists, add 5 to its price and print the updated value; otherwise print “Ticker not found.”   

stocks={
    'teva':24.34,
    'aapl':257.4,
    'tsla':445.445,
    'nvda':196.6
}

ticker=input("enter a ticker:")
err=''
for stock in stocks:
    if stock==ticker:
        stocks[stock]=stocks.get(stock)+5
        print(stocks[stock])
        err=''
        break
    else:
        err="ticker not found"

if err!="":
    print(err)

        