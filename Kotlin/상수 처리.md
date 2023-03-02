# 상수 처리하는 방법, Companion Object

# 학습 동기

상수 선언을 할 때 `companion object` 블럭 안에서 선언하는 경우와 클래스 밖에서 `const val`을 통해 선언하는 경우가 있는데 어떤 차이가 있는지 알아보기 위한 학습

# 내용

1. 코틀린에서 상수는 원시값과 String 만 가능하다.

```kotlin
class SimpleClass {
}

const val constantAtTopLevel : = SimpleClass()

<<Console>>
Const 'val' has type 'SimpleClass'. Only primitives and String are allowed
```

1. Top level 에서의 상수 선언

```kotlin
const val CONSTANT_AT_TOP_LEVEL = "constant value defined at the top-level"
class ConstantAtTopLevelTest {
    @Test
    fun whenAccessingConstantAtTopLevel_thenItWorks() {
        Assertions.assertThat(CONSTANT_AT_TOP_LEVEL).isEqualTo("constant value defined at the top-level")
    }
}
```

- 코틀린에서는 하나의 파일에 여러개의 클래스를 관리할 수 있다.
- class 밖에 선언하게 되면 어디서든 바로 접근할 수 있다.
- 따라서, 여러 클래스에서 같이쓰는 상수를 정의하고 싶을 때 사용하면 된다.

Top-level 선언의 한계

- 심플하지만 어느 클래스에 소속되지 않는다.
- 컴파일러에서 해당 클래스를 새로 만든다.

1. Companion Object 블럭에서의 선언

```kotlin
class ConstantsBestPractices {
    companion object {
        const val CONSTANT_IN_COMPANION_OBJECT = "constant at in companion object"
    }
}

class ConstantInCompanionObjectTest {

    @Test
    fun whenAccessingConstantInCompanionObject_thenItWorks() {
        Assertions.assertThat(CONSTANT_IN_COMPANION_OBJECT).isEqualTo("constant in companion object")
    }
}
```

- 클래스에서 관련된 상수를 관리하고 싶을 때 사용하면 된다.

1. Java 코드에서 상수에 대한 접근

```kotlin
public class AccessKotlinConstant {
    private String staticObjectFromTopLevel = ConstantsBestPracticesKt.CONSTANT_AT_TOP_LEVEL;
    private String staticObjectFromCompanion = ConstantsBestPractices.CONSTANT_IN_COMPANION_OBJECT;
}
```

- 만약 Top-Level에 작성하면 코틀린 파일의 경로를 작성해야한다.
- Companion Object에 작성하면 해당 클래스를 통해 접근할 수 있다.

# 정리

- 웬만하면 Compnaion Object에 상수를 선언하는 것이 적절할 것 같다.