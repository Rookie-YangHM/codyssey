- Git Bast, Windows Terminal 설정을 포함한 설치
- Git 설정의 전역 범위
   - 개행문자 설정을 윈도우는 true, 맥은 input 값으로 지정
   - 사용자 이름과 이메일 주소 설정
   - 기본 브렌치 이름을 main으로 변경
- Git 전역 설정 목록을 확인하는 명령어
- Git 전역 설정을 에디터에서 띄워 전체 설정을 확인하는 법
- Git 의 기본 에디터를 Visual Studio Code 로 변경하는 법

---

- Git Bast, Windows Terminal 설정을 포함한 설치  
  Git Bash는 Windows에서 리눅스 명령어를 사용할 수 있게 해주는 터미널입니다. Windows Terminal은 다양한 쉘(Git Bash, PowerShell 등)을 한 곳에서 사용할 수 있게 해주는 터미널 앱입니다. Git을 설치할 때 Git Bash도 함께 설치되며, Windows Terminal에 Git Bash를 등록해두면 편리하게 사용할 수 있습니다.

- Git 설정의 전역 범위  
  Git의 설정은 시스템, 사용자(전역), 저장소(로컬) 단위로 나뉩니다. 전역 범위는 현재 로그인한 사용자 전체에 적용되는 설정입니다. 일반적으로 사용자 정보, 에디터, 개행문자 등 자주 사용하는 설정을 전역으로 지정합니다.

   - 개행문자 설정을 윈도우는 true, 맥은 input 값으로 지정  
     윈도우는 `core.autocrlf`를 `true`로, 맥/리눅스는 `input`으로 설정합니다. 이는 운영체제별로 개행문자(CRLF/LF) 차이로 인한 문제를 방지하기 위함입니다.  
     예시:  
       - Windows: `git config --global core.autocrlf true`  
       - Mac/Linux: `git config --global core.autocrlf input`

   - 사용자 이름과 이메일 주소 설정  
     커밋 기록에 남을 이름과 이메일을 전역으로 설정합니다.  
     예시:  
       - `git config --global user.name "홍길동"`  
       - `git config --global user.email "hong@example.com"`

   - 기본 브렌치 이름을 main으로 변경  
     새 저장소를 만들 때 기본 브랜치 이름을 `main`으로 지정합니다.  
     예시: `git config --global init.defaultBranch main`

- Git 전역 설정 목록을 확인하는 명령어  
  현재 적용된 전역 설정을 확인하려면 다음 명령어를 사용합니다.  
  예시: `git config --global --list`

- Git 전역 설정을 에디터에서 띄워 전체 설정을 확인하는 법  
  전역 설정 파일(`~/.gitconfig`)을 에디터로 열어 직접 확인하고 수정할 수 있습니다.  
  예시: `code ~/.gitconfig` (VS Code 기준)

- Git 의 기본 에디터를 Visual Studio Code 로 변경하는 법  
  Git에서 커밋 메시지 작성 등 에디터가 필요한 작업 시 VS Code를 기본 에디터로 지정할 수 있습니다.  
  예시: `git config --global core.editor "code --wait"`