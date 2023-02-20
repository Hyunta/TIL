# Spring Batch 5

# Spring Batch Scope & Job Parameter

여기서 말하는 Scope는 `@StepScope`, `@JobScope` 를 말합니다. 무의식적으로 사용하는 애노테이션들이 실제로 어떤 일들을 하는지 알아봅시다. 그리고 같이 엮이는 Job Parameter도 배워봅시다.

Spring Batch의 경우 외부 혹은 내부에서 파라미터를 받아 여러 Batch 컴포넌트에서 사용할 수 있게 지원하고 있습니다. 이 파라미터를 Job Parameter라고 합니다.

Job Parameter를 사용하기 위해서는 항상 Spring Batch 전용 Scope를 선언해야만 하는데요. 크게 `@StepScope` 와 `@JobScope` 2가지가 있습니다.