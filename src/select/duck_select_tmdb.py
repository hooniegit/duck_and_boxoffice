import duckdb

# DuckDB에 연결
# 절대경로 지정 필요 (이유 불문)
conn = duckdb.connect(database='/home/hooniegit/git/personal/duck_and_boxoffice/database/tmdb', read_only=False)  

# 쿼리 실행
# 기본 : 리스트 []
# 인덱스 : 튜플 () => row 개수 만큼 생성
cursor = conn.cursor()
cursor.execute("""
               SELECT *
               FROM tmdb_movie
               WHERE id = 872585;
               """)

# 결과 가져오기
result = cursor.fetchall()[0]
print(result)

# 연결 종료
conn.close()

"""
SELECT 
    id, cast, crew, posters, backdrop_path, belongs_to_collection, budget, 
    genres, original_title, overview, poster_path, production_companies, 
    production_countries, release_date, runtime, revenue
FROM tmdb_movie
WHERE
    movie_id = {}
"""


"""

    context = {
        'movie_id' : movie_id, # id
        'movie_nm' : movie_nm, # original_title
        'movie_dt' : movie_dt, # overview
        'poster' : url_poster, # posters
        'external_image' : url_backdrop, # backdrop_path
        'date' : date, # release_date
        'cast' : cast_pages, # "cast"
        'crew' : crew_pages, # crew
        'belongs_to_collection' : belongs_to_collection, # belongs_to_collection
        'budget' : budget, # budget
        'production_companies' : production_companies, # production_companies
        'production_countries' : production_countries, # productuon_countries
        'revenue' : revenue, # revenue
        'runtime' : runtime # runtime
    } 

"""