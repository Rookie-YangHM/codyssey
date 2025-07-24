# 문제_7 브랜치? 브런치?

## 기술적설명
<p>운영진이 홈페이지에 <strong>사람 얼굴 이미지</strong>를추가하자는 아이디어를 냈다. 여기에 더해, <strong>고객이 직접 텍스트를 입력하고, 언어를 선택하여 음성으로 출력되는 기능</strong>이 있으면 좋겠다는 요청도 추가되었다. 상우는 이 기능을 안전하게 실험할 수 있도록 <strong>새로운 브랜치</strong>를 만들어 개발하기로 했다.</p>
<h1>수행과제</h1>
<ul>
<li><code>add-image</code>라는 이름의 브랜치를 생성하고 해당 브랜치로 전환한다.</li>
<li>기존 <code>david</code> 디렉토리 안에 다음 구조를 생성한다:<ul>
<li><code>/static/david.jpg</code> (이미지 파일 저장)</li>
<li><code>/templates/index.html</code> (HTML 폼 및 결과 페이지)</li>
</ul>
</li>
<li>다음과 같은 기능을 <code>app.py</code>에 구현한다:</li>
</ul>
<h3>🔽 주요 기능 요구사항</h3>
<ul>
<li><code>GET</code> 요청 시 입력 폼을 제공하는 페이지 렌더링</li>
<li><code>POST</code> 요청 시:<ul>
<li>사용자가 입력한 텍스트와 선택한 언어를 기반으로 TTS 변환 수행</li>
<li>변환된 음성을 페이지 내에서 바로 재생</li>
</ul>
</li>
<li>기본 언어는 <code>ko</code>, 선택 옵션으로 <code>en</code>, <code>ja</code>, <code>es</code> 등을 제공</li>
<li>예외 상황(예: 빈 텍스트 입력, gTTS 실패)에 대한 안내 메시지 제공</li>
</ul>
<h3>🔽 HTML 입력 폼 예시 (<code>index.html</code>)</h3>
<pre><code class="language-html">&lt;form method="POST"&gt;
  &lt;label&gt;이름 또는 문장을 입력하세요:&lt;/label&gt;
  &lt;input type="text" name="input_text" required=""&gt;
  
  &lt;label&gt;언어 선택:&lt;/label&gt;
  &lt;select name="lang"&gt;
    &lt;option value="ko"&gt;한국어&lt;/option&gt;
    &lt;option value="en"&gt;영어&lt;/option&gt;
    &lt;option value="ja"&gt;일본어&lt;/option&gt;
    &lt;option value="es"&gt;스페인어&lt;/option&gt;
  &lt;/select&gt;

  &lt;button type="submit"&gt;음성 듣기&lt;/button&gt;
&lt;/form&gt;

{% if error %}
  &lt;p style="color:red;"&gt;{{ error }}&lt;/p&gt;
{% endif %}

{% if audio %}
  &lt;audio controls="" autoplay=""&gt;
    &lt;source src="data:audio/mpeg;base64,{{ audio }}"&gt;
  &lt;/audio&gt;
{% endif %}</code></pre>
<h3>🧠 Flask 예시 코드 주요 내용 (<code>app.py</code>)</h3>
<ul>
<li><code>request.method == 'POST'</code>일 때 사용자 입력과 언어를 처리</li>
<li><code>try-except</code>로 오류 처리 및 사용자 피드백</li>
</ul>
</td>

## 개발환경
<td colspan="3" class="tal fs13 py8 editor"><h1>개발환경</h1>
<ul>
<li>Visual Studio Code만을 사용하여 코드 편집 및 실행할 것</li>
<li>HTML 템플릿, 이미지, Flask 코드 모두 <code>add-image</code> 브랜치에만 반영할 것</li>
<li>서버 포트는 80번으로 고정</li>
</ul>

## 제약조건
<h1>제약사항</h1>
<ul>
<li>Visual Studio Code만을 사용하여 코드 편집 및 실행할 것</li>
<li>HTML 템플릿, 이미지, Flask 코드 모두 <code>add-image</code> 브랜치에만 반영할 것</li>
<li>서버 포트는 80번으로 고정</li>
</ul>
<h1>보너스 과제</h1>
<ul>
<li><code>lang</code> 값이 유효한 값인지 서버 측에서 검증하고 잘못된 값이면 오류 반환</li>
<li>브라우저에서 재생한 음성을 <code>.mp3</code>로 저장할 수 있는 링크 제공</li>
<li>음성은 <code>base64</code> 인코딩 후 HTML에 직접 삽입</li>
<li>사용자의 입력 내역을 로그 파일로 저장 (<code>input_log.txt</code>)</li>
</ul>
