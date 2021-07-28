### 목표:

- 기본적인 쿼리문법을 익힌다.
- SQL 문의 다양한 활용방법

```mysql
SELECT 컬럼 FROM 테이블 [WHERE 조건식]
GROUP BY 그룹화할 컬럼 [HAVING 조건식] ORDER BY 컬럼1 [, 컬럼2, 컬럼3 ...];
```

### 기본적인 문법 순서

```mysql
SELECT [Column] FROM [Table] WHERE [Condition] GROUP BY [Grouped Column] HAVING [Condition] ORDER BY [Column1],[Column2],[Column3];
```



### Select문:

- Count(NAME):
  - NAME 컬럼에 있는 값들의 갯수를 구한다.
  - GroupBy와 같이 쓰인다.
- IfNull(NAME [Column 명] , 'No name'):
  - NAME 컬럼에서 null값을 갖는 데이터를 'No name' 으로 변경해준다.
- IF(조건문,참일때의 값, 거짓일 때의 값) :
  - IF (SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%', 'O', 'X')
  - 참일 때는 'O'로 표시, 거짓일 때는 'X'로 표시
- DISTINCT:
  - 중복을 제거한 값을 가져온다
  - SELECT COUNT(DISTINCT NAME)
  - NAME 컬럼에서 종류가 몇개인지 알 수 있다.
- DATE_FORMAT:
  - DATE_FORMAT(DATETIME, '%Y-%m-%d')
  - 위 같은 방법으로 날짜 표시방법을 변경할 수 있다.

### Where문:

- WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(HOST_ID) > 1)
  - IN에 조건을 주어서 리스트로 받아온 다음에 조건 추가 가능

프로그래머스 SQL문제 푸는데 필요한 개념들은 이정도인듯 하다.
위 내용 외에 더 기초적인 내용들을 머리에서 생각해서 하면 얼추 풀 수 있다.