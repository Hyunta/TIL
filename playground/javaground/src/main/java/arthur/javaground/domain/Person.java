package arthur.javaground.domain;

import lombok.Getter;
import lombok.ToString;

//@Getter
@ToString
public class Person {
    private long seq;
    private String name;
    private String nickname;
    private Integer age;
}
