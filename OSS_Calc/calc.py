# -*- coding: utf-8 -*- 
#.py파일에 한글주석등 UTF-8 문자를 사용하기 위해 파일 상단에 추가
import tkinter as tk #파이썬의 표준 GUI라이브러리 tkinter 라이브러리 임포트

class Calculator: #계산기의 모든 기능과 UI를 포함하는 클래스
    def __init__(self, root): #생성자
        self.root = root #메인 윈도우를 객체 변수에 저장하여 클래스내 어디서든 접근 가능하게 함
        self.root.title("계산기") #윈도우 제목을 계산기로 설정
        self.root.geometry("300x450") #윈도우의 초기 크기를 설정
        
        self.expression = "" #입력 계산식을 문자열 형태로 저장할 변수
        #입력창을 Entry 위젯으로 생성
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        #pack()을 사용하여 위젯을 윈도우에 배치, fill="both"는 위젯이 할당된 공간을 가득 채움
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
        #계산기 버튼 레이아웃 정의
        buttons = [
            ['(', ')', 'C', '←'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        #for 반복문을 통해 버튼 생성
        for row in buttons:
            #버튼을 가로로 묶기 위해 프레임 생성
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                #인코딩 문제 원천 차단을 위해 백스페이스 버튼 특별 처리
                if char == '←':
                    cmd = lambda: self.on_click('BACKSPACE')
                else:
                    #다른 모든 버튼은 해당 버튼의 문자열 그대로 전달
                    #ch = char: lambda가 생성될 때 char 값을 ch에 고정시켜 올바른 문자가 전달되게 함
                    cmd = lambda ch=char: self.on_click(ch)
                #버튼 위젯 생성
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=cmd
                )
                btn.pack(side="left", expand=True, fill="both")
        #키보드의 키 입력을 on_key_press메소드와 연결
        self.root.bind('<Key>', self.on_key_press)

    #모든 버튼 클릭 및 키보드 입력의 처리를 담당하는 메소드
    def on_click(self, char):
        #BACKSPACE 명령어를 받으면 expression의 문자열 마지막 한글자 삭제
        if char == 'BACKSPACE':
            self.expression = self.expression[:-1]
            self.update_entry()
            return  # 작업을 완료하고 함수 종료

        if char == 'C': #C명령어를 받으면 문자열 비우기
            self.expression = ""
            self.update_entry()
            return  # 작업을 완료하고 함수 종료

        if char == '=': #문자열 계산
            try:
                self.expression = str(eval(self.expression))
            except Exception: #계산 오류가 발생하면 에러 표시
                self.expression = "에러"
            self.update_entry()
            return  # 작업을 완료하고 함수 종료

        # 위의 특수 명령어들이 아니면 숫자나 연산자이므로 추가
        self.expression += str(char)
        self.update_entry()
    #키보드 입력 이벤트를 처리하는 메소드
    def on_key_press(self, event):
        key = event.keysym

        if key == 'Return':
            self.on_click('=')
            return
        if key == 'Escape':
            self.on_click('C')
            return
        if key == 'BackSpace':
            self.on_click('BACKSPACE')
            return
        #event.char는 실제 문자값을 가짐
        char = event.char
        #계산기에서 사용가능한 유효 문자인지 확인
        if char in '0123456789+-*/().':
            self.on_click(char)

    #expression 변수의 현재 상태를 화면에 업데이트 하는 메소드
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)