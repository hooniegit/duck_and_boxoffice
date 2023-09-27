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
cursor = conn.cursor()

# 테이블 생성 : 서울
cursor.execute("install httpfs")
cursor.execute("load httpfs")
cursor.execute("set s3_region='ap-northeast-2'")
cursor.execute(f"set s3_access_key_id='{s3_access}'")
cursor.execute(f"set s3_secret_access_key='{s3_secret}'")
cursor.execute("""
               CREATE TABLE box_seoul 
               AS 
               SELECT * 
               FROM read_parquet('s3://sms-warehouse/merged_kobis/loc_code=0105001/*')
               """)

# 데이터 타입 확인
cursor.execute("SELECT * FROM box_seoul")
cursor.execute("DESCRIBE box_seoul")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()