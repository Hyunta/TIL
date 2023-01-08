# Vertica DB

MySQL 행 기반의 데이터베이스로 대용량 데이터를 저장하기에는 한계가 있다. 이를 극복하기 위해서 Vertica DB를 사용하고 있다. 2019년 11월 기준 데이터 1억 9천만건으로 한계 도래. 2020년도 초 EP 상품 수가 4억, 5억건으로 증가할 전망

=> Vertica DB 테스트 진행

→ DB 의 장점 ( 원부관리 용이 )

→ 처리속도 매우 빠름 ( select, insert, update, delete )

→ 신규컬럼추가시 영향도 없음

→ Master-Slave 구조가 아닌 클러스터 구조이기에 동기화 지연이 없음

# 컬럼형 DB는 왜 빠른가?

[컬럼형 DB는 왜 빠른가](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=52606)

전통적인 데이터 저장구조로는 이것을 처리하는 데 한계점에 다다르자, 매우 빠르게 분석할 수 있는 DBMS인 컬럼형 DB가 출시됐다.

| 구분 | Row 기반 DBMS     | Column 기반 DBMS |
| ---- | ----------------- | ---------------- |
| 특징 | - Row 단위로 저장 |                  |

- 하나의 디스크에 여러 레코드가 저장되는 구조 | - Column 단위로 저장
- 컬럼별로 파일이 생성되고 디스크 페이지에는 동일한 컬럼 값들이 연속됨 | | 트랜잭션 특성 | 레코드 단위로 추가, 수정, 삭제에 적합 | 동일한 컬럼에 대해 대량으로 데이터를 처리할 때 적합 | | 압축 효율 | 레코드는 중복이 없이 고유하므로 압축 효율이 상대적으로 낮음 | 컬럼값마다 중복된 값이 많으므로 압축 효율이 매우 높음 | | SQL 패턴 | SELECT * FROM TABLE | SELECT AVG(COL1) FROM TABLE | | 적용 DBMS | RDBMS(MySQL, Oracle etc) | VerticaDB |

컬럼형 DB는 Update를 지양하고, Delete → Insert를 지향한다.

(어차피 Update를 해도, Delete + Insert로 나간다고함 추후 확인 필요)