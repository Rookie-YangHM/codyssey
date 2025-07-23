<p>정말 아주 심플한 웹 페이지 하나 올렸을 뿐인데 놀라운 반응이 왔다. 하루에도 1000명 이상의 사용자들이 웹 페이지를 접근했고 관련한 문의 전화가 꽤 많이 왔다. 물론 상우는 자기가 만든 홈페이지가 대단한 건 아니라는 것을 잘 알고 있었다. 그 보다는 원래 반달곰 커피를 고집스럽게 잘 꾸려온 아버지 덕분이라는 것을 잘 알고 있었다.</p>
<p>그런데 홈페이지가 성과를 보이기 시작하니까 홈페이지에 대한 이런저런 요구 사항들이 많아지기 시작했다. 상우는 요구 사항을 체계적으로 업데이트하기 위해서는 혼자서 작업하더라도 버전 관리(Version Control)가 필요하다는 생각을 하기 시작했다.</p>
<p>‘그래 이럴 때 쓰라고 Git이 있는 거야’</p>
<p>상우는 그렇게 Git을 사용할 준비를 하기 시작했다.</p>
<h1>수행과제</h1>
<h3>✅&nbsp;1. 기초 git 환경 구축</h3>
<ul>
<li>Git을 공식 사이트에서 PC에 다운 받아 설치한다. 이때 윈도우는 Git Bash와 Windows Terminal 설정을 포함해서 설치한다. 윈도우에 Windows Terminal이 없으면 설치한다.</li>
<li>Git의 설정을 전역 범위로 아래와 같이 적용한다.<ul>
<li>개행문자 설정을 윈도우는 true, 맥은 input 값으로 지정한다.</li>
<li>사용자 이름과 이메일 주소를 설정한다.</li>
<li>기본 브랜치 이름을 main으로 변경한다.</li>
</ul>
</li>
<li>Git 전역 설정 목록을 명령어로 확인한다.</li>
<li>Git 전역 설정을 에디터에서 띄워서 전체 설정을 확인한다.</li>
<li>Git의 기본 에디터를 Visual Studio Code로 변경한다.</li>
<li>app.py가 저장되어 있는 작업 디렉토리로 이동하여 git 저장소를 생성한다.</li>
</ul>
<h3>✅&nbsp;2. 최소값 최대값 <strong>프로그램 구현하기 -</strong> <code>**minmax_calculator.py**</code></h3>
<ul>
<li><p>입력된 숫자들 중 <strong>최소값(minimum)</strong> 과 <strong>최대값(maximum)</strong> 을 출력하는 프로그램을 작성한다.</p>
<h3>파이썬 계산기 <strong>기능 요구사항</strong></h3>
<h3>📌 <strong>기능 요구사항</strong></h3>
<ul>
<li><p><strong>입력 예시</strong></p>
<pre><code class="language-css">3 9 1 4 2</code></pre>
</li>
<li><p>입력된 숫자중 최대값 최소값 출력</p>
</li>
<li><p><strong>예외 처리</strong></p>
<ul>
<li>숫자 이외의 값이 입력될 경우 <code>"Invalid input."</code>을 출력한다.</li>
</ul>
</li>
<li><p><strong>출력 예시</strong></p>
<pre><code class="language-css">Min: 1.0, Max: 9.0</code></pre>
</li>
</ul>
<hr>
<h3>🧱 <strong>구현 방식 및 기술 요구사항</strong></h3>
<ul>
<li>Python 내장 함수 <code>min()</code>과 <code>max()</code> 사용을 <strong>금지한다</strong>.</li>
<li>입력값 처리는 반드시 터미널에서 <code>input()</code>을 사용한다.</li>
<li>입력된 숫자는 공백으로 나누어 처리한다. (<code>split()</code> 활용)</li>
<li>숫자로 변환 시 <code>float()</code>를 사용한다.</li>
<li>반드시 다음과 같은 블록으로 실행한다.</li>
</ul>
<pre><code class="language-css">if __name__ == "__main__":
    main()</code></pre>
</li>
</ul>

<ul>
<li>Git은 2.28.0 버전 이상을 사용한다. (해당 버전 이상부터 main 브랜치가 기본으로 설정 가능하다.)</li>
<li>Git에서 기본 제공되는 명령어로 터미널에서 실행하며 별도의 GUI 도구를 사용하지 않는다. 윈도우는 Windows Terminal에서 Git Bash로 작업한다. 맥과 리눅스는 OS에 포함된 Terminal을 사용한다.</li>
</ul>

<h1>제약사항</h1>
<ul>
<li>Git은 2.28.0 버전 이상을 사용한다. (해당 버전 이상부터 main 브랜치가 기본으로 설정 가능하다.)</li>
<li>Git에서 기본 제공되는 명령어로 터미널에서 실행하며 별도의 GUI 도구를 사용하지 않는다. 윈도우는 Windows Terminal에서 Git Bash로 작업한다. 맥과 리눅스는 OS에 포함된 Terminal을 사용한다.</li>
</ul>
<h1>보너스 과제</h1>
<ul>
<li>버전 관리 시스템의 종류 3가지를 Markdown 문서로 제출한다.</li>
<li>.git 디렉토리의 역할의 의미를 Markdown 문서로 제출한다.</li>
<li>파일명은 git_directory.md로 저장한다.</li>
<li>작업 디렉토리에 .git디렉토리를 삭제한 후 git의 상태를 확인한다. 휴지통에서 .git디렉토리를 복원한 후 git의 상태를 확인한다.</li>
</ul>
