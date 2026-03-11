from database import get_connection

def calculate_health_score():

    conn = get_connection()
    cursor = conn.cursor()

    score = 100

    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type='income'
    """)
    income = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type='expense'
    """)
    expenses = cursor.fetchone()[0] or 0

    savings = income - expenses

    if income > 0:
        savings_rate = (savings / income) * 100
    else:
        savings_rate = 0

    if savings_rate < 10:
        score -= 20

    if expenses > income:
        score -= 30

    if score < 0:
        score = 0

    conn.close()

    return score