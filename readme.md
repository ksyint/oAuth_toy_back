# toy project - oAuth2.0
## 구현 사항
1. 카카오, 구글의 소셜 로그인이 수행 되어야 합니다.
2. api는 세가지 종류의 api가 필요합니다.
    1. 구글/카카오 로그인용 api
        * 시간이 부족하시면 둘 중 하나는 생략하셔도 됩니다.
    3. 로그아웃 api
    4. 인증용 api
        * authentication token을 받고 사용자를 인증합니다.
3. 
4. 두분이서 위의 사항을 모두 만족하셨다면, 함께 작업했던 branch에 회고(아래 참고)와 함께 Pull Request를 날려주세요.
기한: 11/21

### 해결해야할 핵심 문제들
<details>
<summary>스스로 생각해볼 수 있다면 혼자서 해보기!</summary>
<div markdown="1">

1. react에서 state는 창이 새로고침되면 사라진다. 그러나 일반적인 페이지는 새로고침시에도 로그인이 유지된다. 이를 어떻게 해결할 것인가?
    * 사용 스택
        * react hook (useState, useEffect)
        * axios
2. 로그인 테스팅을 실행할때, 테스팅을 어떻게 실행할 것인가?
    * api만 따서?
    * state에 따른 component안에 있는 text?
    * 잘 조합해서 사용해보자
    * 만약 필요하다면 enzyme 등의 다른 testing library를 사용해도 무방하다.
        * 설치가 어려우시면 도와드리겠습니당
</div>
</details>

## 실행 방법
1. 먼저 python3가 설치되어있어야 합니다. (2는 안돼요..ㅠㅠ)
2. 다음의 명령어를 실행합니다.
    ```bash
    # 미리 가상환경에서 설치하는걸 추천합니다.

    pip install -r requirements.txt
    pre-commit install -t commit-msg -t pre-commit
    python manage.py runserver
    ```

## 참고 자료
### testing
* jest docs - https://jestjs.io/
* react testing docs - https://testing-library.com/docs/react-testing-library/intro/
### 구현
* https://www.hacksoft.io/blog/google-oauth2-with-django-react-part-2
### 디자인
* oAuth2.0 디자인 가이드
    * https://developers.google.com/identity/branding-guidelines
    * https://developers.kakao.com/docs/latest/ko/reference/design-guide

## 회고합시다!
**develop branch에 PR을 날릴때 항목별로 한줄 회고를 남겨주세요** 실제 프로젝트 진행할때 반영하겠습니다.
1. 프로젝트를 진행하면서 가장 어려웠던 부분은? (테스팅? linting? git? 구현?)
2. 프로젝트를 진행하면서 불필요하다고 생각되었던 부분은? (ex. 과도한 linting 규칙, testing)
