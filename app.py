import sys
from flask import Flask, render_template, request, redirect
sys.path.append(".")
from fin_ratios import Liquidity_ratios, leverage_ratios, efficiency_ratios, profitability_ratios, market_value_ratios
app = Flask(__name__)

RATIOS = [
    "Liquidity Ratios",
    "Leverage Ratios",
    "Efficiency Ratios",
    "Profitability Ratios",
    "Market Value Ratios"
]


@app.route("/")
def index():
    return render_template("/index.html", ratios = RATIOS)


@app.route("/inputvalues", methods = ["GET","POST"])
def calculate():
    if request.method == "POST":
        ratio = request.form.get("ratios")
        if ratio == RATIOS[0]:
            return render_template("/liquidity.html")
        elif ratio == RATIOS[1]:
            return render_template("/leverage.html")
        elif ratio == RATIOS[2]:
            return render_template("/efficiency.html")
        elif ratio == RATIOS[3]:  
            return render_template("/profitability.html")
        elif ratio == RATIOS[4]: 
            return render_template("/marketvalue.html")
        else:
            if not ratio:
                return render_template("/index.html", ratios = RATIOS, message = "No Ratio Type Selected")
            if ratio not in RATIOS:
                return render_template("/index.html", ratios = RATIOS, message = "Invalid Ratio")


@app.route("/liquidity_ratios", methods = ["GET", "POST"])
def liquidity():
    if request.method == "POST":
        current_assets = float(request.form.get("current_assets"))
        current_liabilities = float(request.form.get("current_liabilities"))
        cash_and_cash_equivalent = float(request.form.get("cash_and_cash_equivalent"))
        inventories = float(request.form.get("inventories"))
        operating_cash_flow = float(request.form.get("operating_cash_flow"))

        components = Liquidity_ratios(current_assets, current_liabilities, cash_and_cash_equivalent, inventories, operating_cash_flow)
        
        current_ratio = f"{components.current_ratio():.2f}"
        acid_test_ratio = f"{components.acid_test_ratio():.2f}"
        cash_ratio = f"{components.cash_ratio():.2f}"
        operating_cash_flow_ratio = f"{components.operating_cash_flow_ratio():.2f}"

        return render_template("/liquidity_results.html", current_ratio = current_ratio, acid_test_ratio = acid_test_ratio, cash_ratio = cash_ratio, operating_cash_flow_ratio = operating_cash_flow_ratio)
    
@app.route("/leverage_ratios", methods = ["GET", "POST"])
def leverage():
    if request.method == "POST":
        total_assets = float(request.form.get("total_assets"))
        total_liabilities = float(request.form.get("total_liabilities"))
        operating_income = float(request.form.get("operating_income"))
        shareholders_equity = float(request.form.get("shareholders_equity"))
        interest_expenses = float(request.form.get("interest_expenses"))
        total_debt_service = float(request.form.get("total_debt_service"))


        components = leverage_ratios(total_assets, total_liabilities, shareholders_equity, operating_income, interest_expenses, total_debt_service)
        
        debt_ratio = f"{components.debt_ratio():.2f}"
        debt_to_equity_ratio = f"{components.debt_to_equity_ratio():.2f}"
        interest_coverage_ratio = f"{components.interest_coverage_ratio():.2f}"
        debt_service_coverage_ratio = f"{components.debt_service_coverage_ratio():.2f}"

        return render_template("/leverage_results.html", debt_ratio = debt_ratio, debt_to_equity_ratio = debt_to_equity_ratio, interest_coverage_ratio = interest_coverage_ratio, debt_service_coverage_ratio = debt_service_coverage_ratio )


@app.route("/efficiency_ratios", methods = ["GET", "POST"])
def efficiency():
    if request.method == "POST":
        net_sales = float(request.form.get("net_sales"))
        average_total_assets = float(request.form.get("average_total_assets"))
        cost_of_good_sold = float(request.form.get("cost_of_good_sold"))
        average_inventory = float(request.form.get("average_inventory"))
        net_credit_sales = float(request.form.get("net_credit_sales"))
        average_accounts_receivable = float(request.form.get("average_accounts_receivable"))


        components = efficiency_ratios(net_sales, average_total_assets, cost_of_good_sold,average_inventory, net_credit_sales, average_accounts_receivable)
        
        asset_turnover_ratio = f"{components.asset_turnover_ratio():.2f} times"
        inventory_turnover_ratio = f"{components.inventory_turnover_ratio():.2f} times"
        receivables_turnover_ratio = f"{components.receivables_turnover_ratio():.2f} times"
        days_sales_in_inventory_ratio = f"{components.days_sales_in_inventory_ratio():.2f} days"

        return render_template("/efficiency_results.html", asset_turnover_ratio = asset_turnover_ratio, inventory_turnover_ratio =inventory_turnover_ratio, receivables_turnover_ratio = receivables_turnover_ratio, days_sales_in_inventory_ratio = days_sales_in_inventory_ratio )


@app.route("/profitability_ratios", methods = ["GET", "POST"])
def profitability():
    if request.method == "POST":
        gross_profit = float(request.form.get("gross_profit"))
        net_sales = float(request.form.get("net_sales"))
        operating_income = float(request.form.get("operating_income"))
        net_income = float(request.form.get("net_income"))
        total_assets = float(request.form.get("total_assets"))
        shareholders_equity = float(request.form.get("shareholders_equity"))


        components = profitability_ratios(gross_profit, net_sales, operating_income, net_income, total_assets, shareholders_equity)
        
        gross_margin_ratio = f"{components.gross_margin_ratio():.2f}%"
        operating_margin_ratio = f"{components.operating_margin_ratio():.2f}%"
        net_profit_margin = f"{components.net_profit_margin():.2f}%"
        return_on_assets_ratio = f"{components.return_on_assets_ratio():.2f}%"
        return_on_equity_ratio = f"{components.return_on_equity_ratio():.2f}%"


        return render_template("/profitability_results.html", gross_margin_ratio = gross_margin_ratio, operating_margin_ratio = operating_margin_ratio, net_profit_margin = net_profit_margin, return_on_assets_ratio =return_on_assets_ratio, return_on_equity_ratio = return_on_equity_ratio )


@app.route("/marketvalue_ratios", methods = ["GET", "POST"])
def marketvalue():
    if request.method == "POST":
        shareholders_equity = float(request.form.get("shareholders_equity"))
        preferred_equity = float(request.form.get("preferred_equity"))
        total_common_shares_outstanding = float(request.form.get("total_common_shares_outstanding"))
        dividend_per_share = float(request.form.get("dividend_per_share"))
        share_price = float(request.form.get("share_price"))
        net_income = float(request.form.get("net_income"))


        components = market_value_ratios(shareholders_equity, preferred_equity, total_common_shares_outstanding, dividend_per_share, share_price, net_income)
        
        book_value_per_share_ratio = f"{components.book_value_per_share_ratio():.2f}"
        dividend_yield_ratio = f"{components.dividend_yield_ratio():.2f}%"
        earnings_per_share_ratio = f"{components.earnings_per_share_ratio():.2f}"
        price_earning_ratio = f"{components.price_earning_ratio():.2f}"

        return render_template("/marketvalue_results.html", book_value_per_share_ratio = book_value_per_share_ratio, dividend_yield_ratio = dividend_yield_ratio, earnings_per_share_ratio = earnings_per_share_ratio, price_earning_ratio = price_earning_ratio)




app.run(debug=True)