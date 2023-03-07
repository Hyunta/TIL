# EP-Scheduler CI 적용

- JaCoCo 연동
- 소나큐브 연동
- 단위테스트, 통합테스트 구동환경 분리
- 젠킨스 CI 파이프라인 구성
- local, dev 분리

# 1. Jacoco 연동

Java Code Coverage의 약자로 junit 테스트 결과를 바탕으로 결과를 리포트해주는 정적분석도구다.

Jacoco와 SonarQube를 연계해여 사용하는 경우가 많다.

## 코드 커버리지 측정 기준

1. 구문(Statement)
2. 조건(Condition)
3. 결정(Decision)

```groovy
plugins {
    id 'jacoco'
}

jacoco {
    toolVersion = "0.8.8"
}

test {
    useJUnitPlatform()
    finalizedBy jacocoTestReport
}

jacocoTestReport {
    dependsOn test

    reports {
        xml.required = true
        html.required = true
        csv.required = false
        html.outputLocation = layout.buildDirectory.dir("jacocoHtml")
    }

    finalizedBy(jacocoTestCoverageVerification)
}

jacocoTestCoverageVerification {
    violationRules {
        rule {
            enabled = true
            element = 'CLASS'

            limit {
                counter = 'BRANCH'
                value = 'COVEREDRATIO'
                minimum = 0.00
            }

            limit {
                counter = 'LINE'
                value = 'COVEREDRATIO'
                minimum = 0.00
            }

            limit {
                counter = 'LINE'
                value = 'TOTALCOUNT'
                minimum = 300
            }

//            includes = [ "com.wmp.ep.*" ]
            excludes = [
                    '*.*Application',
                    '*.*Exception',
                    '*.dto.*',
            ]
        }
    }
}
```

# 2. SonarQube 적용

```groovy
docker pull sonarqube
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

최신 자바 라이브러리가 Gradle 6 버전을 지원하지 않아서 7.3.1로 업그레이드

**http://JENKINS_URL/generic-webhook-trigger/invoke**

https://wmporg_search-op:hGt9DUPD4Knx5jCv@dev-ci-jenkins.wemakeprice.kr/generic-webhook-trigger/invoke?token=v2-wmp-ep-sched-ci