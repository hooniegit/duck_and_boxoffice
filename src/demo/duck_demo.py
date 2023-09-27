import duckdb
from configparser import ConfigParser

# config.ini 읽기
parser = ConfigParser()
parser.read("config/config.ini")
s3_access = parser.get("AWS", "S3_ACCESS")
s3_secret = parser.get("AWS", "S3_SECRET")

# DuckDB에 연결
conn = duckdb.connect(database='memory', read_only=False)  

# 쿼리 실행
# s3 버킷에 위치한 TMDB 영화 데이터들을 테이블로 생성하는 데모입니다.
cursor = conn.cursor()
cursor.execute("install httpfs")
cursor.execute("load httpfs")
cursor.execute("set s3_region='ap-northeast-2'")
cursor.execute(f"set s3_access_key_id='{s3_access}'")
cursor.execute(f"set s3_secret_access_key='{s3_secret}'")
cursor.execute("""
               CREATE TABLE t1
               AS
               SELECT *
               FROM read_parquet('s3://sms-warehouse/merged_TMDB/part-*')""")
cursor.execute("SELECT * FROM t1 WHERE id = 299534")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()