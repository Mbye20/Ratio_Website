
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from fin_ratios import Liquidity_ratios, leverage_ratios, efficiency_ratios, profitability_ratios, market_value_ratios
import sqlite3

app = Flask(__name__)

RATIOS = [
    "Liquidity Ratios",
    "Leverage Ratios",
    "Efficiency Ratios",
    "Profitability Ratios",
    "Market Value Ratios"
]


float_converter=lambda x: {i:float(x[i]) for i in x}

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
        form = float_converter(request.form)
        components = Liquidity_ratios(**form)
        try:
            LIQUIDITY_RATIOS = {
                    "current_ratio": f"{components.current_ratio():.2f}",
                    "acid_test_ratio": f"{components.acid_test_ratio():.2f}",
                    "cash_ratio": f"{components.cash_ratio():.2f}",
                    "operating_cash_flow_ratio" : f"{components.operating_cash_flow_ratio():.2f}",
            }
        except ValueError:
            LIQUIDITY_RATIOS = {
                    "current_ratio": components.current_ratio(),
                    "acid_test_ratio": components.acid_test_ratio(),
                    "cash_ratio": components.cash_ratio(),
                    "operating_cash_flow_ratio" : components.operating_cash_flow_ratio(),
            }
        return render_template("/liquidity_results.html", **LIQUIDITY_RATIOS)
    
            
@app.route("/leverage_ratios", methods = ["GET", "POST"])
def leverage():
    if request.method == "POST":
        form = float_converter(request.form)
        components = leverage_ratios(**form)
        try:
            LEVERAGE_RATIOS = {
            "debt_ratio": f"{components.debt_ratio():.2f}",
            "debt_to_equity_ratio" : f"{components.debt_to_equity_ratio():.2f}",
            "interest_coverage_ratio": f"{components.interest_coverage_ratio():.2f}",
            "debt_service_coverage_ratio": f"{components.debt_service_coverage_ratio():.2f}",


            }
        
        except ValueError:
            LEVERAGE_RATIOS = {
            "debt_ratio": components.debt_ratio(),
            "debt_to_equity_ratio" : components.debt_to_equity_ratio(),
            "interest_coverage_ratio": components.interest_coverage_ratio(),
            "debt_service_coverage_ratio": components.debt_service_coverage_ratio(),
            }

        return render_template("/leverage_results.html", **LEVERAGE_RATIOS )


@app.route("/efficiency_ratios", methods = ["GET", "POST"])
def efficiency():
    if request.method == "POST":
        form = float_converter(request.form)
        components = efficiency_ratios(**form)
        try:
            EFFICIENCY_RATIOS = {
            "asset_turnover_ratio": f"{components.asset_turnover_ratio():.2f} times",
            "inventory_turnover_ratio": f"{components.inventory_turnover_ratio():.2f} times",
            "receivables_turnover_ratio": f"{components.receivables_turnover_ratio():.2f} times",
            "days_sales_in_inventory_ratio": f"{components.days_sales_in_inventory_ratio():.2f} days",


        }
        except ValueError:
            EFFICIENCY_RATIOS = {
            "asset_turnover_ratio": components.asset_turnover_ratio(),
            "inventory_turnover_ratio": components.inventory_turnover_ratio(),
            "receivables_turnover_ratio": components.receivables_turnover_ratio(),
            "days_sales_in_inventory_ratio": components.days_sales_in_inventory_ratio(),

        }        
        
        return render_template("/efficiency_results.html", **EFFICIENCY_RATIOS)


@app.route("/profitability_ratios", methods = ["GET", "POST"])
def profitability():
    if request.method == "POST":
        form = float_converter(request.form)
        components = profitability_ratios(**form)
        try:
            PROFITABILITY_RATIOS = {
            "gross_margin_ratio": f"{components.gross_margin_ratio():.2f}%",
            "operating_margin_ratio": f"{components.operating_margin_ratio():.2f}%",
            "net_profit_margin": f"{components.net_profit_margin():.2f}%",
            "return_on_assets_ratio": f"{components.return_on_assets_ratio():.2f}%",
            "return_on_equity_ratio": f"{components.return_on_equity_ratio():.2f}%",

            }
        except ValueError:
            PROFITABILITY_RATIOS = {
                "gross_margin_ratio": components.gross_margin_ratio(),
                "operating_margin_ratio": components.operating_margin_ratio(),
                "net_profit_margin": components.net_profit_margin(),
                "return_on_assets_ratio": components.return_on_assets_ratio(),
                "return_on_equity_ratio": components.return_on_equity_ratio(),

                }      
        

        return render_template("/profitability_results.html", **PROFITABILITY_RATIOS)


@app.route("/marketvalue_ratios", methods = ["GET", "POST"])
def marketvalue():
    if request.method == "POST":
        form = float_converter(request.form)
        components = market_value_ratios(**form)
        try:
            MARKETVALUE_RATIOS = {
            "book_value_per_share_ratio": f"{components.book_value_per_share_ratio():.2f}",
            "dividend_yield_ratio": f"{components.dividend_yield_ratio():.2f}%",
            "earnings_per_share_ratio": f"{components.earnings_per_share_ratio():.2f}",
            "price_earning_ratio": f"{components.price_earning_ratio():.2f}",

            }
        except ValueError:
            MARKETVALUE_RATIOS = {
            "book_value_per_share_ratio": components.book_value_per_share_ratio(),
            "dividend_yield_ratio": components.dividend_yield_ratio(),
            "earnings_per_share_ratio": components.earnings_per_share_ratio(),
            "price_earning_ratio": components.price_earning_ratio(),
            }


        
        return render_template("/marketvalue_results.html", **MARKETVALUE_RATIOS)


if __name__ == "__main__":
    app.run(debug=True)