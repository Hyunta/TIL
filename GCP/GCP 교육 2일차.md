# 2일차 낙서장

# Load Balancer

- HTTPS, TCP, UDP 3가지 중에 선택 가능
- HTTPS로 선택할 경우 내부에서만 할 것 인지, 외부에서도 이뤄질 것인지 선택 가능하다.

# CDN

gsutil cp gs://cloud-training/gcpnet/cdn/cdn.png gs://qwiklabs-gcp-01-c9c09df3b4be gsutil cp gs://cloud-training/gcpnet/cdn/regions.png gs://qwiklabs-gcp-01-c9c09df3b4be

```
for ((i=0;i<100;i++)); do curl -w  \\
    "%{time_total}\\n" -o /dev/null -s <http://34.111.241.66:80/cdn.png>; done
```

# Cloud Interconnect

- 파트너가 있고, 직접 연결하는 것이 있다.

# Cloud VPN

- Classic VPN은 레거시고, HA VPN을 봐야한다.
- HA 는 이중화가 가증한 VPN

# HA VPN

# Private Connection Option

- Private이 들어가면 Internal 망을 사용한다는 것이다.