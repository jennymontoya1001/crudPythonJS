import eel
import sys
import pymysql
import os

sys.path.append("..")
eel.init("front")


@eel.expose
def showPython():
    conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='restaurant'
            )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER")
    result = cursor.fetchone();
    result = cursor.fetchall();
    print(result)
    conn.commit()
    conn.close()
    return result

@eel.expose
def registerPython(documento,nombre,lastname,username,password):
    conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='restaurant'
            )
    cursor = conn.cursor()

    sql = "INSERT INTO USER (ID,NAME,LASTNAME,USERNAME,PASSWORD) VALUES ('{}','{}','{}','{}','{}')".format(documento,nombre,lastname,username,password)
    #print(f"{documento,nombre,lastname,username,password}")

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    print("Data inserted")
    conn.close()






eel.start("index.html",size=(400,500))