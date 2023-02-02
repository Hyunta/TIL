# Loki

[How to Setup Alerting with Loki](https://blog.ruanbekker.com/blog/2020/11/06/how-to-setup-alerting-with-loki/)

해당 블로그를 참고하여 Loki를 이용해서 알림을 보낼 수 있는 기능을 구현해봤습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/699c63a3-6f1c-4b01-ad53-0312f210aba8/Untitled.png)

Loki의 기본 아키텍처는 위 그림과 같습니다. Promtatil을 통해서 로그 데이터를 전송받고 Loki는 이를 가공하여 Grafana, AlertManager에 전달하여 시각화하거나 알림을 보냅니다.

Loki는 Prometheus와 다르게 server-side pull이 아닌 agent-side push 방식을 통해 로그를 수집하므로 loki를 먼저 설치해야 합니다. 이런 불편함을 해소하기 위해서 loki stack이라는 세트를 설치하면 promtail과 loki를 같이 설치합니다. 하지만 기존에 사용중인 시스템들과 연계하기에 어렵기 때문에 각 컴포넌트들을 설치하는 것을 권장합니다.

------

https://github.com/ruanbekker/loki-alerts-docker

해당 Repository를 참고하여 실험해봤습니다.

프로젝트를 클론받아서 `/config/alertmanager.yml` 경로에 있는 `SLACK_WEBHOOK_URL` 에 본인이 알림을 받아야 하는 슬랙봇의 url을 작/성해주면 설정은 끝납니다.

![스크린샷 2023-02-01 오후 12.37.29.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca832c1f-ee83-4f39-99d1-78ede0f89a77/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-02-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.37.29.png)

```bash
# 도커 컨테이너를 실행시킵니다.
docker-compose up -d

# 그라파나에 접속합니다.
open <http://localhost:3000>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f74195ae-46a6-44c5-a346-a3a8972d3777/Untitled.png)

도커 대시보드를 보면 지속적으로 http 요청이 오고 로그가 작성되고 있는 환경을 볼 수 있습니다.

job 이름이 dockerlogs 이므로 검색해보면 아래와 같은 구성을 확인할 수 있습니다.

```bash
{job="dockerlogs"}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/854ce361-4eee-46c3-8108-a1ef8a3d754f/Untitled.png)

```bash
# 1분 간격으로 합산한 값을 보여줌
sum by (compose_project, compose_service) (rate({job="dockerlogs"}[1m]))
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4ddaa9fc-d781-454f-9b82-1a2c3fcf579f/Untitled.png)

로그가 60개 이상 쌍혔을 때 알람이 가도록 되어 있기 때문에 알람을 보냅니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a82f493-2085-4130-86ee-e46f726195d9/Untitled.png)

`localhost:9093` 에 접속해보면 해당 알람이 발생한 것을 확인할 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3a260d7-a7b8-47a8-8039-359c6e5d69ca/Untitled.png)

문제를 해결하기 위해서 docker 컨테이너 중 http-request를 중지시킵니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c5dcf07-e3c8-40da-aac2-5a20c5c5b8c7/Untitled.png)

알림 보내는 간격을 5분으로 설정했기 때문에 5분간격으로 로깅을 진행하고, 문제가 해결됐다면 아래와 같은 슬랙 알림을 보내줍니다.