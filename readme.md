# toy project - oAuth2.0
## 구현 사항
1. swagger UI로 api의 구체적 명세를 디자인 한 후, front쪽에 넘겨주세요
    * https://editor.swagger.io/ 여기서 디자인을 한뒤 json으로 변환하셔도 되고
    * https://stackoverflow.com/questions/34733253/converting-a-swagger-yaml-file-to-json-from-the-command-line
        * 여기 참고하셔서 yaml 파일을 json으로 변환하셔도 됩니다.
2. 카카오, 구글의 소셜 로그인이 구현 되어야 합니다.
3. api는 세가지 종류의 api가 필요합니다.
    1. 구글/카카오 로그인용 api
        * 시간이 부족하시면 둘 중 하나는 생략하셔도 됩니다.
    3. 로그아웃 api
    4. 인증용 api
        * authentication token을 받고 사용자를 인증합니다.
4. 두분이서 위의 사항을 모두 만족하셨다면, 함께 작업했던 branch에 회고(아래 참고)와 함께 Pull Request를 날려주세요.

## 현재 적용된 규칙들
1. commitlint
    * commit message의 형태는 다음과 같아야 합니다.
    * [commit message convention](https://github.com/DevKor-Team/devkor_hackathon_back/blob/develop/.github/COMMIT_MESSAGE_CONVENTION.md)
    * 만약 commit message의 포맷이 맞지 않으면, commit이 되지 않습니다.
2. black
    * 이 프로젝트에서는 Black라고 하는 automatic code formatter를 사용합니다. 코드를 짠 후에는 `pre-commit run`를 실행해주세요.
    * 이를 실행하지 않더라도 commit 시에 자동으로 검사하게 됩니다. 이때 스타일에 맞지 않은 것이 있을 경우 자동으로 수정되며, 이를 다시 한번 git add 으로 반영한 후 commit 하셔야합니다.


## 해결해야할 핵심 문제들
<details>
<summary>스스로 생각해볼 수 있다면 혼자서 해보기!</summary>
<div markdown="1">

1. oAuth시 유저 인증을 어떻게 해야할까?
    * 유저 information을 oAuth의 어느 flow에서 저장할 것인가?
    * 한번 회원가입을 완료한 유저는 어떻게 인증할 것인가?
        * 사실 oAuth에서 회원가입과 인증의 과정은 크게 다르지 않습니다.
2. (선택) oAuth 테스팅을 실행할때, 테스팅을 어떻게 실행할 것인가?
    * api를 어떻게 선언해야할까..?
        * https://swagger.io/docs/specification/authentication/oauth2/ 를 참조해볼것!
        * 저도 처음 해보는 부분이라 선택으로 남겨놓았고, 같이 고민해봤으면 좋겠어요.

</div>
</details>

## 실행 방법
1. 먼저 python3가 설치되어있어야 합니다. (2는 안돼요..ㅠㅠ)
2. 다음의 명령어를 실행합니다.
    ```bash
    # 미리 마련해둔 가상환경에서 설치하는걸 추천합니다.
    # 가상환경 폴더가 git에 탐지되지 않도록 gitignore에 추가해주는것도 잊지 마시고!

    # virtualenv venv 
    # source venv/Scripts/activate

    pip install -r requirements.txt
    pre-commit install -t commit-msg -t pre-commit
    python manage.py runserver
    ```

## 참고 자료
### testing
* https://swagger.io/solutions/api-testing/
* https://www.django-rest-framework.org/api-guide/testing/
    * django drf는 맨 위에 인용된 문서를 읽어보는것도 좋더라구요.. 개인적으로 도움 많이 되었음
### 구현
* https://www.hacksoft.io/blog/google-oauth2-with-django-react-part-2

## 회고합시다!
**develop branch에 PR을 날릴때 항목별로 한줄 회고를 남겨주세요** 실제 프로젝트 진행할때 반영하겠습니다.
1. 프로젝트를 진행하면서 가장 어려웠던 부분은? (테스팅? linting? git? 구현?)
2. 프로젝트를 진행하면서 불필요하다고 생각되었던 부분은? (ex. 과도한 linting 규칙, testing)
