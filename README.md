# 1주차 과제

1주차 과제 목표!

1. 스스로 Django 페이지를 만들어서 서버를 돌리기
2. Django templates에 1주차에 배웠던 네이버 클론코딩처럼 원하는 페이지를 본따서 그에 맞게 꾸미기



## 과제는 Branch를 만들어서 제출하기

### Branch 이름 통일하기

영어이름/hw1

### Branch 만든 후 Branch에 올리는 법

1) 내가 올리고 싶은 폴더 위치로 Terminal을 이동시킨다.

2) 나만의 브랜치를 만든다

```bash
$ git branch gyuri/hw1
```

3) 브랜치가 생성되었는지 확인한다.

```bash
$ git branch
```

-> 확인해 보면 브랜치에 gyuri/hw1 브랜치와 *master 브랜치가 있다는 것을 확인할 수 있음.

- master앞에 `*`의 의미는 현재 나의 위치가 master라는 것. 과제를 올리기 위해서는 내 브랜치로 위치를 옮겨야 한다.

4) 내 브랜치로 위치 옮기기

```bash
$ git checkout gyuri/hw1
```

-> 이를 시행한 후에 git branch로 확인을 해보면 `*`별표가 gyuri/hw1로 이동함을 확인할 수 있다.

5) 폴더 내용 git에 올리기

```bash
$ git init
$ git add . 
$ git commit -m "커밋메세지 적으시오"
$ git push origin gyuri/hw1
```

- git add . 은 나의 모든 폴더를 올린다는 뜻. 일부의 폴더만 올리고 싶으면 폴더 이름을 명시하거나 .gitignore 파일 만들어서 올리고 싶지 않은 파일 거기에 쓰기

  --> gitignore모르시는 분은 구글에 꼭 검색해보기

- push를 할 때에는 자기의 브랜치 이름으로 push하기



--끝!!!--

## 참고자료

[html과 css 연동하는 법](https://m.blog.naver.com/shino1025/221320924962)


