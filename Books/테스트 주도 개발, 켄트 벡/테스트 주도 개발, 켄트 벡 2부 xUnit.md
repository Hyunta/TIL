# 테스트 주도 개발

## 2 부. xUnit

- Python을 이용한 TDD
- 테스트툴(xUnit)을 테스트 주도 개발로 만들어보기

----

### 18 장. xUnit으로 가는 첫걸음

Python으로 코딩을 시작했고, 알고리즘도 Python으로 풀기 때문에 언어에 대한 자신감은 있었는데 생각해보니 프로그램을 구현한 경험은 거의 없었다. Class를 만드는 것도 어색하고 실습을 따라가기가 어색해서 Python 공부도 병행하면서 읽어야겠다.

```
Todo
테스트 메서드 호출하기
먼저 setUp 호출하기
나중에 tearDown 호출하기
테스트 메서드가 실패하더라도 tearDown 호출하기
여러 개의 테스트 실행하기
수집된 결과를 출력하기
```



테스트 메서드가 실행이 되었는지 알아보기 위해서 wasRun 클래스를 생성했다.

체크포인트를 만들어서 테스트하기전에는 'None' , 테스트를 마치면 '1'을 출력해주자

```python
class wasRun:
    def __init__(self,name):
        self.wasRun= None
    def testMethod(self):
        self.wasRun = 1
        
test = wasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
```

다음은 testMethod를 직접 호출하는 대신 진짜 인터페이스인 run()을 사용한다.

```python
class wasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        self.name = name
    def run(self):
        method = getattr(self, self.name) #메서드 가져오기
        method() #메서드 실행
```



TestCase 클래스는 부모클래스로, 

WasRun은 작동했는지 여부를,

TestCaseTest는 참, 거짓 여부를 알려준다.

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

class wasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def testRunning(self):
        test = wasRun("testMethod")
        assert (not test.wasRun)
        test.run()
        assert (test.wasRun)

TestCaseTest("testRunning").run()
```

----

### 19장. 테이블 차리기

테스트를 하다보면 발생하는 3가지 패턴 (Bill Wake의 3A)

1. Arrange - 객체를 생성
2. Act - 어떤 자극
3. Assert - 결과를 검사

2,3 단계는 다르지만 1단계는 공통으로 가져가는 경우가 있다.

ex) 객체 7,3을 통한 덧셈과 뺄셈

객체를 생성할 때 두 가지를 고려한다.

1. 성능:
   - 여러 테스트가 같은 객체를 사용하면, 효율적이다.
2. 격리:
   - 한 테스트가 다른 테스트의 결과에 영향을 미치지 않아야한다.



테스트 사이의 커플링을 만들면 안된다. 객체가 충분히 빨리 생성된다는 가정하에 코드를 수정한다.



```python
class TestCase:
    def __init__(self, name):
        print("name= ", name)
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert (self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert (self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
```

`TestCaseTest("testRunnint").run()`의 작동원리

![image-20210808174631178](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210808174631178.png)

----

### 20장. 뒷정리하기

setUp()을 외부 자원을 할당하는 경우가 있다. 각 테스트가 독립적이길 바란다면 tearDown() 메서드 같은 곳에서 자원을 다시 반환할 필요가 있다.



```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log= "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "



class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)

TestCaseTest("testTemplateMethod").run()
```

- 기존 0/1 플래그에서 로그로 테스트 전략을 수정했다.
- tearDown()을 테스트하고 구현했다.

----

### 21장. 셈하기

목표 : 테스트 실행 갯수와 실패 여부 보여주기

`5 run, 2 failed` 와 같은 형식으로

따로 실행 결과를 기록하는 TestResult 객체를 반환하게 만든다.



```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result


class WasRun(TestCase):
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log= "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def summary(self):
        return "%d run, 0 failed" % self.runCount


TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
```

- 가짜 구현을 한 뒤에 단계적으로 상수를 변수로 바꾸어 실제 구현으로 만듬
- 테스트가 실패했을 때 좀더 작은 스케일로 또 다른 테스트를 만들어서 실패한 테스트가 성공하게 만드는 것을 보조

----

### 22장. 실패 처리하기

테스트가 실패한 경우 Count가 있어야하기 때문에 속성을 추가한다.

테스트를 run하는 중에 fail이 발생한다면 늘어날 수 있도록 설정한다.



``` python
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log= "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.failureCount = self.failureCount + 1

    def summary(self):
        return "%d run, 0 failed" % (self.runCount, self.failureCount)


TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
```

----

### 23장. 얼마나 달콤한지

