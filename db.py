import sqlite3

def save_offer(funpay:str,g2g:str='G2G',status:str='Active'):
    """
    Active / Disactive
    """
    offers = get_active_offer()
    for offer in offers:
        if offer[0] == funpay:
            return

    with sqlite3.connect("game.db") as conn:
        cur = conn.cursor()
        sql = 'INSERT INTO game VALUES (?, ?, ?)'
        params = (funpay,g2g,status)
        cur.execute(sql,params)
        conn.commit()

def get_users():
    with sqlite3.connect("game.db") as conn:
        cur = conn.cursor()

        sql = 'SELECT user FROM users'
        users=cur.execute(sql).fetchall()

        return users
        
def save_user(nickname:str):
    users = get_users()
    for user in users:
        if user[0]==nickname:
            return

    with sqlite3.connect("game.db") as conn:
        cur = conn.cursor()

        sql = 'INSERT INTO users(user) VALUES (?)'
        params = (nickname,)
        cur.execute(sql,params)

        conn.commit()



def get_active_offer():
    offers = []

    with sqlite3.connect("game.db") as conn:
        
        cur = conn.cursor()

        sql = 'SELECT * FROM game WHERE status=?'
        offers=cur.execute(sql,('Active',)).fetchall()

        # offers = cur.fetchall()

    return offers
def set_disactive(funpay:str):

   with sqlite3.connect("game.db") as conn:

        cur = conn.cursor()
        sql = 'UPDATE game SET status = ? WHERE funpay = ?'
        cur.execute(sql,('Disactive',funpay))
        conn.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("game.db")
    # with sqlite3.connect("game.db") as conn:

    #     cur = conn.cursor()
    #     try:
    #         cur.execute("CREATE TABLE game (funpay TEXT, g2g TEXT, status TEXT)")
    #     except sqlite3.OperationalError:
    #         print("Exists game")

    #     try:
    #         cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT , user TEXT)")
    #     except sqlite3.OperationalError:
    #         print("Exists user")
        
    #     save_user('rnamont')

    with sqlite3.connect("game.db") as conn:

        cur = conn.cursor()    
        cur.execute("DELETE FROM users WHERE id=0;")