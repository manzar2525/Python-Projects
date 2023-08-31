import sqlite3




def updateMaster():
    pass
def updateStore():
    pass

def insertIntoMaster(firstName,lastName,email,password):

    cur.execute("INSERT INTO master VALUES(?,?,?,?)",(firstName, lastName,email,password))
    conn.commit()


def insertIntoStore(userID,account,userName,password):

    cur.execute("INSERT INTO store VALUES(?,?,?,?)",(userID,account,userName,password))
    conn.commit()


def fetchfromMaster(userName):
    #fetching master account password for the entered username
    row=cur.execute("SELECT username, password FROM master WHERE username=?",(userName,)).fetchone()
    #conn.commit()
    return row

def fetchfromStore(userName):
    #fetching stored credentials from the vault
    rows=cur.execute("SELECT userID, account, username, password FROM store WHERE userID=?",(userName,)).fetchall()
    #conn.commit()

    return rows


def updateMaster(password,userName):
    cur.execute('UPDATE master SET password=?  WHERE username=? ',( password,userName))
    conn.commit()

    

def updateStore():
    
    pass

conn=sqlite3.connect("passwordManager.db")
if conn==None:
    print("Connection not established with the db")

else:
    
    cur=conn.cursor()
    try:
        cur.execute("CREATE Table IF NOT EXISTS master(fname TEXT,lname TEXT,username TEXT,password TEXT)" )
    except:
        print("Error creating the master table")
    try:
        cur.execute("CREATE Table IF NOT EXISTS store(userID TEXT, account TEXT,username TEXT,password TEXT)" )
    except:
        print("Error creating the store table")

