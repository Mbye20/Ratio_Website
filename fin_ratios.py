
class Liquidity_ratios:

    def __init__(self, current_assets, current_liabilities, cash_and_cash_equivalent, inventories, operating_cash_flow):
        self.current_assets = current_assets
        self.current_liabilities = current_liabilities 
        self.cash_and_cash_equivalent = cash_and_cash_equivalent
        self.inventories = inventories
        self.operating_cash_flow = operating_cash_flow

    def current_ratio(self):
        return self.current_assets / self.current_liabilities
    def acid_test_ratio(self):
        return (self.current_assets - self.inventories) / self.current_liabilities
    def cash_ratio(self):
        return self.cash_and_cash_equivalent / self.current_liabilities
    def operating_cash_flow_ratio(self):
        return self.operating_cash_flow/ self.current_liabilities

class leverage_ratios:
    def __init__(self, total_assets, total_liabilities, shareholders_equity,
     operating_income, interest_expenses, total_debt_service):
        self.total_assets = total_assets
        self.total_liabilities = total_liabilities
        self.shareholders_equity = shareholders_equity
        self.operating_income = operating_income
        self.interest_expenses = interest_expenses
        self.total_debt_service =total_debt_service
    
    def debt_ratio(self):
        return self.total_liabilities/ self.total_assets
    def debt_to_equity_ratio(self):
        return self.total_liabilities/ self.shareholders_equity
    def interest_coverage_ratio(self):
        return self.operating_income / self.interest_expenses
    def debt_service_coverage_ratio(self):
        return self.operating_income/ self.total_debt_service

class efficiency_ratios:
    def __init__(self, net_sales, average_total_assets, cost_of_good_sold,
     average_inventory, net_credit_sales, average_accounts_receivable):
        self.net_sales = net_sales
        self.average_total_assets = average_total_assets
        self.cost_of_good_sold = cost_of_good_sold
        self.average_inventory = average_inventory
        self.net_credit_sales =net_credit_sales
        self.average_accounts_receivable = average_accounts_receivable

    def asset_turnover_ratio(self):
        return self.net_sales/ self.average_total_assets
    def inventory_turn_over_ratio(self):
        return self.cost_of_good_sold / self.average_inventory
    def receivables_turnover_ratio(self):
        return self.net_credit_sales/ self.average_accounts_receivable
    def days_sales_in_inventory_ratio(self):
        return 365 / (self.cost_of_good_sold / self.average_inventory)


class profitability_ratios:
    def __init__(self, gross_profit, net_sales, operating_income, net_income, total_assets, shareholders_equity):
        self.gross_profit = gross_profit
        self.net_sales = net_sales
        self.operating_income = operating_income
        self.net_income = net_income
        self.total_assets = total_assets
        self.shareholders_equity = shareholders_equity

    def gross_margin_ratio(self):
        return (self.gross_profit / self.net_sales) * 100
    def operating_margin_ratio(self):
        return (self.operating_income / self.net_sales) * 100 
    def net_profit_margin(self):
        return (self.net_income / self.net_sales) * 100
    def return_on_assets_ratio(self):
        return (self.net_income/ self.total_assets) * 100
    def return_on_equity_ratio(self):
        return (self.net_income/ self.shareholders_equity) * 100

class market_value_ratios:
    def __init__(self, shareholders_equity, preferred_equity, total_common_shares_outstanding, 
    dividend_per_share, share_price, net_income):
        self.shareholders_equity = shareholders_equity                
        self.preferred_equity = preferred_equity
        self.total_common_shares_outstanding = total_common_shares_outstanding
        self.dividend_per_share = dividend_per_share
        self.share_price = share_price
        self.net_income = net_income

    def book_value_per_share_ratio(self):
        return (self.shareholders_equity - self.preferred_equity) / self.total_common_shares_outstanding
    def dividend_yield_ratio(self):
        return self.dividend_per_share / self.share_price
    def earnings_per_share_ratio(self):
        return self.net_income / self.total_common_shares_outstanding
    def price_earning_ratio(self):
        return self.share_price / ( self.net_income / self.total_common_shares_outstanding)
            
    
    
    
        

    
        
        
        

