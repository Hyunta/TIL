## OAuth(Open Authorization)란

OAuth는 인증을 위한 프로토콜이다.

OAuth는 인증과 인가를 모두 포함하고 있다. 그 중 **인가**에 좀 더 초점을 맞추고 있다.

네이버 로그인을 생각해보자. 네이버 사용자인지 인증하는 과정은 네이버에서 담당한다. OAuth는 인증을 제공하지만, 주된 목적은 인증된 사용자의 정보를 가져오는 권한을 제공하는 것이다.

OAuth 2.0 부터는 반드시 HTTPS 사용, 웹이 아닌 애플리케이션도 지원, Access Token 만료 시간 설정 등이 추가되었다.



## 용어 정리

- Resource Owner : 사용자, 클라이언트
- Client Application : 사용자가 사용하는 서비스 애플리케이셔 
- Resource Servcer : OAuth를 통해 인증, 인가를 제공해주는 서버, 자원 서버, 자원을 제공해준다.
- Authorization Server : OAuth를 통해 인증, 인가를 제공해주는 서버, 인증 서버, 토큰을 발급해준다.

Resource Servcer와 Authorization Server는 자원과 인증으로 분리되어 있긴 하지만, 둘 다 같은 소속이다. ex) Google, Naver, Kakao 등

