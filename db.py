import sqlite3

def save_offer(funpay:str,g2g:str='G2G',status:str='Active'):
    """
    Active / Disactive
    """

    with sqlite3.connect("game.db") as conn:
        cur = conn.cursor()
        sql = 'INSERT INTO game VALUES (?, ?, ?)'
        params = (funpay,g2g,status)
        cur.execute(sql,params)
        conn.commit()

def get_active_offer():

    with sqlite3.connect("game.db") as conn:
        
        cur = conn.cursor()

        sql = 'SELECT * FROM game WHERE status=Active'
        offers = cur.execute(sql).fetchall()

    return offers
def set_disactive(funpay:str):

   with sqlite3.connect("game.db") as conn:

        cur = conn.cursor()
        sql = 'Update game set status = Disactive where id = ?'
        cur.execute(sql,(funpay,))
        conn.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("game.db")
    with sqlite3.connect("game.db") as conn:

        cur = conn.cursor()
        cur.execute("CREATE TABLE game (funpay TEXT, g2g TEXT, status TEXT)")

        # cur.save_offer("https://funpay.com/lots/offer?id=25790923")
