# 학습 동기

AOP 실습 중 JDK 동적 프록시를 이용하여 test를 진행하는 부분이 있었다. JDK 동적 프록시가 뭔지 모르고, CGLIB 등등 프록시라는 말은 자주 써왔는데 막상 해보려니 잘 안돼서 자바와 스프링에서 프록시를 어떻게 구현하고 사용해야하는지 정리하게 됐다.

# 상황 가정

Case1. 인터페이스와 구현 클래스 → Configuration

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b030b658-528c-49a0-bcc1-203713c683d8/Untitled.png)

Case2. 인터페이스 없는 구체 클래스 → Configuration

Case3. 구체 클래스 + 애노테이션 → ComponentScan

```
정상 요청

  [796bccd9] OrderController.request()
  [796bccd9] |-->OrderService.orderItem()
  [796bccd9] |   |-->OrderRepository.save()
  [796bccd9] |   |<--OrderRepository.save() time=1004ms
  [796bccd9] |<--OrderService.orderItem() time=1014ms
  [796bccd9] OrderController.request() time=1016ms

예외 발생

[b7119f27] OrderController.request()
[b7119f27] |-->OrderService.orderItem()
[b7119f27] | |-->OrderRepository.save()
[b7119f27] | |<X-OrderRepository.save() time=0ms
ex=java.lang.IllegalStateException: 예외 발생!
[b7119f27] |<X-OrderService.orderItem() time=10ms
ex=java.lang.IllegalStateException: 예외 발생!
[b7119f27] OrderController.request() time=11ms ex=java.lang.IllegalStateException: 예외 발생!
```

**요구사항 추가**

원본 코드를 전혀 수정하지 않고, 로그 추적기를 적용해라. 특정 메서드는 로그를 출력하지 않는 기능

보안상 일부는 로그를 출력하면 안된다. 다음과 같은 다양한 케이스에 적용할 수 있어야 한다.

v1 - 인터페이스가 있는 구현 클래스에 적용 v2 - 인터페이스가 없는 구체 클래스에 적용 v3 - 컴포넌트 스캔 대상에 기능 적용

가장 어려문 문제는 **원본 코드를 전혀 수정하지 않고, 로그 추적기를 도입**하는 것이다. 이 문제를 해결하려면 프록시(Proxy)의 개념을 먼저 이해해야 한다.

# 프록시 개념

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a1eb655-1160-45e5-9269-eadce9ba173a/Untitled.png)

Client는 요청을 프록시로 보낸건지 서버로 보낸건지 몰라야한다. 그저 요청을 할 뿐이고 서버에서 응답하는 것이다. 서버와 프록시는 같은 인터페이스를 사용해야 한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6570d168-44b9-4794-a9a0-587364f70093/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b449cdb6-9200-493d-b8a0-193682b4a8c8/Untitled.png)

프록시를 통해서 할 수 있는 일은 크게 두가지다.

1. 접근 제어
2. 부가 기능 추가

GOF 디자인 패턴에 따르면 같은 프록시여도 의도에 따라 패턴 이름이 바뀐다.

1. 접근 제어가 목적이라면, ***프록시패턴***
2. 부가 기능 추가가 목적이라면, ***데코레이터 패턴***

# 프록시 패턴과 데코레이터 패턴

## 프록시 패턴

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a6dc7f7-b292-48e1-9a02-d870e6d2879d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0ea89d3-2ea7-4263-b9da-22c649d0a00d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8c809ec4-553e-4236-b179-23b2d634b083/Untitled.png)

프록시 패턴 어렵지 않다.

Cache값이 존재하면 Cache를 반환하고, 존재하지 않으면 실제 target에 요청을 보낸다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddac3a3d-793a-4ab8-ac44-b5d58e9a2623/Untitled.png)

## 데코레이터 패턴

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4032475c-f692-4194-9bc7-ccc77e4160ac/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/35442f91-6aa4-4451-8c1a-99f173b73e1f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c874ef0b-54b8-41b5-9b35-e337765c3758/Untitled.png)

데코레이터 패턴을 통해 로그 기록을 변경할 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c55f82e8-9bef-475f-bf16-1b3bfbdc7c30/Untitled.png)

데코레이터를 여러개 달 수도 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15f7331d-0880-46d4-b6f2-139424a04133/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc1c63fa-3976-47de-b439-5367253ae89e/Untitled.png)

