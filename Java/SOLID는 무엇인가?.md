# 객체지향 설계 원칙 SOLID

## 단일 책임 원칙, Single Responsibility Principle

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3327437e-b746-427a-ad36-9b4435bacb1b/Untitled.png)

- 유지보수가 항상 성능을 이기게 된다.
- 유지보수를 극대화하기 위해 객체를 잘 쪼개라
  - SW는 변화에 기민하게 대응할 수 있어야 하기 때문이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/416abfbb-9f3e-4921-b0fc-fd17b31f6ff3/Untitled.png)

- 변경에서 다른 책임의 변경으로의 연쇄작용에서 자유로울 수 있다.
- 다른 원칙의 기초 철학

## 개방 폐쇄 원칙, Open Closed Principle

- 높은 응집도와 낮은 결합도라는 원리로 설명한다.
- 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c32bb6d0-dc57-48a5-9a45-50470adc3f83/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33ef92a5-6252-428d-813e-7bc00977fd52/Untitled.png)

- 전역 변수 사용하면 원칙에 위반한다.
- 아무나 값을 바꿀 수 있으니 추적하기 어렵다.
- Spring에서 DI를 하면서 편해진다. 유지보수 굳
  - 할인 Policy → 비율, 정가 할인

## 리스코프 치환 원칙, Liskov Substitution Principle

- 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b680b725-c925-4e74-84bb-171bea736d5e/Untitled.png)

- 다형성이 핵심이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c7c9f70-abb0-43cc-9c96-ba84d0589cbc/Untitled.png)

- 호환성 이야기
- 상속을 통해 확장을 할 때는 호환성이 중요하다.
- 그럴경우 합성을 이용한 재사용을 해야한다.

## 인터페이스 분리 원칙, Interface Segregation Principle

- 범용 인터페이스 하나보다는 특정 클라이언트를 위한 여러 개의 인터페이스 분리가 더 좋다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88f160f6-153d-4d0f-8c4e-7a88cbbea732/Untitled.png)

- 단일 책임 원칙하고 인터페이스 분리 원칙은 강화하는 것이다.
- 클라이언트 관점에서 어떻게 해줘야하는지 고려해서 맞추는 것이다

## 의존관계 역전 원칙, Dependency Inversion Principle

- 구체화가 아니라 추상화에 의존해야한다
- Spring에서 interface를 의존하여 주입하는 것 처럼.