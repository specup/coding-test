# (주) 스펙업애드 개발팀 기술 면접 과제

### 문제 1. 장고 및 장고 Admin을 활용하여 다음 기능을 구현하시오
- Django Admin에서 관리자가 사용자 포인트를 적립, 사용할 수 있어야 합니다.
- 모든 유저의 포인트를 띄우는 페이지를 만드세요
    * 포인트: delta의 합계
    * 포인트 사용 횟수: delta가 0 미만인 것들의 개수 (포인트, 포인트 사용 횟수의 계산은 Django ORM을 이용하여 DBMS 내부에서 계산)

#### 페이지 출력 예시
|사용자|포인트|포인트 사용 횟수|
|---|---|---|
|test1|200|0|
|test2|50|2|
|test3|140|1|
|test4|20|0|


#### Model은 아래 조건 대로 구현하시오
UserPointHistory
- created_at: 해당 History가 만들어진 datetime (Django Model 내부 기능을 이용할 것)
- user: 해당 사용자 (django.contrib.auth.model.User)
- delta: 포인트 변화량 (추가, 삭제 량) (ex: -10, +100)
- Many to Many 관계를 이용할 것

### 문제 2. 다음 데이터에 대해 컨텐츠 type별 수익 총액을 구하는 SQL문을 작성하고 Answer2.txt 파일에 기록해주세요.
Table: Content

|id|subject|type|
|---|---|---|
|7011|대기업 취업완성 3개월 종합반|종합반|
|7012|대기업 취업완성 6개월 환급반|환급반|
|7013|대기업 취업완성 6개월 종합반|종합반|

Table: UserContent

|id|username|real_name|content_id|profit|
|---|---|---|---|---|
|1157421|user1|김유신|7011|115000|
|1157422|user2|이순신|7011|115000|
|1157423|user3|김수로|7012|210000|
|1157424|user4|이도|7012|200000|
|1157425|user5|정약용|7011|113000|



#### 제출 방법
github이나 bitbucket private 저장소를 활용하고 jw.lee@specupad.com에 읽기 권한을 부여한 뒤에 이메일로 회신하여주시기 바랍니다.
