순환 참조가 발생한다.

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c43c94a8-5d9f-4995-b4bc-ff3ba29473d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230216T091146Z&X-Amz-Expires=86400&X-Amz-Signature=bb75be132e778f45581beeb22eb3e307536a88099831e900fc6b95bef7f64e25&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

Properties 클래스에 `@ConstructorBinding` 을 추가하고, Configuration에 `@EnablleConfigurationProperties(KafkaProducerProperties.class)` 를 추가해서 해결했다.

```kotlin
package arthur.catalogservice;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

@RequiredArgsConstructor
@Configuration
@Slf4j
@EnableConfigurationProperties(KafkaProducerProperties.class)
public class KafkaConfiguration {

    private final KafkaProducerProperties kafkaProducerProperties;

    @Bean
    public String init() {
        List<String> bootstrapServers = kafkaProducerProperties.getBootstrapServers();
        String acks = kafkaProducerProperties.getAcks();
        String linger = kafkaProducerProperties.getLinger();
        String retries = kafkaProducerProperties.getRetries();
        String backoff = kafkaProducerProperties.getBackoff();

        log.info("bootstrapServers={}", bootstrapServers);
        log.info("acks={}", acks);
        log.info("linger={}", linger);
        log.info("retries={}", retries);
        log.info("backoff={}", backoff);
        return retries;
    }
}
package arthur.catalogservice;

import lombok.Getter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.ConstructorBinding;

import java.util.List;

@Getter
@ConstructorBinding
@ConfigurationProperties("kafka.producer")
public class KafkaProducerProperties {
    private final List<String> bootstrapServers;
    private final String acks;
    private final String linger;
    private final String retries;
    private final String backoff;

    public KafkaProducerProperties(List<String> bootstrapServers, String acks, String linger, String retries, String backoff) {
        this.bootstrapServers = bootstrapServers;
        this.acks = acks;
        this.linger = linger;
        this.retries = retries;
        this.backoff = backoff;
    }
}
```