import sqlite3

# conn = sqlite3.connect('db/db.db')

# c = conn.cursor()

# c.execute("SELECT pin FROM accounts WHERE fullName = 'Sid Venkatayogi'")
# # c.fetchone()
# # c.fetchmany()
# print(c.fetchone())

# conn.commit()
# conn.close()

def getAcc(name, pin):
    conn = sqlite3.connect('db/db.db')

    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE fullName = ? AND pin = ?",(str(name), int(pin)))
    result = c.fetchone()
    if result != None:
        return (result)
    return False

def createAcc(name, pin, email, deposit):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("INSERT INTO accounts (fullName, pin, email, totalBalance) VALUES (?, ?, ?, ?)", (str(name), int(pin), str(email), int(deposit)))

    conn.commit()
    conn.close()
def closeAcc(acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("DELETE FROM accounts WHERE accID = ?",(int(acc),))

    conn.commit()
    conn.close()

def getBalance(acc):

    conn = sqlite3.connect('db/db.db')

    c = conn.cursor()
    c.execute("SELECT totalBalance FROM accounts WHERE accID = ?", (int(acc),))
    return(c.fetchone()[0])

    conn.commit()
    conn.close()

def deposit(amount, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("UPDATE accounts SET totalBalance = totalbalance + ? WHERE accID = ?",(amount, acc))

    conn.commit()
    conn.close()

def withdraw(amount, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()
    c.execute("SELECT totalBalance FROM accounts WHERE accID = ?", (int(acc),))
    balance = c.fetchone()[0]
    if (balance >= amount):
        c.execute("UPDATE accounts SET totalBalance = totalbalance - ? WHERE accID = ?",(amount, acc))
        print(f"\nSUCCESSFULLY WITHDREW ${amount}!")
    else:
        print("\n*INSUFFICIENT FUNDS*")
        c.execute("UPDATE accounts SET totalBalance = totalbalance - ? WHERE accID = ?",(balance, acc))
        print(f"SUCCESSFULLY WITHDREW ${balance}")


    conn.commit()
    conn.close()

def editName(newName, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("UPDATE accounts SET fullName = ? WHERE accID = ?",(newName, acc))

    conn.commit()
    conn.close()

def editEmail(newEmail, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("UPDATE accounts SET email = ? WHERE accID = ?",(newEmail, acc))
    
    conn.commit()
    conn.close()

def editPin(newPin, acc):
    conn = sqlite3.connect('db/db.db')
    c = conn.cursor()

    c.execute("UPDATE accounts SET pin = ? WHERE accID = ?",(newPin, acc))
    
    conn.commit()
    conn.close()
