from database import get_connection
from collections import Counter

def detect_subscriptions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT description FROM transactions
    WHERE type='expense'
    """)

    descriptions = [row[0] for row in cursor.fetchall()]

    counts = Counter(descriptions)

    subscriptions = []

    for desc, count in counts.items():
        if count >= 3:
            subscriptions.append(desc)

    conn.close()

    return subscriptions