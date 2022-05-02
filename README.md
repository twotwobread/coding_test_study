# coding_test_study
파이썬을 이용한 코테 스터디
- [스터디 진행 방식](#스터디-진행-방식)
- [git을 이용한 commit](#git을-이용한-commit)
- [commit 규칙](#commit-규칙)
- [pr 규칙](#pr-규칙)


---
## 스터디 진행 방식
### 1. 매주 실버:1, 골드:1, 삼성기출:2 문제 선정 후 풀기
### 2. 매주 일요일 13시 줌을 이용한 코드 리뷰 및 아이디어 공유
###   - 선정된 문제 중 1~2문제 선정 후 진행
###   - 자신이 푼 코드 첫 부분에 코드 풀이의 아이디어 작성 ( 아래 예시 참조 )
![image](https://user-images.githubusercontent.com/78334910/166247235-d3a51b4a-a51e-41e9-8e7b-28c19e6f1974.png)
###   - 코드 리뷰가 끝나면 팀원들의 피드백 및 질문  
---
## git을 이용한 commit
### 1. base가 되는 이 레파지토리 fork
![image](https://user-images.githubusercontent.com/78334910/166261228-f79ed1e6-5173-45a9-a7e3-50768eb29f33.png)
### 2. fork된 자신의 레파지토리의 주소 복사
![image](https://user-images.githubusercontent.com/78334910/166252211-08d1d8a7-fe6a-4ad4-a4a6-97e4746673c7.png)
### 3. git bash를 실행 후 원하는 디렉토리로 이동하여 git clone
![image](https://user-images.githubusercontent.com/78334910/166252587-14ea6ac0-efb6-4856-80fa-bea10e7c529f.png)
### 4. 자신의 github 닉네임으로 디렉토리 생성
![image](https://user-images.githubusercontent.com/78334910/166252871-514ad9ba-33f3-4296-90a8-c5631e3ced96.png)
### 5. 디렉토리 안으로 이동 후 자신의 코드 파일을 생성 후 git add
![image](https://user-images.githubusercontent.com/78334910/166253800-fbfa1e3f-af62-4f07-974e-08a92f9ba3d4.png)
#### ※ 아래와 같은 경고문 발생 시 화살표 부분과 같은 코드에 자신의 계정을 넣을 것!!
![image](https://user-images.githubusercontent.com/78334910/166254219-6cb2d576-3b10-4cf6-b900-72a7c1c75762.png)
### 6. 아래의 [commit 규칙](#commit-규칙)에 맞춰 git commit
![image](https://user-images.githubusercontent.com/78334910/166257199-a8d14302-8f92-40d9-a6a6-237f05e5966a.png)
### 7. push를 위한 git push
![image](https://user-images.githubusercontent.com/78334910/166257381-2c0928ae-04d9-4a7b-b828-82f0c0bee6f9.png)

---
## PR(Pull Request) 생성 - 자기 github에 잔디 채우기 위함.
### 1. fork해서 자신의 github에 생긴 레파지토리에서 pull requests 선택
![image](https://user-images.githubusercontent.com/78334910/166262145-f55f9935-5016-49cf-93d6-02216585330d.png)
### 2. New pull request 누르기
![image](https://user-images.githubusercontent.com/78334910/166262368-7949275d-aee9-4925-bd8b-88722a447b57.png)
### 3. Create pull request 누르기
![image](https://user-images.githubusercontent.com/78334910/166262808-2f9f6f16-1170-42b5-88ad-4c2bb6636e48.png)
### 4. 아래의 [pr 규칙](#pr-규칙)에 맞게 title 작성 후 create pull request
![image](https://user-images.githubusercontent.com/78334910/166264065-94da6496-3b4f-4229-81c2-262122ba2ce8.png)


---
## commit 규칙
### - commit 메세지 : 문제이름_난이도_풀이시간
### - description : 문제 주소
### - 위의 규칙을 이용한 터미널에서 git commit 방법
```
git commit -m "문제이름_난이드_풀이시간" -m "문제주소"
git commit -m "토마토_골드5_15분" -m "https://www.acmicpc.net/problem/7576"
```
---
## pr 규칙
### - PR title : 자신의 github 닉네임_월,주차_푼 문항 수
```
twotwobread_5월1주차_1문제
```
### - comment는 무관
---
