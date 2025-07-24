


## 🧪 Mission 01 - Git 기본 설정을 해봤음

### ✅ Git을 설치했음
- Git 공식 웹사이트에 들어가서 Git을 다운로드하고 설치했음.
- Windows에서는 Git Bash와 Windows Terminal도 함께 설치했음.
- Windows Terminal이 없을 경우, Microsoft Store에서 따로 설치했음.

### ✅ Git 전역 설정을 했음
- 줄바꿈 설정을 운영체제에 맞게 설정
  - Windows에서는 아래 명령어를 입력 :
    ```
    git config --global core.autocrlf true
    ```
  - macOS에서는 아래 명령어를 입력했음 :
    ```
    git config --global core.autocrlf input
    ```
- 사용자 이름(`user.name`)과 이메일 주소(`user.email`)도 설정 :
  ```
  git config --global user.name "내이름"
  git config --global user.email "내이메일@example.com"
  ```
- 기본 브랜치 이름을 `master` 대신 `main`으로 설정 :
  ```
  git config --global init.defaultBranch main
  ```

### ✅ Git 설정 확인
- `git config --list` 명령어로 설정된 내용을 확인
- `git config --global -e` 명령어로 전역 설정파일을 에디터로 열어 확인

### ✅ 기본 에디터를 바꿨음
- Git의 기본 에디터를 Visual Studio Code로 바꾸는 설정을 했음.
  ```
  git config --global core.editor "code --wait"
  ```

### ✅ 작업 디렉토리에 Git 저장소를 만들었음
- `app.py` 파일이 있는 디렉토리로 이동했음.
- `git init` 명령어를 실행해서 Git 저장소를 생성했음.

```
이렇게 Git의 기본 설정을 모두 마쳤음 👍
```