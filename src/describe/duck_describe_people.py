import duckdb

# DuckDB에 연결
# 절대경로 지정 필요 (이유 불문)
conn = duckdb.connect(database='/home/hooniegit/git/personal/duck_and_boxoffice/database/tmdb', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()
cursor.execute("DESCRIBE tmdb_people")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()