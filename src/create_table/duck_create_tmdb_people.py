import duckdb
from configparser import ConfigParser

# config.ini 파일 읽기
parser = ConfigParser()
parser.read("config/config.ini")
s3_access = parser.get("AWS", "S3_ACCESS")
s3_secret = parser.get("AWS", "S3_SECRET")

# DuckDB에 연결
# 절대경로 지정 필요 (이유 불문)
conn = duckdb.connect(database='/home/hooniegit/git/personal/duck_and_boxoffice/database/tmdb', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()

# 테이블 생성 : 2023년 1월, 서울
cursor.execute("install httpfs")
cursor.execute("load httpfs")
cursor.execute("set s3_region='ap-northeast-2'")
cursor.execute(f"set s3_access_key_id='{s3_access}'")
cursor.execute(f"set s3_secret_access_key='{s3_secret}'")
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tmdb_people
               AS 
               SELECT * 
               FROM read_parquet('s3://sms-warehouse/TMDB_people/*/*.parquet')
               """)

# print("finished : TABLE CREATE")

# 데이터 타입 확인
cursor.execute("DESCRIBE tmdb_people")

print("finished : EXECUTION")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()