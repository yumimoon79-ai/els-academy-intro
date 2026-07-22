# ELS 영어수학학원 학원소개 페이지 (GitHub Pages)

네이버 블로그 홈페이지형 위젯에서 연결할 **학원소개 웹페이지**입니다.

## 폴더 구성

- `index.html` : 학원소개 메인 페이지
- `.nojekyll` : GitHub Pages가 파일을 그대로 배포하도록 하는 빈 파일
- `assets/` : 페이지에 사용되는 이미지 (지금은 임시 placeholder)
- `naver-widget-code.txt` : 네이버 블로그 위젯 연결 코드
- `_make_placeholders.py` : 임시 이미지 다시 만들 때 쓰는 스크립트 (업로드 안 해도 됨)

---

## 1. 먼저 수정할 내용

`index.html` 을 VS Code로 열고 아래를 검색해서 바꾸세요.

1. `0324650182` → 실제 상담 전화번호
2. `카카오톡 상담` 버튼의 `href="#"` → 실제 카카오톡 채널 URL
3. `학원 위치` 버튼의 `href="#"` → 네이버 플레이스/지도 URL
4. 하단의 학원 주소와 등록 학원명
5. 원장 소개·프로그램 문구에서 고칠 부분

## 2. 이미지 교체

`assets` 폴더의 파일과 **똑같은 파일명**으로 새 사진을 저장하면 HTML 수정 없이 바뀝니다.

- `hero.jpg` : 첫 화면 대표 이미지
- `director.jpg` : 원장 소개 사진
- `english-class.jpg` : 영어 수업 사진
- `math-class.jpg` : 수학 수업 사진
- `learning-system.jpg` : 학습관리 앱·리포트 이미지
- `academy-space.jpg` : 학원 전경·교실 사진

권장: 가로 1600px 이상, JPG

## 3. GitHub 저장소 만들기

1. GitHub 로그인 → 우측 상단 `+` → `New repository`
2. Repository name: `els-academy-intro`
3. `Public` 선택 → `Create repository`

## 4. 파일 업로드

이 폴더 안의 `index.html`, `.nojekyll`, `assets` 폴더를 저장소에 올립니다.
(웹 업로드 시 `uploading an existing file` 사용, 또는 git push)

> 주의: 바깥 폴더가 아니라 그 **안의 파일들**이 저장소 첫 화면에 보여야 합니다.

## 5. GitHub Pages 공개 설정

1. 저장소 `Settings` → 왼쪽 `Pages`
2. Source: `Deploy from a branch`
3. Branch: `main`, Folder: `/(root)` → `Save`

공개 주소:

```
https://YOUR-GITHUB-ID.github.io/els-academy-intro/
```

## 6. 네이버 위젯 연결

`naver-widget-code.txt` 를 열고, 위 공개 주소를 학원소개 클릭 영역의
`href` 에 넣습니다. (자세한 코드는 파일 참고)

## 꼭 확인할 것

- 모바일에서 잘 보이는지
- 전화 버튼이 실제 연결되는지
- 카카오톡·네이버 지도 링크가 열리는지
- 실제 학생 사진 사용 시 초상권 동의를 받았는지
- 공개하면 HTML과 사진이 인터넷에 공개된다는 점
