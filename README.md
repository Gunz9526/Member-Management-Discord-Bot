# Member-Management-Discord-Bot

## 프로젝트 소개
소속 인원 및 블랙리스트 관리를 위한 서비스 입니다. 멀티쓰레드를 활용하여 flask, discord bot을 동시에 실행합니다. 

## 개발 기간 
- 2024.06 ~ 

## 개발환경
- **Version** : Python 3.11.9
- **IDE** : VSCode
- **Framework** : Flask,
- **Package** : Discord.py, Discord.Extension, flask-restx, Flask-SQLAlchemy, Flask-JWT-Extended, pymysql
- **ORM** : SQLAlchemy

## 기술 스택
- **Server** : AWS EC2, Gunicorn
- **DataBase** : AWS RDS, Mysql
- 

## 프로젝트 아키텍쳐
![프로젝트 아키텍쳐](https://github.com/Gunz9526/Member-Management-Discord-Bot/blob/main/img/ERD.JPG)

## 주요 기능
- Discord Command를 통해 DB에 인원 추가 및 조회
- 랜덤한 조합의 문장으로 route -> 링크 중복 방지, 인증 최소화, 유저가 접속함과 동시에 링크 만료로 비허가 유저 접속 불가
- JWT를 이용한 세션 관리.
- Discord 계정의 닉네임, ID, 고유ID 저장 -> 작업한 유저 특정 가능

- 관리자 명령어를 통해 dicord Cog모듈 로드 여부 관리
- 관리자 페이지에서 상기한 모든 기능과 사용자들의 작업 내역 조회 및 복구, 데이터 훼손 유저 식별
      
## ✒️ API
- API 상세설명 : 


- API 명세서 : 
