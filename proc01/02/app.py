from flask import Flask

# Flask 프로그램을 만들고, app이라는 변수에 저장
app = Flask(__name__)

# 인터넷 주소('/')로 접속하면 hello_world 함수를 실행
@app.route("/")
def hello_world():
  """
  '/' 주소로 접속했을 때 "Hello, DevOps!"라는 글자를 출력하는 함수
  """
  return "Hello, DevOps!"

if __name__ == "__main__":
  # app.run()은 웹 서버를 실행하는 명령어
  # host='0.0.0.0'은 컴퓨터의 모든 인터넷 주소에서 접속할 수 있게 해줌
  # port=8080은 8080번 포트로p 접속하라는 의미
  app.run(host='0.0.0.0', port=8080)
