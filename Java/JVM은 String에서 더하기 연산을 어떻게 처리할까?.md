## 자바에서 String을 어떻게 관리하지?
`.java` 파일을 컴파일 할 때 클래스 파일을 분리해서 `.class` 파일을 받는데 그 안에 `constant pool`이 있다.
```java
public class ConstantPool {
    public void printHello() {
        String hello = "Hello";
        System.out.println(hello);
    }
}

```
사용되는 상수들은 `constant pool` 에 저장되어, JVM이 필요에 의해 사용한다.

```java
String string = "string";
String string2 = "string";

//동등 
string.equals(string2);
//동일
string == string2;
```
두 객체가 할당된 메모리 주소가 같으면 **동일**하고,
두 객체의 내용이 같으면 **동등**하다고 말한다.

---

## String + 연산의 작동원리
JDK 5 이전에는 String + 연산시 String 객체가 생성됐습니다. 따라서 + 갯수만큼 객체가 필요했었죠.
```java
String string1 = "a";
String string2 = "b";
String string3 = "c";

System.out.println(string1 + string2 + string3);
```
작동을 시키면 `string1+string2` 을 하면서 중간단계를 객체로 만들고, 한번더 `객체+string3` 을 해서 비효율적이었습니다.

---

**JDK 5부터는 컴파일시 `StringBuilder` 혹은 `StringBuffer`로 변환되도록 변경됐습니다.**
![](https://images.velog.io/images/mohai2618/post/9e1ef5fc-8042-4e30-8c8a-5066e2afa46b/image.png)

`StringBuilder`를 이용하면 문자열에 +를 했을 때 보다 객체 생성비용이 줄어듭니다. 하지만 루프 같은 상황에서는 `StringBuilder`가 계속해서 생기게 됩니다.

```java
String string1 = "a";
for (int i = 0; i < 1000; i++) {
	string1 += i;
}
System.out.println(string1);
```
해당 메서드를 실행시키면 `StringBuilder` 객체가 계속해서 생성됩니다.

---

**JDK 9부터는 이를 개선하고자 StringConcatFactory를 도입했습니다.**

해당 메서드를 실행시킨 바이트코드를 살펴보면 아래와 같이 `StringConcatFactory`가 호출되는 것을 볼 수 있습니다.
```java
 INVOKEDYNAMIC makeConcatWithConstants(Ljava/lang/String;I)Ljava/lang/String; [
      // handle kind 0x6 : INVOKESTATIC
      java/lang/invoke/StringConcatFactory.makeConcatWithConstants(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;
      // arguments:
      "\u0001\u0001"
    ]
```

#### JDK가 알아서 효율적으로 작동하지만, 의존하기보다는 StringBuilder를 코드에 작성하여 효율적인 상황이 보인다면 사전에 방지하는 것이 좋습니다.





#### Reference:
https://www.baeldung.com/jvm-constant-pool
https://docs.oracle.com/javase/8/docs/api/index.html
https://docs.oracle.com/javase/9/docs/api/java/lang/invoke/StringConcatFactory.html
https://jerry92k.tistory.com/50