## 프록시 패턴 vs 데코레이터 패턴

GOF 패턴은 코드의 짜임새보다 의도가 더 중요하다. 프록시 패턴과 데코레이터 패턴은 의도가 다르기 때문에 분리되어있다.

프록시 패턴: 다른 객체에 접근을 제어하기 위한 프록시

데코레이터 패턴: 객체에 추가 기능을 동적으로 추가하고, 기능을 확장하기 위한 대안 제공

## 적용

### Case 1. 인터페이스 + 구현 클래스

Config에서 빈 등록을 할 때 프록시 객체를 주입해준다. 아래 코드에서 `xxxInterfaceProxy` 객체들은 인터페이스를 구현한 프록시 객체다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15bd9a5d-80c6-4625-82aa-aced7ae65d1e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cc770e3-96c4-465a-a04f-e5cd286e285d/Untitled.png)

전체적인 흐름은 아래 도식과 같이 이뤄진다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be7a109e-3c43-41bb-9e2d-46bcb0a7d7e5/Untitled.png)

### Case2. 구체 클래스

`xxxConcreteProxy` 는 객체를 상속받은 객체다. 구체 클래스를 상속받다보니 제약조건이 생긴다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/663e3ba6-dc38-417d-864e-7c9f8086085a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01ba0875-be07-4266-ad51-04a75bc7c7ed/Untitled.png)

부모 클래스의 생성자를 호출해야하므로, repository에 null을 넣어준다.

## 정리

가장 기본적인 프록시 패턴을 이용해서 적용해봤다.

구체 클래스 기반의 프록시는 해당 클래스를 상속받아야 하므로 제약조건이 있다.

인터페이스 기반의 프록시는 그에 비해 수월하다.

하지만 모든 상황에서 인터페이스가 존재할 수는 없는 법이다. 결국 취향에 맞춰 선택할 수 있는 영역이 아니다.

우선 요구사항에 맞춰 원본 코드의 수정없이 구현을 했다.

**하지만, 단점이 너무 명확하다.**

프록시 클래스를 너무 많이 만들어야 한다. 모두 중복 로직인데 적용하는 클래스마다 프록시 클래스를 만들어야 한다. 대상 클래스가 100개면 프록시 클래스도 100개 만들어야한다.

→ 이를 해결하기 위한 기술이 **동적 프록시**다.

# 동적 프록시

자바가 기본으로 제공하는 JDK 동적 프록시 기술이나 CGLIB 같은 프록시 생성 오픈소스 기술을 활용하면 프록시 객체를 동적으로 만들어낼 수 있다.

JDK 동적 프록시를 이해하기 위해서 리플렉션을 어느정도 알고 있어야 한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/695bcc30-08c9-4f2e-b930-81482da3966f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90381039-7d53-458c-883a-c8496623985c/Untitled.png)

Reflection을 통해  invoke할 메서드를 전달할 수 있다 정도만 알고 있으면 된다.

## JDK 동적 프록시

앞서 살펴본것처럼 프록시 클래스를 여러개 만들지 않는 방법이다. JDK 동적 프록시는 인터페이스를 기반으로 프록시를 동적으로 만들어준다. 따라서 인터페이스가 필수다.

왜 인터페이스가 필수지..??

추측1. 새로운 구현 클래스를 만들어서 사용하려고

아래와 같이 A,B 서로 다른 인터페이스를 구현한 구현체 AImpl,BImpl을 보자.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e654f9a2-26da-4ec1-afe3-52c1e9f41043/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2d64c79a-10ec-4a6f-ac18-c5d21994afbf/Untitled.png)

프록시 패턴을 이용하면 이렇게 구현했을 것이다.

JDK 동적 프록시에 적용할 로직은 `InvocationHandler` 인터페이스를 구현해서 작성하면 된다.

