# Dev 환경 InfluxDb로 연결

# 주제

- JVM 리소스를 InfluxDb에 적재하고 모니터링할 방안을 찾아본다.
- 가능하면 지금 구조 그대로 가져가보고 싶다
  - actuator - influxDb - Grafana

# 설치

- 홈페이지에서 스펙에 맞게 설치한다. https://portal.influxdata.com/downloads/

```bash
sudo apt-get update && sudo apt-get install influxdb2
```

- port를 3100으로 변경해도 8086으로 시작되는 이슈

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f91d47f-7e53-4bfb-a472-afeb35c15120/Untitled.png)

- influxDB가 생각보다 더 잘나가는 DB 였다.
- 2023년 3월 기준 TSDB 중에서는 압도적으로 1등이다