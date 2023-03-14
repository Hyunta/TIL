

```mysql
select *
from A left join B B2 on A.a = B2.a
where A.b <> B2.b;
```

A와 B에 a,b 필드가 있고 join을 해서 b 값을 비교한다고 가정합니다.

| table | a(int) | b(varchar(10)) |
| ----- | ------ | -------------- |
| A     | 1      | null           |
| B     | 1      | 'abc'          |

저는 <>를 통해서  null과 'abc'는 다르다고 나올 줄 알았는데 아무 값도 나오지 않는다.

mysql에서 null은 기본적으로 false로 취급하기 때문에 나오지 않는다.