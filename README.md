# 🔬 Intro
Duck DB의 특성에 대한 이해를 목적으로 python 환경에서 테이블 생성 및 데이터 조회 실습을 진행합니다.

### about Duck DB 
- Duck DB는 in-memory 단계에서 데이터를 관리하는 데이터베이스로, SQLite에 버금가는 빠른 처리 속도를 가지고 있습니다.
- 서버로 구성되는 것이 아닌, local 환경에서 가볍게 구동되는 것이 특징입니다.
- Duck DB는 다양한 데이터소스와 결합할 수 있으며, 클라우드 환경의 AWS S3 스토리지와의 통신도 가능합니다.

### need to know
1. Duck DB와 MySQL의 쿼리는 기본적인 형태는 유사하지만, 지엽적인 부분에서의 차이점들이 상당히 많습니다.
2. python 환경에서 생성한 Duck DB 테이블은 in-memory 환경이 아닌 로컬 환경에 저장됩니다.
3. connection labels을 사용하지 않는 한, Duck DB는 단일 connector만을 지원합니다. Thread를 열거나 복수의 스크립트로 connection을 구성하려면 connection label이 필요하며, 해당 레포지토리에서는 관련 내용에 대해서 다루지 않습니다. 공식 가이드를 참조 부탁드립니다.

### target
- AWS s3 버킷에 저장된 2018.01.01~2023.09.08 기간의 박스오피스(Kobis, Parquet 형식) 데이터를 사용합니다.
- 해당 데이터들을 사용하여 Duck DB 테이블을 생성 및 조회하고 간단한 통계 자료들을 생성합니다.

# 🛠️ Install
### at local
``` bash
$ wget https://github.com/duckdb/duckdb/releases/download/v0.8.1/duckdb_cli-linux-amd64.zip
$ unzip duckdb_cli-linux-amd64.zip
```

### at python (what we use)
``` bash
$ pip install duckdb
```

# 🪧 notice
1. This repository runs in python3.10
2. `/src/create_table` 이하의 모든 스크립트는 AWS s3 접속을 위한 key 정보를 포함하고 있습니다.
해당 레포지토리에서는 AWS와 관련된 내용에 대해서는 다루지 않습니다. 이 점을 참조 부탁드립니다.
또한 config parser와 관련된 내용도 다루지 않습니다.