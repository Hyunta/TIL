# Spring Batch Job Flow

Spring Batch의 Job을 구성하는데는 Step이 있습니다.

Step은 실제 Batch 작업을 수행하는 역할을 합니다.

이전에 작성한 코드를 보시면 Job은 코드가 거의 없죠?

실제로 비지니스 로직을 처리하는 기능은 Step에 구현되어 있습니다.

Step은 Batch로 실제 처리하고자 하는 기능과 설정을 모두 포함하는 장소

Batch 처리 내용을 담다보니, Job 내부의 Step들간의 순서 혹은 처리 흐름을 제어할 필요가 있습니다.

어떻게 제어하는지 알아봅시다.

## Next

순차적으로 Step을 연결시킬 때 사용한다.

step1 → step2 → step3으로 진행할 때 next를 사용할 수 있다.

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
@Configuration
@RequiredArgsConstructor
public class StepNextJobConfiguration
{
    private final JobBuilderFactory jobBuilderFactory;
    private final StepBuilderFactory stepBuilderFactory;

    @Bean
    public Job stepNextJob()
    {
        return jobBuilderFactory.get("stepNextJob")
            .start(step1())
            .next(step2())
            .next(step3())
            .build();
    }

    @Bean
    public Step step1()
    {
        return stepBuilderFactory.get("step1")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is Step1");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step step2()
    {
        return stepBuilderFactory.get("step2")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is Step2");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step step3()
    {
        return stepBuilderFactory.get("step3")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is Step3");
                return RepeatStatus.FINISHED;
            })
            .build();
    }
}
```

하지만 새롭게 생성한 stepNextJob 말고도 simpleJob이 실행되는 문제가 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c2481e81-236b-44a6-8005-38940792ba40/Untitled.png)

application.yml에 해당 조건을 추가해주면, Spring Batch 실행시 Program Argument로 job.name이 넘어오면 해당 값과 일치하는 Job만 실행하겠다는 것이다. 만약 job.name이 없으면 NONE을 할당하겠다는 의미다. NONE이 할당되면 어떤 배치도 실행시키지 않겠다는 말이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75ba796f-d9af-423e-b153-a9f82ca2e4ee/Untitled.png)

해당 설정을 통해 지정한 Job만 실행할 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d6509296-b6e3-40c8-a214-f973c56d3195/Untitled.png)

## Flow - 조건별 흐름 제어

앞선 예제는 선행 Step이 실행되지 않을 경우 이후 Step이 전부 실행되지 않습니다.

만약 정상일 때는 Step2로, 비정상일 경우에는 Step3로 수행해야한다면 어떻게 할까요?

```java
package play.springbatch.job;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.batch.core.ExitStatus;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.repeat.RepeatStatus;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Slf4j
@Configuration
@RequiredArgsConstructor
public class StepNextConditionalJobConfiguration
{
    private final JobBuilderFactory jobBuilderFactory;
    private final StepBuilderFactory stepBuilderFactory;

    @Bean
    public Job stepNextConditionalJob()
    {
        return jobBuilderFactory.get("stepNextConditionalJob")
            .start(conditionalJobStep1())
            .on("FAILED")
            .to(conditionalJobStep3())
            .on("*")
            .end()
            .from(conditionalJobStep1())
            .on("*")
            .to(conditionalJobStep2())
            .next(conditionalJobStep3())
            .on("*")
            .end()
            .end()
            .build();
    }

    @Bean
    public Step conditionalJobStep1()
    {
        return stepBuilderFactory.get("step1")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is stepNextConditionalJob Step1");

                /**
                 ExitStatus를 FAILED로 지정한다.
                 해당 status를 보고 flow가 진행된다.
                 **/
                contribution.setExitStatus(ExitStatus.FAILED);

                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step conditionalJobStep2()
    {
        return stepBuilderFactory.get("conditionalJobStep2")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is stepNextConditionalJob Step2");
                return RepeatStatus.FINISHED;
            })
            .build();
    }

    @Bean
    public Step conditionalJobStep3()
    {
        return stepBuilderFactory.get("conditionalJobStep3")
            .tasklet((contribution, chunkContext) ->
            {
                log.info(">>>>> This is stepNextConditionalJob Step3");
                return RepeatStatus.FINISHED;
            })
            .build();
    }
}
```

해당 코드를 실행시키면 Step1에서 실패가 발생했을 경우 Step3가 실행되기 때문에 Step2가 실행되지 않는 것을 확인할 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1680521-ae2d-4bdf-beab-02e3bec10bb6/Untitled.png)