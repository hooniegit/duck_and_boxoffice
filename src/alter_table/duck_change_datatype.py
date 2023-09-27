import duckdb

# DuckDB에 연결
conn = duckdb.connect(database='memory', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()

# 데이터 타입 확인
cursor.execute("DESCRIBE box_whole")

# 데이터 타입 변환
# seoul_202301 / box_seoul / box_total
cursor.execute("ALTER TABLE box_whole ALTER sales_amount TYPE BIGINT")
cursor.execute("ALTER TABLE box_whole ALTER sales_share TYPE DOUBLE")
cursor.execute("ALTER TABLE box_whole ALTER sales_inten TYPE BIGINT")
cursor.execute("ALTER TABLE box_whole ALTER sales_change TYPE BIGINT")
cursor.execute("ALTER TABLE box_whole ALTER sales_acc TYPE BIGINT") 
cursor.execute("ALTER TABLE box_whole ALTER audi_cnt TYPE INTEGER") 
cursor.execute("ALTER TABLE box_whole ALTER audi_inten TYPE DOUBLE")
cursor.execute("ALTER TABLE box_whole ALTER audi_acc TYPE INTEGER")
cursor.execute("ALTER TABLE box_whole ALTER audi_cnt TYPE INTEGER")
cursor.execute("ALTER TABLE box_whole ALTER scrn_cnt TYPE INTEGER")
cursor.execute("ALTER TABLE box_whole ALTER show_cnt TYPE INTEGER")

# 변환 결과 확인
cursor.execute("DESCRIBE box_whole")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()