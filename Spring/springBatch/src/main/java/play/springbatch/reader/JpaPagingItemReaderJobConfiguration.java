package play.springbatch.reader;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.JobBuilderFactory;
import org.springframework.batch.core.configuration.annotation.StepBuilderFactory;
import org.springframework.batch.item.ItemWriter;
import org.springframework.batch.item.database.JpaPagingItemReader;
import org.springframework.batch.item.database.builder.JpaPagingItemReaderBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import play.springbatch.entity.Pay;

import javax.persistence.EntityManagerFactory;

@Slf4j
@RequiredArgsConstructor
@Configuration
public class JpaPagingItemReaderJobConfiguration
{
    private final JobBuilderFactory jobBuilderFactory;
    private final StepBuilderFactory stepBuilderFactory;
    private final EntityManagerFactory entityManagerFactory;

    private static final int CHUNK_SIZE = 10;

    @Bean
    public Job jpaPagingItemReaderJob()
    {
        return jobBuilderFactory.get("jpaPagingItemReaderJob")
            .start(jpaPagingItemReaderStep())
            .build();
    }

    @Bean
    public Step jpaPagingItemReaderStep()
    {
        return stepBuilderFactory.get("jpaPagingItemReaderStep")
            .<Pay, Pay>chunk(CHUNK_SIZE)
            .reader(jpaPagingItemReader())
            .writer(jpaPagingItemWriter())
            .build();
    }

    @Bean
    public JpaPagingItemReader<Pay> jpaPagingItemReader()
    {
        return new JpaPagingItemReaderBuilder<Pay>()
            .name("jpaPagingItemReader")
            .entityManagerFactory(entityManagerFactory)
            .pageSize(CHUNK_SIZE)
            .queryString("SELECT p FROM Pay p WHERE amount >= 2000")
            .build();
    }

    private ItemWriter<Pay> jpaPagingItemWriter()
    {
        return list ->
        {
            for (Pay pay : list)
            {
                log.info("Current Pay = {}", pay);
            }
        };
    }

}
