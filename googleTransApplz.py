import sys
import googletrans  # googletrans 4.0의 최신판과 PyQt5 최신판을 먼저 인스톨.

from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5 import uic   # 이상의 다섯 줄 코딩으로 작업을 하기 위한 환경설정이 모두 끝남. uic가 빨강 불로 에러가 나는 경우에는 우측상단 모서리에서 확인하여 system interpreter로 설정해주어야 하는 경우가 있음. 아나콘다와 같이 설치될 때 그런 에러가 나는 경우가 있음.


form_class = uic.loadUiType("ui/google_ui_first.ui")[0]   # form_class 는 작명을 하면 되는 것. 확장자까지 써준다. 파이썬 파일과 종류가 다르니까 ui와 같이 별도의 디렉토리를 만드는 것이 좋다.
# 윗줄의 코딩이 디자인한 외부 ui를 불러와서 저장한 것.


class GoogleTrans(QMainWindow, form_class):

    def __init__(self):  # 생성자 만드는 것은 자동완성을 이용
        super().__init__()  # 부모 클래스 생성자 호출.
        self.setupUi(self)  # 불러온 ui파일을 연결. 윗줄들과 이줄은 무조건 해준다고 생각할 것.

        # 이하는 각 옶션들 코딩
        self.setWindowTitle("구글 한줄 번역기 만들기 연습")  # 윈도우 타이틀. 자동완성이 안 되니까 스펠링 오타에 철저히 주의
        self.setWindowIcon(QIcon("icon/google.png"))  # 윈도우 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 Made by Chihwan Group")  # 맨 밑의 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action)  # 이것이 signal에 해당
        # self.init_btn.clicked.connect(self.init_action)

        # 인풋을 가져와서 구글 모듈에 실어서 실행하고 결과를 출력하게 하는 코딩이 필요. 함수 제작

    def trans_action(self):  # 이것이 slot에 해당. signal 이 가면 slot이 실행되는 것. 번역실행 함수를 작명하여 하나 만듦. 작명시 무슨 함수인지 알 수 있게 작명하고 동시에 주석도 달아줌. 이 버튼이 눌리면 그 함수를 불러오게 하는 것이 필요.
        korText = self.kor_input.text()  # kor_input에 입력된 한글 텍스트 가져오기. 입력하는 글을 가져오게 하는 함수는 text() 그것을 어딘가에 저장해야 할 것.
        if korText == "": #입력값이 없으면 이라는 코딩. ""은 공백이라는 것이므로.
            print("공백테스트")

        trans = googletrans.Translator()  # 구글 트랜스 모듈의 객체 선언
        # print(googletrans.LANGUAGES) #정의해 놓은 언어의 약자를 볼 수 있다.


        engText = trans.translate(korText, dest="en")  # 영어 번역결과를 가져오게 하는 함수. 이것도 저장해야. engText를 작명하여 저장
        japText = trans.translate(korText, dest="ja")
        chnText = trans.translate(korText, dest="zh-cn")


        self.eng_input.append(engText.text)  #말미에 .text라고 써 주어야 정상적으로 출력된다. 번역된 영어텍스트를 eng_input에 출력
        self.jap_input.append(japText.text)
        self.chn_input.append(chnText.text)


        def init2_action(self):  #초기와 버튼 함수  clear는 공통
            self.kor_input.clear()
            self.eng_input.clear()
            self.ja_input.clear()
            self.ch_input.clear()

        def init1_action(self):  # 입력초기화 버튼 함수
            self.kor_input.clear()  # 입력 내용 지우기



# 이하와 같이 하면 실행구문이 완성됨.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())





















