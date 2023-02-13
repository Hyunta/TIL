package arthur.javaground.controller;

import arthur.javaground.domain.Person;
import arthur.javaground.mapper.PersonMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
@Slf4j
public class personController {

    private final PersonMapper personMapper;

    @GetMapping("/people")
    public String findAll() {
        List<Person> all = personMapper.findAll();
        System.out.println("all = " + all);
        return "ok";
    }
}
