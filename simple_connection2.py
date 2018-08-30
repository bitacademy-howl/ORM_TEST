# ########################################################################################################################
# # Pymysql 을 사용한 연결설정 및 커넥션 얻어오기 & query
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='stark1234',
                       db='webdb', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sqls = []

sql = "INSERT IGNORE INTO customer VALUES ('%s', '%s', '%s')"

sqls.append(sql % ('이삐', '남', '춘천'))
sqls.append(sql % ('김머시기', '여', '경기'))
sqls.append(sql % ('X', '남', '경기'))
sqls.append(sql % ('이희웅', '남', '동두천'))

try:
    for sql in sqls:
        print(sql)
        curs.execute(sql)
    conn.commit() # insert 는 항상 commit 잊지 말자 시발...

except Exception as e:
    print(e)

sql = "select * from customer"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)

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