from flask import Flask, request, jsonify
from flask_cors import CORS

from database import init_db, get_connection
from insights import budget_warnings
from health_score import calculate_health_score
from subscription_detector import detect_subscriptions
from scheduler import run_scheduler

app = Flask(__name__)
CORS(app)

init_db()

@app.route("/add_transaction", methods=["POST"])
def add_transaction():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions(type,amount,category,description,date)
    VALUES(?,?,?,?,?)
    """,(
        data["type"],
        data["amount"],
        data["category"],
        data["description"],
        data["date"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"status":"success"})


@app.route("/health")
def health():

    score = calculate_health_score()

    return jsonify({"score":score})


@app.route("/warnings")
def warnings():

    return jsonify(budget_warnings())


@app.route("/subscriptions")
def subscriptions():

    return jsonify(detect_subscriptions())


if __name__ == "__main__":
    run_scheduler()
    app.run(debug=True)