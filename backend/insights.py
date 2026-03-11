from database import get_connection

def budget_warnings():
    conn = get_connection()
    cursor = conn.cursor()

    warnings = []

    cursor.execute("SELECT * FROM budgets")
    budgets = cursor.fetchall()

    for budget in budgets:

        cursor.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE category=? AND type='expense'
        """,(budget["category"],))

        spent = cursor.fetchone()[0] or 0

        if spent >= 0.85 * budget["limit_amount"]:
            warnings.append(
                f"Warning: {budget['category']} budget almost reached"
            )

    conn.close()
    return warnings

    def spending_alerts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type='expense'
    """)
    total = cursor.fetchone()[0] or 0

    if total > 5000:
        return ["High spending detected this month"]

    return []