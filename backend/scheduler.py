from database import get_connection
from datetime import date

def run_scheduler():

    conn = get_connection()
    cursor = conn.cursor()

    today = str(date.today())

    cursor.execute("""
    SELECT * FROM scheduled_transactions
    WHERE scheduled_date<=? AND executed=0
    """,(today,))

    rows = cursor.fetchall()

    for row in rows:

        cursor.execute("""
        INSERT INTO transactions(type,amount,category,description,date)
        VALUES(?,?,?,?,?)
        """,(
            row["type"],
            row["amount"],
            row["category"],
            row["description"],
            today
        ))

        cursor.execute("""
        UPDATE scheduled_transactions
        SET executed=1 WHERE id=?
        """,(row["id"],))

    conn.commit()
    conn.close()