# ########################################################################################################################
# # Pymysql 을 사용한 연결설정 및 커넥션 얻어오기 & query
import pymysql

class CRUD:
    def insert(self, items):
        conn = pymysql.connect(host='localhost', user='root', password='stark1234',
                               db='webdb', charset='utf8')
        # Connection 으로부터 Cursor 생성
        curs = conn.cursor()

        for item in items:
            # SQL문 실행
            sql = "INSERT IGNORE INTO customer VALUES ('%s', '%s', '%s')"
            sql = sql % (item[0], item[1], item[2])
            print(sql, type(sql))

            # 아래는 원하는 대로 동작하지 않음 (because item.__str__ 혹은 __repr__ 는 특수문자(따옴표) 등을 이스케이프 문자가 포함된 문자열로 표현한다.)
            # 따라서 SQL 문장 자체가 INSERT IGNORE INTO customer VALUES '(\\'hi\\', \\'hello\\', \\'aa\\')' 의 형태로 변한다.

            # sql = "INSERT IGNORE INTO customer VALUES %s"
            # sql = sql % item.__str__

            try:
                curs.execute(sql)
            except Exception as e:
                print(e)

        conn.commit() # 항상 commit 잊지 말자 : commit 이 수행되어야 transection 당 데이터베이스 변경사항이 적용 완료 된다.

        # Connection 닫기
        conn.close()
        return

    def __init__(self):
        pass














    # def __init__(self, items=[]):
        # print("생성자 호출")
        # self.items = items
        # print(self.items)
    #
    # 이런식으로 되야된다는 것인가????
    # connection , vo.CRUD(connection) <- class VO(CRUD가 포함된 MODEL을 상속)


    # DAO VO Connection pool 작동원리 및 구현??? 시간나면...