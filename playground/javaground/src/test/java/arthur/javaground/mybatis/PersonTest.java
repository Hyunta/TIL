package arthur.javaground.mybatis;


import arthur.javaground.domain.Person;
import arthur.javaground.mapper.PersonMapper;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import javax.annotation.Resource;
import java.util.List;

@SpringBootTest
public class PersonTest {

    @Resource
    PersonMapper personMapper;

    @Test
    void findAll() {
        List<Person> all = personMapper.findAll();
        System.out.println("all = " + all);
    }
}