```java
package java.lang.reflect;
  public interface InvocationHandler {
       public Object invoke(Object proxy, Method method, Object[] args) throws Throwable;
}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a81f294b-8dea-4bbd-b6d8-5ab26652caf1/Untitled.png)

Object target : 동적 프록시가 호출할 대상

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7892759b-0ebb-4718-b209-2f58fc0b167f/Untitled.png)

AImplProxy, BImplProxy와 같은 프록시 클래스를 따로 만들지 않더라도 TimeInvocationHandler를 이용해서 프록시 객체를 동적으로 만들 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2dcb2a6-0347-4615-96a2-1e207ed2cdc9/Untitled.png)

`proxyClass=class com.sun.proxy.$Proxy9` 생성된 프록시 정보

프록시는 TimeInvocationHandler 로직을 실행한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b84b17dc-750d-4ba1-ac3c-c31cb2687993/Untitled.png)

AImpl과 BImpl 각각 프록시를 만들지 않고, TimeInvocationHandler를 공통으로 ㅎ사용해서 동적으로 만들었다.

이제 100개의 프록시 클래스를 만들필요 없이, 필요한 InvocationHandler를 넣어주면 된다.

부가 기능 로직도 하나의 클래스에 모아 SRP도 지킬 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc18962c-a30f-4935-b9ac-65c805984c89/Untitled.png)

### 적용 (인터페이스가 있는 Case1만 적용 가능)

InvocationHandler를 상속받는 LogTraceBasicHandler 구현체를 만든다.

이곳에는 Logging 관련 부가 기능이 적혀있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e953a464-5e8b-4ea1-bee8-cc55c8cbe89d/Untitled.png)

Configuration에서 동적으로 프록시를 만들어서 주입해준다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/739c6dc7-dfc0-4f8e-becf-cec01bcb38b0/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99918711-e830-4515-8615-064978692499/Untitled.png)

`url/v1/no-log` 를 호출하는 경우 로그가 남으면 안된다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cfe95d84-d8f2-4675-bf9c-9b94b6f2a8fd/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0e1a6ccb-f6c0-4ec4-b868-56f017120217/Untitled.png)

### 한계

JDK 동적 프록시는 인터페이스가 필수다.

V2 애플리케이션처럼 인터페이스 없이 구체클래스만 있으면 적용할 수 없다.

CGLIB이라는 외부 라이브러리를 사용해서 바이트 코드를 조작해야한다.

## CGLIB

Code Generator Library

- 바이트코드를 조작해서 동적으로 클래스를 생성하는 기술을 제공하는 라이브러리
- 구체 클래스만 가지고 동적 프록시를 만들 수 있다.
- 스프링 프레임워크가 스프링 내부 소스 코드에 포함했다. 따라서 스프링 환경이라면 라이브러리 추가없이 사용할 수 있다.

어차피 스프링의 ProxyFactory를 이용하는 경우가 대다수이기 때문에, 대충 어떤 느낌인지 감만 잡고 넘어가자.

JDK 동적 프록시의 `InvocationHandler` 처럼

CGLIB에는 `MethodInterceptor` 가 있다.

```java
package org.springframework.cglib.proxy;
  public interface MethodInterceptor extends Callback {
      Object intercept(Object obj, Method method, Object[] args, MethodProxy
  proxy) throws Throwable;
  }
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73229fcb-7cd0-4d15-921f-d71da45097fc/Untitled.png)

- JDK 동적 프록시와 거의 동일하다.
- 성능상 MethodProxy를 사용하는 것을 권장한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18da75d8-e0b6-46b5-834d-f1f778586f35/Untitled.png)

- CGLIB은 Enhancer를 사용해서 프록시를 생성한다.
- setSuperClass() : 구체 클래스를 상속받아서 프록시를 생성할 수 있다. 어떤 구체 클래스를 상속받을지 지정한다.
- setCallback() : 프록시에 적용할 실행 로직을 할당한다.
- enhancer.create() : 설정한 값을 토대로 프록시를 생성한다.

JDK 동적 프록시는 implement해서 만들고, CGLIB은 extends해서 만든다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c43cf9d-29d0-4449-afb6-bfaf5fe2e9d6/Untitled.png)

CGLIB가 동적으로 생성하는 클래스 이름은 다음 규칙으로 생성된다.

