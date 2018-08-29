# ########################################################################################################################
# # Pymysql 을 사용한 연결설정 및 커넥션 얻어오기 & query
# import pymysql
from builtins import Exception

import pymysql

# MySQL Connection 연결
from pymysql import IntegrityError
from pymysql.constants.ER import REQUIRES_PRIMARY_KEY
from pymysql.err import raise_mysql_exception

conn = pymysql.connect(host='localhost', user='root', password='stark1234',
                       db='webdb', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
# sql = "DESC customer"
# qq = curs.execute(sql)
# print(qq)

# sql = "CREATE TABLE pyths (name VARCHAR(30), gender CHAR(10), city VARCHAR(30));"
# curs.execute(sql)

# sql = "INSERT INTO pyths VALUES ('김정수', '남', '서울')"
# curs.execute(sql)
# conn.commit()

# sql = "INSERT INTO pyths VALUES ('김정수', '남', '서울')"
# curs.execute(sql)



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
    conn.commit() # insert 는 항상 commit 잊지 말자 시발...

except Exception as e:
    print(e)

sql = "select * from customer"
curs.execute(sql)
#
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows

# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

# Connection 닫기
conn.close()


#





# """
# pymysql은 python에서 mysql 연동을 위한 라이브러리 입니다.
# 해당 코드는 pymysql을 이용하여 CRUD하는 간단한 예시입니다.
# """
# import pymysql
#
# # MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='root', password='stark1234', db='webdb', charset='utf8', )
# curs = conn.cursor(pymysql.cursors.DictCursor)
#
# # curs.execute("create table webtoonCommends (name VARCHAR(30), gender CHAR(10), city VARCHAR(30))")
#
# # ==== select example ====
# sql = "select * from webtoonCommends"
# curs.execute(sql)
#
# # 데이타 Fetch
# rows = curs.fetchall()
# print(rows)
#
# # ==== insert example ====
# sql = """insert into webtoonCommends(name,gender,city)
#          values (%s, %s, %s)"""
# curs.execute(sql, ('홍길동', '남', '서울'))
# curs.execute(sql, ('이연수', '여', '서울'))
# conn.commit()
#
# # ==== update OR delete example ====
# # sql = """update webtoonCommends
# #          set region = '서울특별시'
# #          where region = '서울'"""
# # curs.execute(sql)
#
# # sql = "delete from webtoonCommends where id=%s"
# # curs.execute(sql, 6)
#
# conn.commit()