# 그라파나와 ELK 연동 가능한지 리서치

메트릭과 시스템 리소스에 대한 모니터링은 이미 그라파나로 충분히 구축되어 있어서, 이번 과제는 거의 로그 모니터링을 주로 하게 될 것 같았습니다. SpringCloud 환경을 구성하고 있기 때문에 zipkin을 통해 traceId를 부여하고 ES와 LogStash를 통해서 구축하면 될 것 같아보였습니다. 저희가 현재 모니터링 툴로 그라파나에서 시각화하는 부분이 많기 때문에 ELK 스택의 Kibana가 아닌 Grafana로 표출이 가능한지 확인해봤습니다.

우선 Grafana의 주 목적은 메트릭 분석 및 시각화 입니다. Kibana는 로그 및 포렌식 보안과 같은 기타 로그 종속 사용에 중점을 둡니다.

https://logz.io/blog/grafana-vs-kibana/

## Kibana

키바나는 ELK 스택에서 로그 탐색, 시각화, 대시보드 구성을 통해 ES에 저장된 로그데이터를 보여주는 역할을 합니다.

핵심 기능은 데이터 쿼리와 분석입니다. 사용자는 ES에 인덱싱된 특정 이벤트와 문제 분석할 수 있도록 도와주고 쿼리기반으로 차트, 테이블 등을 보여줍니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d325be8-bce2-42ae-87a1-afefec9120c8/Untitled.png)

## Grafana

그라파나는 데이터 시각화 오픈소스 툴입니다. 프로메테우스, influxDB, ElasticSearch와 함께 사용됩니다.

그라파나는 키바나에서 메트릭 정보 시각화를 많이 지원하지 않기 때문에 이를 개선하기 위해서 나왔습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ebb1763-7f57-47df-974e-781ee99bc7f5/Untitled.png)

## Logging과 Metrics

두 시각화 도구의 가장 큰 차이는 목적입니다. 그라파나는 메트릭 정보를 시각화하기 위해 설계되었습니다. CPU, Memory, I/O 작업을 주로 보여줍니다. 키바나는 ElasticSearch를 기반으로 로그 메세지를 분석하기 위해 주로 사용됩니다.

아예 사용이 불가능한 것은 아니지만 사용성에 제한이 있습니다.

그라파나 측에서는 Loki를 통해서 로그 모니터링까지 지원하고 있습니다. Loki는 로그 데이터를 인덱싱하지 않고, 라벨을 통해 categorizing 하기 때문에 라벨을 통해 모니터링이 필요한 경우 키바나보다 나은 선택지일 수 있습니다. 그 외에는 키바나가 로깅 처리에 최적화가 더 잘 되어있습니다.

## Querying

쿼리와 로그를 검색하는 기능은 키바나의 강점입니다. Lucene Syntax나 Query DSL 등을 사용해서 ElasticSearch에 적재된 데이터를 시각화합니다.