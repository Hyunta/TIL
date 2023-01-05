# AWS SQS

# 소개

Amazon Simple Queue Service 는 배달 못한 편지 대기열, 비용할당 태그 모든 프로그래밍 언어를 사용하여 엑세스 할 수 있는 일반 웹 서비스 API 를 제공한다. SQS는 표준과 FIFO 대기열을 모두 지원한다.

## 이점

1. 보안 : 기본 SQS 암호화 SSE를 사용하거나 사용자 지정을 통해서 메시지 컨텐츠 보호가능
2. 내구성 : 메시지 안전을 위해 SQS를 여러 서버에 저장한다.
   1. 표준 대기열은 적어도 한번 메시지 전송
   2. FIFO는 정확히 한번에 메시지 처리
3. 가용성
4. 확장성
5. 안정성 : 메시지를 잠그므로 여러 Producer가 메시지를 보내고, 여러 Consumer가 수신할 수 있다.
6. 사용자 지정

## 대기열 유형

| 구분 | 표준대기열                                                   | FIFO 대기열 |
| ---- | ------------------------------------------------------------ | ----------- |
|      | 무제한 처리량— 표준 대기열은 API 작업당 초당 API 호출 수를 거의 무제한으로 지원합니다 (SendMessage,ReceiveMessage, 또는DeleteMessage). |             |

최소 한 번 배송— 메시지는 한 번 이상 배달되지만 한 개 이상의 메시지 사본이 전달되는 경우가 있습니다.

최선의 주문— 메시지가 전송된 순서와 다른 순서로 전달되는 경우가 있습니다. | 높은 처리량— 사용하는 도구배치, FIFO 대기열은 API 메서드당 초당 최대 3,000개의 메시지를 지원합니다 (SendMessageBatch,ReceiveMessage, 또는DeleteMessageBatch). 초당 3000개의 메시지는 각각 10개의 메시지로 구성된 300개의 API 호출을 나타냅니다. 할당량 증가를 요청하려면 지원 요청을 제출하십시오. 배치 처리가 없으면 FIFO 대기열은 API 메서드(SendMessage, ReceiveMessage 또는 DeleteMessage)별 초당 최대 300개의 API 호출을 지원합니다.

정확히 한 번 처리— 메시지는 한 번 전달되며 소비자가 메시지를 처리하고 삭제할 때까지 계속 사용할 수 있습니다. 중복 항목을 대기열에 삽입하지 않습니다.

선입선출 배송— 메시지를 보내고 받는 순서는 엄격하게 보존됩니다. | |  | 다음 예와 같이 처리량이 중요할 때 애플리케이션 간에 데이터를 전송합니다.

실시간 사용자 요청을 폭넓은 배경 작업과 분리: 미디어 크기를 조정하거나 인코딩하는 동안 미디어를 업로드할 수 있습니다.

작업을 여러 작업자 노드에 할당: 대량의 신용카드 확인 요청을 처리합니다.

이후의 처리를 위해 메시지를 배치 처리합니다. 다수의 항목이 데이터베이스에 추가되도록 예약합니다. | 다음 예와 같이 이벤트 순서가 중요할 때 애플리케이션 간에 데이터를 전송합니다.

사용자가 입력한 명령이 올바른 순서로 실행되는지 확인하십시오.

가격 수정을 올바른 순서로 전송하여 올바른 제품 가격 표시.

학생이 계정 등록 전에 과정에 등록하지 못하도록 차단. |

# Amazon SQS 기본 아키텍처

## 분산 대기열

분산 메세징 시스템에는 구성 요소, 대기열, 대기열 메시지가 있다.

**Producer**(메시지를 큐로 전송하는 컴포넌트)

**Consumer**(큐의 메시지를 수신하는 컴포넌트)가 있습니다

**Queue**(메시지 A~E 유지)는 여러 SQS 서버에 메시지를 중복 저장한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cfa3abc-4f35-45e9-a460-9544f6ad2168/Untitled.png)

## 메시지 생명 주기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/78e6e160-0461-48d0-ae4f-67de3184b09f/Untitled.png)

1. producer는 메시지 A를 큐에 전달하고 SQS 서버에 중복 분산된다.
2. consumer가 메세지 A를 처리할 준비가 되면 큐에서 메시지를 소비하고 메시지A를 반환한다. 메시지 A가 처리되는 동안 큐에 그대로 남아있고 제한 시간동안은 추후 수신 요청으로 반환하지 않는다.
3. consumer가 큐에서 메시지 A를 삭제하여 제한시간 초과가 만료되면 이 메시지가 수신되어 다시 처리되지 못하도록 한다.

# 메세지 큐

## 큐 생성

AmazonSqs 클라이언트를 사용한다. `creatQeueue` 메서드를 통해서 생성한다.

```java
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.model.AmazonSQSException;
import com.amazonaws.services.sqs.model.CreateQueueRequest;

AmazonSQS sqs = AmazonSQSClientBuilder.defaultClient();
CreateQueueRequest create_request = new CreateQueueRequest(QUEUE_NAME)
        .addAttributesEntry("DelaySeconds", "60")
        .addAttributesEntry("MessageRetentionPeriod", "86400");

try {
    sqs.createQueue(create_request);
} catch (AmazonSQSException e) {
    if (!e.getErrorCode().equals("QueueAlreadyExists")) {
        throw e;
    }
}

//간소화된 버전
sqs.createQueue("MyQueue" + new Date().getTime());
```

## 큐 목록 가져오기

```java
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.model.ListQueuesResult;

AmazonSQS sqs = AmazonSQSClientBuilder.defaultClient();
ListQueuesResult lq_result = sqs.listQueues();
System.out.println("Your SQS Queue URLs:");
for (String url : lq_result.getQueueUrls()) {
    System.out.println(url);
}
```

파라미터 없이 listQueues를 사용하면 모든 대기열이 반환된다.

```java
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.model.ListQueuesRequest;

AmazonSQS sqs = AmazonSQSClientBuilder.defaultClient();
String name_prefix = "Queue";
lq_result = sqs.listQueues(new ListQueuesRequest(name_prefix));
System.out.println("Queue URLs with prefix: " + name_prefix);
for (String url : lq_result.getQueueUrls()) {
    System.out.println(url);
}
```

`listQueuesRequest` 객체를 전달하면 반환된 결과를 필터링 할 수 있다.

## 지정된 큐 갖고오기

```java
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;

AmazonSQS sqs = AmazonSQSClientBuilder.defaultClient();
String queue_url = sqs.getQueueUrl(QUEUE_NAME).getQueueUrl(); 
```

# 메시지

## 단일 메시지 보내기