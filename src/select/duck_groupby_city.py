import duckdb

# DuckDB에 연결
conn = duckdb.connect(database='memory', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()
cursor.execute("""
SELECT loc_code, SUM(audi_cnt)
FROM box_whole
WHERE CAST(SUBSTRING(date FROM 1 FOR 4) AS INTEGER) = 2023
GROUP BY loc_code
ORDER BY loc_code ASC
""")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()