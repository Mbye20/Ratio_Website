import sys
from flask import Flask, render_template, request, redirect
sys.path.append(".")
from ratio.fin_ratios import Liquidity_ratios, leverage_ratios, efficiency_ratios, profitability_ratios, market_value_ratios
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
    





app.run(debug=True)