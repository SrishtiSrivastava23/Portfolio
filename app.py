from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

CSV_FILE = "contact_data.csv"

# Create the CSV with headers if it doesn't exist

if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Message"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Append data to the existing CSV file
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, email, message])

    print(f"Saved to CSV: {name} ({email}) - {message}")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
