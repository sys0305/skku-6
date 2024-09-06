# 연습문제

1. board_list라는 view function 만들기
2. 127.0.0.1:8000/board 에 접속하면 해당하는 view function이 호출되도록 url연결.
3. 해당하는 view function은 우리가 bootstrap에서 만든 board-list.html이 rendering되도록 구성.
4. DB에 저장되어 있는 Board들이 board-list.html에 렌더링 되도록 view function 수정.

# Extension 설치

1. vscode-extension unibeautify 검색 후 설치
2. project-root에서 .vscode라는 폴더 만든 후 settings.json이라는 파일 만들기

```
{
  "html.format.templating": true,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "emmet.includeLanguages": {
    "django-html": "html"
  },
  "unibeautify.enabled": true,
  "[django-html]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "Glavin001.unibeautify-vscode"
  }
}
```
