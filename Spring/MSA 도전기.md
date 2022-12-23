# 유레카 서버 생성

spring initializr

EurekaServer, SpringWeb 의존성 추가

1. main 클래스에 `@EnableEurekaServer` 애노테이션 추가

```java
@EnableEurekaServer
@SpringBootApplication
public class ServiceDiscoveryApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServiceDiscoveryApplication.class, args);
    }
}
```

1. application.yml에 eureka 설정 추가

```yaml
server:
  port: 8761

spring:
  application:
    name: imp-discovery-service

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
```

[localhost](http://localhost):8761로 가면 대시보드를 제공한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f1ec654-f84d-402f-8fc9-372ab817681c/Untitled.png)

# 유레카 클라이언트 생성

각 도메인별 클라이언트 서버 생성

EurekaDiscoveryClient 의존성 추가

1. main에 `@EnableDiscoveryClient` 애노테이션 추가

```java
@EnableDiscoveryClient
@SpringBootApplication
public class AuthServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(AuthServiceApplication.class, args);
	}
}
```

1. application.yml 설정
   1. defaultZone은 생략해도 가능

```yaml
server:
  port: 9090

spring:
  application:
    name: auth-service

eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: <http://localhost:8761/eureka>
```

1. 대시보드 확인하면 등록된 클라이언트를 확인할 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6491a592-d02e-497f-a4b2-feabdbb18cbf/Untitled.png)

1. 작성된 코드를 복붙해서 가져온다.

Member, Product 유레카 클라이언트를 각각 생성해줌

막힌 부분:

1. Product에 대한 Test 중 Member를 사용해야하는 경우 어떻게 할 것 인가?