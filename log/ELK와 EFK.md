# ELK와 EFK 스택의 차이

ElasticSearch - LogStash - Kibana

ElasticSearch - Fluentd - Kibana

로그를 수집하는 과정에서 로그 적재기, 로그 저장소, 로그 시각화 툴이 필요하다. LogStash와 Fluentd는 모두 로그 적재기의 역할을 한다. 로그 파일을 수집하고 적재하여 ElasticSearch에 적재하고 해당 데이터를 Kibana를 이용해 표출하는 용도로 스택을 구성한다.

LogStash는 애플리케이션 당 메모리를 1GB 정도 사용하는 반면에 Fluentd는 애플리케이션 당 메모리를 25MB 정도만 사용하기 때문에 가볍다.

둘다 엔터프라이즈급 로그 파이프라인 구성에 사용되는 로그 분석용 파서 역할을 할 수 있습니다. 필터링, 라우팅할 수 있습니다.

LogStash는 자체 로그 수집 기능이 없으며 Filebeat, Metricbeat 에이전트에서 수집한 로그를 받거나 다른 시스템과 통합하는 과정을 통해 수집된 로그를 받을 수 밖에 없습니다. 반면에 Fluentd는 자체 데몬을 통해 다양한 소스의 로그를 수집할 수 있습니다.

해당 부분이 차이나기 때문에 모놀리식한 환경에서 로깅 파이프라인을 구축할 때는 LogStash를 사용하고, MSA 환경에서는 Fluentd를 이용하는 것이 용이합니다.

Reference:

https://medium.com/flowfactor/logstash-vs-fluentd-a-drag-race-d4df351ef3f6

https://techblog.gccompany.co.kr/eks-환경에서의-efk-도입기-e8a92695e991

https://nangman14.tistory.com/68