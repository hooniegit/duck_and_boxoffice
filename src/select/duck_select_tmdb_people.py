import duckdb, os

# database 절대 경로 반환
current_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(current_dir, f'../../database/tmdb')

# DuckDB에 연결
conn = duckdb.connect(database=database_dir, read_only=False)  

# 쿼리 실행 - cast 목록 반환
cursor = conn.cursor()
cursor.execute('''
               SELECT "cast"
               FROM tmdb_movie
               WHERE id = 872585;
               ''')

# 결과 가져오기
result_cast_list = cursor.fetchall()[0]
print(result_cast_list)


cursor.execute('''
               SELECT *
               FROM tmdb_people
               WHERE id = 3;
               ''')

# 결과 가져오기
result_cast = cursor.fetchall()[0]
print(result_cast)


# 연결 종료
conn.close()
