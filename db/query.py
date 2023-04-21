import sqlite3

# conn = sqlite3.connect('db/db.db')

# c = conn.cursor()

# c.execute("SELECT pin FROM accounts WHERE fullName = 'Sid Venkatayogi'")
# # c.fetchone()
# # c.fetchmany()
# print(c.fetchone())

# conn.commit()
# conn.close()
def getBalance(acc):

    conn = sqlite3.connect('db/db.db')

    c = conn.cursor()

    c.execute("SELECT totalBalance FROM accounts WHERE accID = ?", (acc))
    return(c.fetchone()[0])


    conn.commit()
    conn.close()

def depositdb(amount, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("UPDATE accounts SET totalBalance = totalbalance + ? WHERE accID = ?",(amount, acc))

    conn.commit()
    conn.close()