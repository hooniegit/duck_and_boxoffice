import duckdb, os

# database 절대 경로 반환
current_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(current_dir, f'../../database/tmdb')

# DuckDB에 연결
conn = duckdb.connect(database=database_dir, read_only=False)  
cursor = conn.cursor()

# 쿼리 실행 - cast 목록 반환
cursor.execute(f'''
            SELECT 
                id, original_title, overview, posters,
                backdrop_path, release_date, "cast", crew,
                belongs_to_collection, budget, production_companies, production_countries,
                revenue, runtime
            FROM 
                tmdb_movie
            WHERE 
                id = 872585;
            ''')

# 결과 가져오기
result_all = cursor.fetchall()[0]

# 데이터 1차 가공
movie_id = result_all[0]
movie_nm = result_all[1]
movie_dt = result_all[2]
poster = result_all[3]
external_image = result_all[4]
date = result_all[5]
cast_list = result_all[6]
crew_list = result_all[7]
belongs_to_collection = result_all[8]
budget = result_all[9]
production_companies = result_all[10]
production_countries = result_all[11]
revenue = result_all[12]
runtime = result_all[13]

# 쿼리 실행 - people 목록 반환
result_set = tuple(id for id in cast_list)
cursor.execute(f'''
                SELECT *
                FROM tmdb_people
                WHERE id IN {str(result_set)};
                ''')

# 결과 가져오기
result_people = cursor.fetchall()

# 쿼리 실행 - column 목록 반환
cursor.execute(f'''
                SELECT column_name
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE table_name = 'tmdb_people';
                ''')

# 결과 가져오기
result_columns = cursor.fetchall()
column_list = [column[0] for column in result_columns]

# 연결 종료
conn.close()

column_list = ['id', 'date_gte', 'name', 'known_for_department', 'profile_img', 'birth', 'death', 'year']

# people dict를 담은 리스트 생성
result_list = []
for people in result_people:
    result_dict = {i : val for i, val in zip(column_list, people)}
    result_list.append(result_dict)

# 테스트
print(movie_id)
print(movie_nm)
print(result_people)
print(column_list)
print(result_list)  
