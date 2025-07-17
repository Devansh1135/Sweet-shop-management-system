from flask import Flask, render_template, request, redirect, url_for, flash
from sweet_shop import SweetShop

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

shop = SweetShop()

@app.route("/")
def index():
    sweets = shop.get_all_sweets()
    return render_template("index.html", sweets=sweets)

@app.route("/add", methods=["POST"])
def add_sweet():
    try:
        id = int(request.form["id"])
        name = request.form["name"]
        category = request.form["category"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])

        shop.add_sweet(id, name, category, price, quantity)
        flash("Sweet added successfully!", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete_sweet():
    try:
        id = int(request.form["id"])
        if shop.delete_sweet(id):
            flash(f"Sweet with id {id} deleted.", "success")
        else:
            flash(f"Sweet with id {id} not found.", "warning")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("index"))

@app.route("/purchase", methods=["POST"])
def purchase_sweet():
    try:
        id = int(request.form["id"])
        quantity = int(request.form["quantity"])
        shop.purchase_sweet(id, quantity)
        flash(f"Purchased {quantity} units.", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("index"))

@app.route("/restock", methods=["POST"])
def restock_sweet():
    try:
        id = int(request.form["id"])
        quantity = int(request.form["quantity"])
        shop.restock_sweet(id, quantity)
        flash(f"Restocked {quantity} units.", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("index"))

@app.route("/search", methods=["GET"])
def search_sweet():
    # Get search params; only one is used at a time
    search_id = request.args.get("search_id")
    search_name = request.args.get("search_name")
    search_category = request.args.get("search_category")

    result = None

    if search_id:
        try:
            sid = int(search_id)
            result = shop.search_sweet_by_id(sid)
        except:
            flash("Invalid ID entered.", "danger")
    elif search_name:
        result = shop.search_sweet_by_name(search_name)
    elif search_category:
        result = shop.search_sweet_by_category(search_category)

    if not result:
        flash("No sweets found matching the criteria.", "warning")
        return redirect(url_for("index"))

    # Show results page with single sweet or multiple sweets? Your method returns one sweet by category, 
    # so for category search maybe change it to return list? For now, just show one.
    return render_template("index.html", sweets=[result])

@app.route("/sort")
def sort_sweets():
    order = request.args.get("order", "asc")
    reverse = (order == "desc")
    sweets = shop.sort_sweets_by_price(reverse=reverse)
    return render_template("index.html", sweets=sweets)

if __name__ == "__main__":
    app.run(debug=True)
