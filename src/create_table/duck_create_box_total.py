import duckdb
from configparser import ConfigParser

# config.ini 읽기
parser = ConfigParser()
parser.read("config/config.ini")
s3_access = parser.get("AWS", "S3_ACCESS")
s3_secret = parser.get("AWS", "S3_SECRET")

# DuckDB에 연결
# 절대경로 지정 필요 (이유 불문)
conn = duckdb.connect(database='/home/hooniegit/git/personal/duck_and_boxoffice/database/memory', read_only=False)  

# 쿼리 실행
cursor = conn.cursor()

# 테이블 생성
# s3 디렉토리의 하위 디렉토리를 wildcard로 지정 가능
# 단, 2겹 이상의 tree 구조를 가지고 있을 경우 중간 디렉토리에 wildcard 명시 필요
cursor.execute("install httpfs")
cursor.execute("load httpfs")
cursor.execute("set s3_region='ap-northeast-2'")
cursor.execute(f"set s3_access_key_id='{s3_access}'")
cursor.execute(f"set s3_secret_access_key='{s3_secret}'")
cursor.execute("""
               CREATE TABLE box_whole
               AS
               SELECT *
               FROM read_parquet('s3://sms-warehouse/merged_kobis/*/*')""")

# 데이터 타입 확인
cursor.execute("SELECT * FROM box_whole")
cursor.execute("DESCRIBE box_whole")

# 결과 가져오기
result = cursor.fetchall()
print(result)

# 연결 종료
conn.close()