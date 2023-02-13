# Colima 삽질 일지

- 수웅님이 올리신 PR의 테스트가 실행되지 않아서 해결하는 과정을 정리해봤습니다.



Docker를 띄워놓고 테스트를 실행했는데 Container는 올라가는데 S3 클래스가 생성되지 않는 것을 확인했습니다.

![image-20230208124539826](/Users/we/Library/Application Support/typora-user-images/image-20230208124539826.png)

```java
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'amazonS3': Invocation of init method failed; nested exception is com.amazonaws.SdkClientException: Unable to load region information from any provider in the chain
```

진행하는 과정 중에 Docker가 이제 유료화가 되어 Colima를 통해 진행해야한다고 들어서, Colima를 설치하고 다시 테스트를 돌려봤습니다. 예상했지만 여전히 Test가 실행이 되지 않았습니다.

![image-20230208125112442](/Users/we/Library/Application Support/typora-user-images/image-20230208125112442.png)

로그를 들여다보니 해당 부분부터 Token is not supported 라는 문구가 나오면서 연결을 재시도하다가 실패하는 것을 확인할 수 있었습니다.



`Unable to load region information from any provider in the chain`  문구를 찾아보았습니다. 



---

도저히 해결되지 않았었는데 문제는 빈등록에 있었다.

S3Config에서 설정한 테스트용 빈이 적절하게 등록되지 않아서 문제가 발생했다.

source에서 사용하는 S3 빈이 아니라, LocalStackS3Config에서 설정한 빈 주입이 필요했다.

기존에 `@Extension(SpringExtenstion.class)` 부분을 제거하고 SpringBootTes로 대체했더니 해결됐다.