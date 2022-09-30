# 안녕하세요
#주세용 세용이 주세용
>일반 테스트 형식 구문을 사용하는 마크업 언어의 일종인 마크다운은 사용법이 참쉽고 간결해요
>따라서 빠르게 문서정리가 가능합니다.
>단! 모든 HTML 마크업을 대체하지않습니다.
>HTML Markdown (마크업) <-> Markdown

> * 마크업 : 문서에서 특정 내용이 어떤 역할을 하는지 표시
> * 마크다운 : 번거로운 마크업의 태그를 더 간단한 기호로 표시



## 1.문법
### 1.1 Header
> 헤더는 제목을 표현할 떄 사용
> 단순히 글자 크기가 아니다.
> 의미적인 중요도!

# h1 태그
## h2 태그
### h3 태그
#### h4 태그
##### h5 태그
###### h6 태그

### 1.2 List
>목록 나열에 사용
* 순서가 있는 목록
1. 순서가 있는 항목
2. 순서가 있는 상위 항목
    1. 순서가 있는 하위 항목
    2. 순서가 있는 하위 항목
        1.  순서가 있는 하하위 항목

* 순서가 없는 목록
* 순서가 없는 상위 항목 
    * 순서가 없는 하위 항목
        * 순서가 없는 하하위 항목
        
### 1.3code block
> 코드 블럭은 작성한 코드를 정리, 강조할 때 사용
> 이것도 인라인과 블럭으로 나뉘어 사용가능 


* inline : 백틱을  한번 이용해 사용
    `consol.log('hello');`
* block : 백틱을 세번 이용해 사용
    ```javascript
    consol.log('hello');
    ```

    
### 1.4 이미지
>로컬 이미지 삽입 또는 링크 활용해 삽입가능
* ![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAT4AAACfCAMAAABX0UX9AAAAbFBMVEX///8AAADT09NISEg4ODjQ0NAeHh7W1tYRERH5+flnZ2dZWVkYGBiwsLDy8vKYmJjo6OjIyMj19fXCwsIvLy+QkJC3t7eqqqpFRUXj4+MNDQ2fn59NTU2Dg4NdXV0qKiojIyN9fX1ubm48PDw6tcSpAAADi0lEQVR4nO3da3eaMACA4cSqoGuZtWrFWm/9//9xp1wDhOAaDKfkfT5tJS2Hd1YwXCYEAAAAAAAAAAAAAAAAAAAAAAAARiwKJk4Fq6G3uEfr7ZN0bL+Nht7qvry5bpfaDb3d/dgNU0/K96G3vA+ToepJ+Tr0tttbH4fLt//973/5G1/4NXVnnq3097/9ndINeXO71tcwffm5XesDPCfb8eF6te/pv5rr1fYu/c2duF5tMB9Tvpnr1ZLPCvmskM8K+ayQzwr5rJDPynjzxUGp7TN9pIzRThwvlAGBZvlo8y3+HJ5zh5O+33oalmOWuhErWQwIz5ofMuJ86pzSp/abluqQlnylub/5tJMJ28oI8hnyyeZepXZuhHymfJf6riGoLiefMZ98qn5DVJ/dJ58xX233caovJp85X+WM4raxlHwd+WR54Ks5KUy+rnyXOFsYN5eRrzOfPGXL9uSrui+fvCbLGrsN8t2XL9l9/NUuId8d+Q4z8apdQL578snD5Ey+hrvztSIf+X7KnG8u9Z7JlzLne9MeqsirOmdFvtZ8O93HDDmNPv4r37q53I98L9qjlVnlCLDIt1iUP0XNd1G+npf0JZ/mWHkn9Pmi06a4fnSjfkP55fMtG+tNvup5IZlO/2nzaScUqoqrmf3JJyqvJLn8/lXU5xPxxVxvU4z0KF9QiZK8flryiZmx3jkuBnqUT919hGmBtnzGO5TmyuUGPuUTH/UvtObLr/nWUa/e9yqfuGV/v2Z/b8/XMqul/KyEX/mifbWUIZ+43lHPs3zpYfCmOGNuytc40klsq2M8y5fsPsq3fmM+oZmzqdXzLp/Yqqd7zfnWjburb/Uh3uUT6p/N+cR6Wqu3qI/wL5+qI5+IK59Ujs0ZK/KZ8omZMqG60Vy+Sz5jPuWTyibWLCafOZ94yZfr6pGvK19+NZH+ngfydeVLr2VruU2dfJ35vvu1PWxkzPnCzKF167fFmDC/+kpjsdTf1yBGnE/Es1LbXUUrZYx215BqHC0XxpvPCfJZIZ8V8lkhnxXyWSGfFfJZGVc+nmH1Q+mT4Jw/BzObznK92t6lEwQHx7+92Yvvy+1aHyC/KOV8fHLmmJ8JaZvQ+T0adzc79DWCh1+bryl7KMdP/HwMwzVRj+X8iZ+PMdBzr0fx1Otv0ee0e2v7Nf0cwfteYcX/mAAAAAAAAAAAAAAAAAAAAAAAAIAe/QPfUjco97t4cwAAAABJRU5ErkJggg==)

# 1.6 table
> 표를 작성
* `|` 파이프 사이에 컬럼

|이름|학과|학번|나이|


## 1.7 기타
>인용문 : `>`
>수평선  : `---`
강조 : `*이태리*`, `*주세용*`


## GIT
코드 관리, 협업, 배포

##CLI (Command line Interface)
커맨드(명령어)를 통해 작동하는 인터페이스
< - > GUI(Graphic User Interface)

1.pwd : 현재 폴더의 경로

2.ls : 현재 폴더 내용물

3.cd : 폴더 변경

4.mkdir : 폴더 생성

5.rm : 폴더 삭제

6.touch : 파일 생성

7.cp : 파일복사

8.mv : 파일/폴더 이동
