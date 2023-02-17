# 학습 동기

`@ConfigurationProperties` 를 이용하면 application.yml에 작성한 properties를 객체로 매핑할 수 있다. 처음에 SpringBoot에서 어떻게 파일을 읽어와서 값을 저장하고 있는지 궁금해서 찾아봤다.

처음에는 ChatGPT한테 물어보면 알려줄 것 같아서 물어봤더니, 어떻게 ConfigurationProperties를 사용하는지 방법에 대해서만 알려주고 구체적으로 어떻게 Binding하는지 알려주지 않아서 직접 찾아보게됐다.

# 과정

## @ConfigurationProperties에서 PropertySource를 받아오는 과정

- `@ConfigurationProperties` 는 스프링 부트에서 관리하는 기술이기 때문에, 해당 패키지에 가서 클래스를 살펴봤다.
  

![](https://velog.velcdn.com/images/mohai2618/post/492e1bff-f2c3-4e88-a89b-30c0da93a963/image.png)

`ConfigurationProperties` 를 관리하는 객체들이 많이 있었는데 이것저것 보다보니 `ConfigurationPropertiesBinder` 가 관련된 정보를 묶어주는 역할을 한다는 것을 알았다.

뭔가 Spring Core에서 제공하는 Environment를 이용해서 값을 읽어오고 있을 것 같아서 무작정 필드값에 Environment가 있는 클래스를 찾았다.

`ConfigurationPropertiesBinder` 는 필드값으로 `ApplicationContext` 와 `PropertySources`를 갖는데, 이름으로 유추해봤을 때 내가 찾던 `Environment` 가 있을거라고 추측했다.

![](https://velog.velcdn.com/images/mohai2618/post/331fa585-4a80-4626-832f-0892e5ad792e/image.png)

`PropertySourcesDeducer.getPropertySources()` 메서드를 호출하게 되면 applicationContext에서 Environment를 받아와서 해당 객체의 propertySource를 받아오는 작업을 진행한다.
![](https://velog.velcdn.com/images/mohai2618/post/56de8e94-5c2c-4ff3-8d00-0ffc8070837d/image.png)

이를 통해서 `@ConfigurationProperties`가 붙어있는 클래스에 어떻게 Environment가 붙는지를 알 수 있었다. 하지만 내 궁금증은 어떻게 Environment에 application.yml 값이 저장될 수 있는지에 가까워서 계속 탐구를 진행했다.

## Environment에 application.yml 내용을 읽어오는 과정

이어서 SpringBoot가 아니라 Spring Core 쪽 코드를 파악하면서 어떻게 파일을 읽어서 가져오는지 탐구해봤다.

![](https://velog.velcdn.com/images/mohai2618/post/b505ed4f-03a4-4adc-b9cf-935583f8cf63/image.png)

먼저 Environment를 받아오는 코드들을 찾아봤다. `AbstractEnvironment.cutomizePropertySources()`  메서드를 통해 사용자가 임의로 application.yml에 작성하는 필드값들은 받아온다는 것을 확인할 수 있었다.

![](https://velog.velcdn.com/images/mohai2618/post/ef14a5a3-93fb-494a-8db6-117bb24dc843/image.png)

`PropertySourcesPropertyResolver` 객체를 참고하라고 되어있길래 찾아봤더니 property 값을 가져오는 메서드들을 확인할 수 있었다.

![](https://velog.velcdn.com/images/mohai2618/post/4982458c-ed4c-4d7e-bfe0-7920b185622c/image.png)

PropertySource에 등록된 property의 targetType이 있는 경우 맞춰서 객체로 반환하고, 없으면 String으로 보내는게 기본값인 것처럼 보였다.

SpringBoot에서는 PropertySource에 추가로 `@ConfigurationProperties` 어노테이션이 붙어있는 빈들도 등록해주는 것으로 확인했다.
![](https://velog.velcdn.com/images/mohai2618/post/b2565e16-9c7f-4dfd-90e1-06a3f3f9d21e/image.png)

# 정리
직접 추적해가면서 흐름을 파악해보려고 했는데 추상화되어있는 부분들이 많아서 정확하게 잘 추적한지는 모르겠다. 하지만 대략적인 그림은 그릴 수 있었다.
SpringBoot에서 먼저 application.yml을 propertySource로 등록하는 과정을 진행하고, Spring Core에서 property Source를 통해 받아와 객체로 변환해주는 작업을 진행한다.
이래서 Properties로 등록하면 application.yml에 있는 정보를 가져와 객체로 생성할 수 있는 것 같다.
아직까지 확실하지 않은 부분들도 있어서 추후 알게된다면 추가하겠다.