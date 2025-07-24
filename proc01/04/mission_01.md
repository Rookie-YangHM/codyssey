


## 🧪 Mission 01 - Git 기본 설정

### ✅ Git을 설치
- Git 공식 웹사이트에 들어가서 Git을 다운로드하고 설치
- Windows에서는 Git Bash와 Windows Terminal도 함께 설치 (상세)
  1) **Git for Windows 설치** (https://git-scm.com/download/win)
     - 설치 중 **Select Components** 단계에서 `Git Bash Here`를 체크.
     - **Adjusting your PATH environment**: `Git from the command line and also from 3rd-party software` 선택.
     - **Choosing the default editor used by Git**: VS Code를 쓸 거라서 `Use Visual Studio Code as Git's default editor` 선택.
     - **Choosing the default branch name for new repositories**: `main`을 기본 브랜치로 선택(가능한 버전일 경우).
     - **Configuring the line ending conversions**: Windows라서 `Checkout Windows-style, commit Unix-style line endings (recommended)` 선택.
     - 그 외 옵션은 기본값으로 두고 설치 종료.
  2) **Windows Terminal 설치**
     - **Microsoft Store**를 열고 `Windows Terminal`을 검색해 설치.
     - 설치 후 실행해서 **Settings(설정) → Default profile**을 `Git Bash`로 변경.
       - 만약 목록에 `Git Bash`가 없다면 **Add new profile → New empty profile**을 눌러 아래처럼 설정:
         - **Command line**: `"C:\\Program Files\\Git\\bin\\bash.exe" -li`
         - **Name**: `Git Bash`
         - **Starting directory**: `%USERPROFILE%` (기본값 사용해도 됨)
     - 저장(Save)해서 Windows Terminal을 열면 기본으로 Git Bash가 뜨도록 설정.
  3) **VS Code를 터미널에서 `code` 명령으로 실행 가능하게 설정**
     - VS Code 실행 → **Command Palette**(`Ctrl+Shift+P`) → `Shell Command: Install 'code' command in PATH` 실행.

### ✅ Git 전역 설정
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
- `git config --global --list` 명령어로 설정된 내용을 확인
- `git config --global -e` 명령어로 전역 설정파일을 에디터로 열어 확인

### ✅ 기본 에디터를 바꿨음
- Git의 기본 에디터를 Visual Studio Code로 바꾸는 설정을 했음.
  ```
  git config --global core.editor "code --wait"
  ```

### ✅ 작업 디렉토리에 Git 저장소를 작성
- `app.py` 파일이 있는 디렉토리로 이동
- `git init` 명령어를 실행해서 Git 저장소를 생성

```
이렇게 Git의 기본 설정을 모두 마쳤음 👍
```