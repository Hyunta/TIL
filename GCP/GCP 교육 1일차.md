# 1일차 낙서장

1. VPC 네트워크
2. IPv6를 이제 사용할 수 있다
3. 
4. BYOIP 내 아이피를 사용하는 방법
5. NIC를 여러개 꼽아서 여러 VPC에 엮는 방법
6. 실습
7. DNS 세팅
8. DNS 설정할 때 정책을 정해서 어느망에서 사용하는지 라우팅, 같은 URI 지만 같은 지역으로 받는 세팅 및 실습
9. 퀴즈

# 용어 소개

1. CIDR 표기법

- A.B.C.D/E

| 2진수 | 10진수 | 16진수 |      |
| ----- | ------ | ------ | ---- |
| 0000  | 0      | 0      |      |
| 0001  | 1      | 1      |      |
| 0010  | 2      | 2      |      |
| 0011  | 3      | 3      |      |
| 0100  | 4      | 4      |      |
| 0101  | 5      | 5      |      |
| 0110  | 6      | 6      |      |
| 0111  | 7      | 7      |      |
| 1000  | 8      | 8      |      |
| 1001  | 9      | 9      |      |
| 1010  | 10     | A      |      |
| 1011  | 11     | B      |      |
| 1100  | 12     | C      |      |
| 1101  | 13     | D      |      |
| 1110  | 14     | E      |      |
| 1111  | 15     | F      |      |

- E로 마스킹해서 사용할 수 있는 양을 조절함

ex)

/32 로 마치면 1개만 사용 가능 → 255.255.255.255

10.128.0.0/20 이면 마스크가 20개

8.8.4/4.8.8 만큼의 주소를 쓸 수 있다.

111111111.111111111.1111 / 0000.00000000.00000000

이만큼 사용할 수 있다. 2^12개 → 4,096개

10.0.0.0/24

→ 10.0.0.0 ~ 10.0.0.255 까지 256개 사용할 수 있지만 게이트웨이로 4개를 사용해야한다.

- IPv6 주소 체계는 4보다 길어져서 더 많이 사용할 수 있다.
- `.` 대신 `:` 를 사용한다.
- 각 자리는 32비트로 총 128비트를 사용한다. 표기도 16진수로 표기

------

# VPC networks

Region 기반으로 하나씩 만들어짐

# IPv6

- GCP에서는 fd20::으로 앞에 고정되어 있다.

# Routes

- 방화벽 규칙과 RoutingTable이 일치해야만 이동 가능하다.
- Subnet이 만들어질 때 자동으로 만들어짐
- 네트워크 대역이 겹치지 않으면 Peering을 통해서 서로 다른 Private망을 연결할 수 있다.

# BYOIP

- 보유하고 있는 IP 주소를 클라우드에서 사용할 수 있도록 한다.

manage

ping -c 3 10.130.0.2

mynet eu

ping -c 3 10.132.0.2

privatenet

ping -c 3 172.16.0.2

실습

- VPC에서 처음으로 등록한(nic0인) NIC만 이름으로 호출가능하다
- region에 따라서 접근이 안된다.

# 두번째 실습

- IAP가 있으면 무조건 구글 인증을 받은 사용자만 접근할 수 있도록 한다.
- Client 3대와 Server 2대를 구성해서 확인해본다.

# 02 Controlling Access to VPC Networks

Organization - Project 순으로 정책을 관리할 수 있다.

- 권한이 여러개가 겹치면, 가장 느슨한 권한이 적용된다.
- Project에는 편집자를 주고, BigQuery에는 뷰어 권한을 주면 BigQuery도 편집이 가능해진다.

gcloud compute instances create test-vm --machine-type=n1-standard-1 --subnet=default --zone=us-central1-a

blue

10.128.0.2

green

10.128.0.3

------

# 네트워크 트렌드

Decentralization → 탈중앙화

Automation → 자동화

두가지가 현재 네트워크의 트렌드다.

Google의 방식은 Legacy 일 수도 있다.

MSA, DevOps, CI/CD 의 컨셉이 탈중앙화의 컨셉이다.

2000년대 ~ 2010 초반 : CBD(Component Based Development) → IT 관점

2000년대 후반 ~ 2010년대 : SOA(Service Oriented Architecture) 비지니스 → 표준화 / 중앙 통제

2010년대 후반 ~ : Agile, MSA, DevOps, CI/CD, … → 환경이 빨리 바뀌기 때문에 표준을 아예 풀어버린다

- MSA 도메인별로 루즈하게 엮여있기 때문에 독자 배포가 가능하다. → 도메인 내부에서만 맞추면된다. 개발 방법도 신속하게 이뤄진다.
- MSA에 맞춰서 컨테이너 Kubernetes, Docker 기술들이 떠올랐다. 환경변화에 빠르게 대응하기 위함

privatenet-us-vm

in

ping -c 3 172.16.0.2

ex

ping -c 3 34.121.132.139

# Peering

서로 다른 VPC 끼리 네트워크를 엮고 싶다면 Peering을 이용하면 된다.

- A → B , B → A 두가지를 모두 구성해야한다.
- 구성하면 자동으로 VPC networks의 Routes에 등록된다. Next Hop으로 찾아볼 수 있음
- Peering이 구성되면 Ping 으로 Internal IP로 연결할 수 있음을 확인할 수 있다.
- A → B 하나만 삭제해도 모든 구성이 삭제된다.
- Peering으로 연결됐을 경우 DNS는 사용할 수 없다. IP 주소로 호출해야한다.

# Load Balancing

- 쿠버네티스로 구성하는 방법을 알아두면 좋을 것 같다.. 대세임
- Hybrid NEG(Network Endpoint Group) 으로 여러 서비스를 엮을 수 있다.