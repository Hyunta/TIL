# Spring Batch

# 소개

> Batch는 일괄처리 라는 뜻을 갖고 있습니다.

큰 데이터를 읽고, 가공하고, 저장한다면 해당 서버는 순식간에 CPU, I/O 등의 자원을 다 써버려서 다른 request를 처리하지 못합니다.

집계기능이 하루에 1번 수행된다면, 이를 위해 API를 구성하는 것은 너무 낭비가 아닐까요?

추가로 데이터가 너무 많아서 처리 중 실패가 나면 어떻게 될까요? 5만번째에서 실패했다면 50001번째부터 실행하면 좋지 않을까요?

또 누군가 아침에 집계한 함수를 다른 누군가 실행시켜서 집계 데이터가 2배가 될 수도 있습니다. 같은 파라미터로 같은 함수를 실행할 때 이미 실행한 경우 실패가 된다면 얼마나 좋을까요?

단발성으로 대용량을 처리하는 어플리케이션을 **배치 어플리케이션**이라고 합니다. 배치 어플리케이션을 구성하기 위해선 비지니스 로직 외에 부가적으로 신경써야할 부분들이 많다는 것을 알 수 있습니다.

웹 어플리케이션을 개발할 때 Spring MVC를 통해서 비지니스 로직에 집중할 수 있는 것 처럼 Spring 진영에서 **Spring Batch** 를 통해서 배치 어플리케이션을 지원합니다.

배치 어플리케이션은

- 대용량 데이터
- 자동화 - 심각한 문제 해결을 제외하고는 사용자 개입 없이 실행되어야 한다.
- 견고성 - 잘못된 데이터를 충돌 / 중단 없이 처리할 수 있어야 한다.
- 신뢰성 - 무엇이 잘못됐는지 추적할 수 있어야 한다. ex)
- 성능 - 지정한 시간 안에 처리를 완료하거나 동시에 실행되는 다른 어플리케이션을 방해하지 않도록 수행되어야 한다.

# 사례

## 일 매출 집계

거래가 자주 발생하는 커머스 사이트는 하루 50만~100만건 정도가 발생합니다. 데이터는 최소 100만에서 200만 row가 생깁니다. 한달이면 5000만~1억건까지가 될수도 있습니다.

실시간 집계 쿼리로 해결하기에는 부하가 너무 심합니다. 전날 Batch를 통해 만들어준 집계 데이터를 바로 전달하면 성능과 부하를 모두 잡을 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68956620-5d25-4286-991c-42855a362d20/Untitled.png)

# 코드

```java
package play.springbatch.job;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.repeat.RepeatStatus;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class SimpleJobConfiguration
{
    private final JobBuilderFactory jobBuilderFactory;
    private final StepBuilderFactory stepBuilderFactory;

    @Bean
    public Job simpleJob()
    {
        return jobBuilderFactory.get("simpleJob")
            .start(simpleStep1())
            .build();
    }

    @Bean
    public Step simpleStep1()
    {
        return stepBuilderFactory.get("simpleStep1")
            .tasklet(((contribution, chunkContext) ->
            {
                log.info(">>>>>>This is Step1");
                return RepeatStatus.FINISHED;
            }))
            .build();
    }
}
```

- SpringBatch의 모든 Job은 `@Configuration` 으로 등록해서 사용합니다.

- jobBuilderFactory, stepBuilderFactory 는 이름을 별도로 지정하지않고 get을 통해 이름을 지정한다.

- .tasklet() 은 step 안에 수행될 기능들을 명시한다.

  Step 안에서 단일로 수행될 커스텀함 기능들을 선언할 때 사용한다.

- Spring Batch에서 Job은 하나의 배치 작업 단위를 말한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14f152fd-4ebb-416a-835b-8ad56f7d0311/Untitled.png)

tasklet과 (reader,processor,writer) 한 묶음은 같은 단위다. 마치 `@Component` 처럼 명확한 역할은 없지만 지정한 커스텀한 기능.

# MySQL 환경에서  Spring Batch 실행해보기

Spring Batch는 어플리케이션 코드 분만 아니라 메타 데이터 테이블들이 필요하다. 메타 데이터란 데이터를 설명하는 데이터다.

Spring Batch의 메타 데이터는

- 이전에 실행한 Job이 어떤 것들이 있는지
- 최근 실패한 Batch Parameter가 어떤 것들이 있고, 성공한 Job은 어떤 것들이 있는지
- 다시 실행한다면 어디서부터 시작하면 될지
- 어떤 Job에 어떤 Step들이 있고, 성공한 것과 실패한 것은 어떤 것들이 있는지

등등 Batch 어플리케이션을 운영하기 위한 메타데이터가 여러 테이블에 분산되어 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/192bc438-6f53-4dce-a89e-3a36c57b4320/Untitled.png)

H2 DB는 Spring Boot가 자동으로 생성해주지만, 다른 DB는 개발자가 직접 생성해야한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4fc75186-e845-4084-9ada-463a1b2c0d1d/Untitled.png)

`schema-mysql.sql` 을 이용해서 메타데이터 테이블을 생성해주면 된다.

# 메타데이터 테이블 개요

[소개](https://jojoldu.tistory.com/326?category=902551)

Job Parameter 마다 Job Instance가 생성되고 만약 Job Parameter가 같다면 새로 생성하지 않는다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31be4eda-53bc-45a4-94bd-1c9900f83ec7/Untitled.png)

만약 생성한적이 있다면 아래처럼 예외를 반환한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/614006bc-5909-4c53-b3ea-0c313f5331bb/Untitled.png)

참고글:

https://jojoldu.tistory.com/324