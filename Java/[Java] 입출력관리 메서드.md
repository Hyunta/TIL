### 목표:

> Java로 처음 알고리즘을 풀 때는 Scanner를 이용하다가 BufferedReader를 알게되고 효율성에 대해 생각했다. 입출력으로 생각보다 시간이 단축되는 것을 보고 정리를 하기로 했다.

----
### 입력:
1. Scanner
2. BufferedReader

### 출력:
1. System.out.println()
2. BufferedWriter

### 문자열 Formatting:
1. StringBuilder
2. StringBuffer
3. StringTokenizer
----
Input, Output과 관련된 Java Class Convention 

- Stream으로 끝나는 클래스 : 바이트 단위로 입출력을 수행하는 클래스
- Reader / Writer로 끝나는 클래스 : 캐릭터 단위로 입출력을 수행하는 클래스
- File로 시작하는 클래스 : 하드디스크의 파일을 사용하는 클래스
- Data로 시작하는 클래스 : 자바의 원시 자료형을 출력하기 위한 클래스
- Buffered로 시작하는 클래스 : 시스템의 버퍼를 사용하는 클래스

----
## 입력


### 1. Scanner

``` java
Scannner sc = new Scanner(System.in);
```
#### System.in 은 InputStream의 정적 필드이다.
![](https://images.velog.io/images/mohai2618/post/04d5c9ba-5897-4e7b-a56d-25565376c321/image.png)
#### Stream 이란:
![](https://images.velog.io/images/mohai2618/post/603040cf-8a02-4936-893a-f959ccb9dada/image.png)

- 키보드 입력에서의 Stream은 쉽게 말하면 내가 입력하는 값이다.
- InputStream은 말그대로 입력하는 값이고
- OutputStream은 출력하는 값이다.

#### 하지만 System.in으로만 입력을 받고 처리를 안한다면 바이트 단위로 받게되어 UTF-8의 입력을 처리할 수 없다.
- 자세한 사항은 https://st-lab.tistory.com/41 에서 볼 수 있다.

#### Scanner의 역할
![](https://images.velog.io/images/mohai2618/post/d94bb7c9-9f1d-4a90-887c-ba29b97465e6/image.png)

#### InputStreamReader를 호출하여 StreamDecoder를 호출하여 InputStream을 온전한 문자형태로 해석한다.
![](https://images.velog.io/images/mohai2618/post/14d02134-fb3c-426f-80a2-553e997beff4/image.png)

### Scanner 정리:
 - InputStream을 받아온다.
 - InputStreamReader를 통해 StreamDecoder를 호출한다.
 - 바이트 단위 데이터를 Character 단위 데이터로 변환한다.
 - 이후 next(),nextInt(),nextDouble(), nextFloat() 등을 통해 값을 받는다.
   - 참고로 호율성이 떨어지는 이유는 뒤에 정규식 검사를 많이 하기 때문이다.
   
----

### 2. BufferedReader

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```
#### InputStream을 읽어오는 과정은 동일하다.
- InputStreamReader를 통해 바이트 단위의 데이터를 char로 처리한다.

#### BufferReader의 역할
- 우리가 이용하고 싶은 문자열은 char이 아니다. 따라서 배열에 받아야하는데 매번 할 수는 없다.
- 따라서 Buffer를 이용해서 문자를 쌓아두고 한 번에 문자열처럼 보낸다.
- br.readline() 메서드는 한줄을 통으로 String으로 받아온다.


#### BufferReader 정리
- inputStream -> InputStreamReader -> BufferReader
- 위 과정을 통해 byte, char, String 타입으로 변환이 된다.
- 버퍼가 있는 스트림이고, 정규식 검사를 하지 않기 때문에 빠르다.

----
## 출력

### 1. System.out.print_()
```java
System.out.println("Hello World")
```
- InputStream과 동일한 방식으로 PrintStream(System.out)을 받아와서 print(), println(), prinf() 방식으로 출력한다.
![](https://images.velog.io/images/mohai2618/post/e268dc90-5d3d-4675-952a-311f393ffdfd/image.png)
![](https://images.velog.io/images/mohai2618/post/0b305ccf-687a-452d-9d39-e13de9fb35af/image.png)


### 2. BufferedWriter
```java
BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

bufferedWriter.write("Hello World!");
bufferedWriter.flush(); 
bufferedWriter.newLine();
bufferedWriter.close();
```
- BufferedWriter는 Buffer를 이용해서 OutputStream을 저장해두고 flush를 하거나 close될 때 출력한다.

----
## 문자열 Formatting
String을 `String c = a + b;` 처럼 사용하면 String은 불변하기 때문에 새로운 메모리 영역을 가리키게되고 a 와 b는 메모리에 garbage로 남아있게된다.
이를 해결하기 위해서 StringBuffer 과 StringBuilder가 나왔다.
 - JDK1.5버전 이후에는 컴파일 단계에서 String 객체를 사용하더라도 StringBuilder로 컴파일 되도록 변경되었다.
 - 하지만 반복문에서는 인스턴스를 계속 생성하기 때문에 사용하지 말아야한다.

### 1. StringBuilder vs StringBuffer
두 메서드의 코드는 비슷하지만 StringBuffer는 멀티 쓰레드 환경에서 안전하다. StringBuilder는 동기화를 지원하지 않기 때문에 단일 쓰레드 환경에서 적합하다.
``` java
BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

StringBuilder stringBuilder = new StringBuilder();

stringBuilder.append("Hello\n"); 
stringBuilder.append("World!\n");
bufferedWriter.write(stringBuilder.toString());

bufferedWriter.flush();
bufferedWriter.close();
```

``` java
BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

StringBuffer stringBuffer = new StringBuffer();

stringBuffer.append("abc\n"); 
stringBuffer.append("123\n");
bufferedWriter.write(stringBuffer.toString()); 

bufferedWriter.flush();
bufferedWriter.close();
```

### 2.StringTokenizer
StringTokenizer는 문자열을 분리할 때 사용한다.
기본 사용법은 다음과 같다.

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
StringTokenizer st = new StringTokenizer(br.readLine());
st.nextToken()
```
기본적으로 Token은 공백을 기준으로 분리되고, 따로 delim을 설정하여 구분자를 지정할 수 있다. 또한 구분자를 Token으로 반영할 것인지도 정할 수 있다.

----

## 정리:
Java로 알고리즘을 풀면서 input과 output 방법을 언젠간 정리하고 싶었는데 이렇게 하게되어서 후련하고, 과정을 알게되어서 더 적극적으로 도입할 수 있을 것 같다.



----
Reference:
https://docs.oracle.com/javase/7/docs/api/java/io/BufferedReader.html
https://st-lab.tistory.com/41
https://docs.oracle.com/javase/7/docs/api/java/io/BufferedWriter.html
https://ryulth.com/devnote/2019/06/17/java-io-tips/