```
대상클래스$$EnhancerByCGLIB$$임의코드
hello.proxy.common.service.ConcreteService$$EnhancerByCGLIB$$25d6b0e3
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7a67a3d-1f71-4f5f-ae69-88f9a6148b66/Untitled.png)

### 한계

- 부모 클래스의 생성자를 체크해야한다 → CGLIB은 자식 클래스를 동적으로 생성하기 때문에 기본 생성자가 필요하다.
- 클래스에 finall 있으면 상속 불가능
- 메서드에 final 있으면 해당 메서드 오버라이딩 불가능

현재 V2에 동적 프록시를 적용할 수 없다.

- 기본 생성자를 추가해야하므로, 의존관계를 setter 주입으로 바꾼다.
- 하지만 ProxyFactory를 이용하면 더 편리하므로 뒤에서 알아보자.

## 정리

남은 문제

- 인터페이스가 있으면 JDK 동적 프록시, 없으면 CGLIB  어떻게 해야하지?
- 두 기술을 함께 사용해서 부가기능을 제공하면 InvocationHandler, MethodInterceptor를 각각 중복으로 만들어서 관리해야하나?
- 특정 조건에 맞을 때 프록시 로직을 적용하는 기능도 같이 제공해줫으면

# 프록시 팩토리

스프링이 유사한 구체 기술들이 있을 때 일관성있게 접근하고, 편리하게 추상화된 기술을 제공한다.

동적 프록시를 통합해서 편리하게 만들어주는 ProxyFactory 라는 기능을 지원한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd94a764-be9e-432a-be6e-66da1865b9a4/Untitled.png)

스프링은 InvocationHandler와 MethodInterceptor를 각각 중복으로 따로 만들지 않고 관리하도록 Advice라는 새로운 개념을 도입했다.

개발자는 InvocationHandler와 MethodInterceptor를 신경쓰지말고 Advice만 만들면된다.

프록시 팩토리를 사용하면 Advice를 호출하는 전용 InvocationHandler와MethodInterceptor를 내부에서 사용한다.

Advice를 만드는 기본적인 방법은 다음 인터페이스를 구현하는 것이다.

```java
package org.aopalliance.intercept;
  public interface MethodInterceptor extends Interceptor {
      Object invoke(MethodInvocation invocation) throws Throwable;
}
```

CGLIB에서 제공하는 MethodInterceptor와 이름이 같으므로 주의하자.

MethodInterceptor → Interceptor → Advice 관계다

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3b956b3-1ccc-4e1f-a407-1f98b40bfe1c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7223f41d-a827-4925-99ab-a8ab7de0f5c7/Untitled.png)

- ProxyFactory에 target 클래스를 집어넣는다. 인터페이스의 유무에 따라 인터페이스가 있다면 JDK 동적 프록시를 사용하고, 구체 클래스만 있다면 CGLIB을 사용한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fb1b9fd0-dcab-4664-928e-49741d26cd94/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c2df1df-11ab-4311-8bb2-641d2d1b619f/Untitled.png)

- 구체클래스만 있으면 CGLIB을 사용한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/78810fc4-d1be-4dc9-b057-c593ea4a0979/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/da7a4e14-44b3-4f11-b726-1a9d6ffb627c/Untitled.png)

proxyTargetClass 라는 옵션을 true로 주면 항상 CGLIB 만 사용할 수 있다.

## 포인트컷, 어드바이스, 어드바이저

- 포인트컷: 어디에 부가기능을 적용할지, 어디에 적용하지 않을지 판단하는 필터링 로직
- 어드바이스: 프록시가 호출하는 부가기능, 프록시 로직
- 어드바이저: 하나의 포인트컷과 하나의 어드바이스를 갖고 있는 맵

프록시에 맞춘 설명, AOP 부분에서 다시 AOP에 맞춰서 정리하겠다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5aca506e-1cc3-4995-a48f-fc5263d1dc0b/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e76fb9e9-ed5c-4b05-9709-abed59b5ef6d/Untitled.png)

Advisor 갯수만큼 프록시를 만들지 않아도 된다. 하나의 프록시에 여러 어드바이저 가능 제발 기억하자. 실무에서 어드바이저만큼 프록시가 생성된다고 샃각하는 것 같다.  AOP를 적용할 때 최적화를 진행해서 프록시는 하나만 만들고, 하나의 프록시에 여러 어드바이저를 적용한다.

## 적용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b2cab86-1fa8-46f2-bb24-f9e7e223eb51/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd880fee-7f17-495d-9920-6b642463fe81/Untitled.png)

프록시팩토리를 이용하여 프록시 객체를 주입하여 구체클래스도 CGLIB으로 동적 프록시를 할 수 있게 됐습니다.

## 한계

1. 너무 많은 설정

   → 스프링 빈 개수 만큼 설정을 해야한다.

2. 컴포넌트 스캔

   → 해결안. 빈 후처리기를 이용한다.

궁금증, 왜 같은 CGLIB인데 ProxyFactory는 기본생성자가 필요없지?