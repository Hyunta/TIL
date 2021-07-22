# Git Message Convention

![](https://images.velog.io/images/mohai2618/post/f466d007-04a6-4dd2-91a2-1c91bf5c69f4/image.png)

## Intro

Git은 협업을 위한 툴이고 commit message를 통일성있게 작성하는 것이 유지보수의 효율성을 높이기 때문에 통용되는 Git commit message의 관습을 알아보고자 했다.

## 기본적인 틀

>
>type: Subject
>
>body
>
>footer

### The Title :
Title은 Type과 Subject로 구성된다.

#### The Type :
- feat: A new feature
	- 새로운 기능
- fix: A bug fix
	- 버그 수정
- docs: Changes to documentation
	- 문서 수정
- style: Formatting, missing semi colons, etc; no code change
	- 포맷 변경, 세미 콜론 누락 ; 코드의 변화는 없다.
- refactor: Refactoring production code
	- 리팩토링
- test: Adding tests, refactoring test; no production code change
	- 테스트 관련 수정 및 추가
- chore: Updating build tasks, package manager configs, etc; no production code change

#### The Subject :
주제는 50자 이내로 작성하고 대문자로 시작하고 마침표를 찍지 않는다.
명령문으로 작성한다.(ex: Change commit, Add controller)

### The Body :
선택사항. commit 에 대한 부연 설명이 필요할 경우에만 작성.
**'어떻게'** 가 아니라 **'무엇을 왜'**

만약 Body를 작성해야한다면 Title과 한줄 간격을 띄운다. 그리고 각 줄에는 최대 72자까지만 작성하도록 한다.

### The Footer :
선택사항. issue를 Tracking하기 위한 Id를 넣는 용도로 사용한다.

### Example :

```
feat: Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

### 끝
아직 협업을 할 일이 많지는 않다, 하지만 개발자의 특성상 협업은 불가피하다. 지금부터 통일성있는 commit 습관을 만들고 개인적인 프로젝트도 규칙적인 message로 관리하자.




### Reference
https://udacity.github.io/git-styleguide/