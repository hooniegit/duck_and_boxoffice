import duckdb

# DuckDB에 연결
conn = duckdb.connect(database='memory', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()
cursor.execute("DESCRIBE box_total")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()