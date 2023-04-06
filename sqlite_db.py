import sqlite3 as sq

global db, cur
db = sq.connect('survivors_builds.db')
cur = db.cursor()
async def db_connect() -> None:

    # cur.execute("""CREATE TABLE "sb" (
    # 	"id"	INTEGER NOT NULL,
    # 	"img_perk"	TEXT NOT NULL,
    # 	"perks_addons_list"	TEXT NOT NULL,
    # 	"deskriptions"	TEXT NOT NULL,
    # 	PRIMARY KEY("id" AUTOINCREMENT)
    # );""")

    # cur.execute("""CREATE TABLE "kb" (
	# "id"	INTEGER NOT NULL,
	# "img"	TEXT,
	# "list"	TEXT,
	# "deskription"	TEXT,
	# PRIMARY KEY("id" AUTOINCREMENT)
    # );""")

    # cur.execute("""CREATE TABLE "sos" (
	# "id"	INTEGER NOT NULL,
	# "name"	TEXT NOT NULL,
	# "perk_pic"	TEXT NOT NULL,
	# "descr"	TEXT NOT NULL,
	# PRIMARY KEY("id" AUTOINCREMENT)
    # );""")

    db.commit()

async def art_1():
    art1 = cur.execute("SELECT * FROM art ORDER BY RANDOM() LIMIT 1").fetchall()
    return art1

async def sos_1():
    sos1 = cur.execute("SELECT * FROM sos WHERE id=1").fetchall()
    return sos1

async def sos_2():
    sos2 = cur.execute("SELECT * FROM sos WHERE id=2").fetchall()
    return sos2

async def sos_3():
    sos3 = cur.execute("SELECT * FROM sos WHERE id=3").fetchall()
    return sos3

async def sos_4():
    sos4 = cur.execute("SELECT * FROM sos WHERE id=4").fetchall()
    return sos4

async def sos_5():
    sos5 = cur.execute("SELECT * FROM sos WHERE id=5").fetchall()
    return sos5

async def surv_b1():
    sb1 = cur.execute("SELECT * FROM sb WHERE id=1").fetchall()
    return sb1

async def surv_b2():
    sb2 = cur.execute("SELECT * FROM sb WHERE id=2").fetchall()
    return sb2

async def surv_b3():
    sb3 = cur.execute("SELECT * FROM sb WHERE id=3").fetchall()
    return sb3

async def killer_b1():
    kb1 = cur.execute("SELECT * FROM kb WHERE id=1").fetchall()
    return kb1

async def killer_b2():
    kb2 = cur.execute("SELECT * FROM kb WHERE id=2").fetchall()
    return kb2

async def killer_b3():
    kb3 = cur.execute("SELECT * FROM kb WHERE id=3").fetchall()
    return kb3


#python sqlite_db.py