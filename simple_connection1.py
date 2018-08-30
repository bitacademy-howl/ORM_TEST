# ########################################################################################################################
# # Pymysql 을 사용한 연결설정 및 커넥션 얻어오기 & query
import pymysql

def simple_connection1():
    conn = pymysql.connect(host='localhost', user='root', password='stark1234',
                           db='webdb', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    sqls = []
    sqls.append("INSERT IGNORE INTO customer VALUES ('김정수', '남', '서울')")
    sqls.append("INSERT IGNORE INTO customer VALUES ('이삐', '남', '춘천')")
    sqls.append("INSERT IGNORE INTO customer VALUES ('강수정', '여', '경기')")
    sqls.append("INSERT IGNORE INTO customer VALUES ('김머시기', '여', '경기')")
    sqls.append("INSERT IGNORE INTO customer VALUES ('X', '남', '경기')")
    sqls.append("INSERT IGNORE INTO customer VALUES ('이희웅', '남', '동두천')")

    try:
        for sql in sqls:
            curs.execute(sql)
        conn.commit()

    except Exception as e:
        print(e)

    sql = "select * from customer"
    curs.execute(sql)
    #
    # 데이타 Fetch
    rows = curs.fetchall()
    print(rows)     # 전체 rows

    # Connection 닫기
    conn.close()