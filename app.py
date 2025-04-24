from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Read data from CSV file
def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # First row is the header
        rows = list(reader)     # Remaining rows are the data
    return headers, rows

@app.route("/", methods=["GET", "POST"])
def index():
    # Load data from the CSV file
    headers, rows = read_csv("data.csv")
    
    # Check if a button was clicked to show popup
    selected_row = None
    if request.method == "POST":
        # Get the row details from the form
        row_index = int(request.form.get("row_index"))
        selected_row = rows[row_index]
    
    # Pass 'zip' to the template
    return render_template("layout.html", headers=headers, rows=rows, selected_row=selected_row, zip=zip)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)