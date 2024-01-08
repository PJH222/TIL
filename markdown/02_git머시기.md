

## git 명령어
### git init >> master 되려면~~~

### git status
#### git init 직후
```
PS C:\Users\장훈\test> git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

#### a.text 파일생성 직후

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)

커밋 될 것이 아직 add 되지 않았지만, 추적되지 않은 파일들이 있음
```


#### git add a.txt
- .txt없이 쓰면 폴더 추가
```
커밋 될 수 있는 변화가 생김

```


## git commit -m "메세지"
- 만약 최초로 add 한 이후의 파일이 있다면, 
`git commit -am "메세지"`로 한번에 **add와 커밋**까지 할 수 있음.
- `git commit`만 치는 경우, 여러 줄의 커밋 메세지를 작성할 수 있다.
- 디폴트로 설정된 txt에디터를 수정할 수 있다.  

## 여기까지 순서로 보자면,,,
- 파일 만들고 > git add > git commit > git status로 하면 정상적으로 스테이지로 올라감

## git config
* git config --global user.email
* git config --global user.email "이메일 주소"
* git config --global user.name
* git config --global user.name "사용자명"


## cat `파일이름`
그 파일의 내용을 보는 것

## nano `파일명`
해당 파일의 세부사항 수정 및 새로 만들기

## git log 
- git의 히스토리 살피기 
- show version
## git log --stat
- git의 상세 히스토리 살피기
## git log -p
- 각 버젼별로 변경 사항에 대해 표시
## git log --oneline
- 간단하게 표기 (7글자만 표기됨)

## git diff
- 변화된 내용을 보여줌
- 마지막 버젼과 워킹 트리와의 차이를 보여줌
```
$ git diff
diff --git a/abc.txt b/abc.txt
deleted file mode 100644
index e69de29..0000000
diff --git a/b.txt b/b.txt
deleted file mode 100644
index 561285e..0000000
--- a/b.txt
+++ /dev/null
@@ -1,3 +0,0 @@
-잠와 죽는다아아앙...
-
-
```


## git reset --hard
- 지금까지 한 작업 제거
- 이전 버전으로 돌아간다~~
- `--hard`를 `--mixed or soft`로 바꾸면 작업 내용이 삭제되진 않는다.
  


_create read update delete <<이정도 알면 버젼관리에 대해 꽤 아는 것이다>>_
`CRUD`
## ls -al
- 숨겨진 파일도 모두 보기

## git checkout `commit ID`
- 해당 커밋이 있는 버젼으로 되돌아가기
- 그 버전에서 없었던 파일이면 기존에 있던 파일이 나타나지 않음
- 단, 삭제가 된 것은 아님
- `master` 가장 최신의 커밋 버젼으로 돌아가기
  
## git config --global core.editor "nano"


## git revert nano




