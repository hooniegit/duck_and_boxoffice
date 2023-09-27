import duckdb

# DuckDB에 연결
# 절대경로 지정 필요 (이유 불문)
conn = duckdb.connect(database='/home/hooniegit/git/personal/duck_and_boxoffice/database/memory', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()
cursor.execute("""
               SELECT *
               FROM box_seoul
               WHERE EXTRACT(DOW FROM CAST(SUBSTRING(date FROM 1 FOR 4) || '-' || SUBSTRING(date FROM 6 FOR 2) || '-' || SUBSTRING(date FROM 9 FOR 2) AS DATE)) IN (6, 0);
               """)

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()