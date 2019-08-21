# Web Crawling!
> ~ 19.05.27
> 멋쟁이사자처럼 7기 스터디

<br>

## 목차
1. 셀레니움
2. 실행

<br> 

## 1. 셀레니움
웹 자동화 작업을 도와주는 라이브러리 (웹 드라이버)입니다.<br>
자동으로 돌아가는 웹 메크로를 만들어 브라우저에 있는 정보를 긁어모으는 원리입니다.<br>
셀레니움을 통해 자동 로그인, 웹에 있는 버튼 누르기, 그리고 동적 웹 크롤링이 가능해집니다.

<br>

## 2. 실행

>1. 자동 로그인 (auto_login.py) <br>
포털 사이트 Naver 를 활용합니다. <br>
아이디 값과 비밀번호 값을 미리 입력해놓은 뒤에 자동으로 로그인하도록 설정합니다.

>2. 네이버 웹툰 제목 크롤링 (webtoon_title.py) <br>
네이버 웹툰 사이트를 활용합니다. <br>
버튼을 눌러 페이지를 넘겨가면서 웹툰의 제목들을 가져옵니다. <br>

>3. 네이버 생활뉴스 랭킹 30 제목 크롤링 (article_ranking_title.py) <br>
네이버 뉴스 사이트를 활용합니다. <br>
뉴스 랭킹 30의 제목을 긁어옵니다. <br>

>4. 네이버 생활뉴스 랭킹 30 기사마다 댓글 수집 (article_ranking_comment.py) <br>
3에서 이어집니다.<br>
뉴스 랭킹 30의 제목과 링크를 추출하여 배열에 저장합니다. <br>
추출한 링크를 바탕으로 댓글을 모아 사전형 자료에 정리합니다. <br>