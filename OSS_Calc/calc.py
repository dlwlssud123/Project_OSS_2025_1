# -*- coding: utf-8 -*-
import tkinter as tk #Tkinter library를 tk라는 이름으로 불러옴


class Calculator:
    #생성자: 객체가 처음 생성될 때 호출 
    def __init__(self, root): 
        self.root = root #메인 윈도우(root)를 객체 변수로 저장
        self.root.title("계산기") #윈도우의 제목을 계산기로 설정
        self.root.geometry("300x400") #크기를 300*400 픽셀로 설정
      
        self.expression = "" #계산식을 저장할 문자열 변수를 초기화

        # 숫자가 표시될 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right") 
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]
        #반복문으로 버튼들을 생성, 배치
        for row in buttons:
            frame = tk.Frame(root) #버튼들을 한줄에 묶기 위한 프레임
            frame.pack(expand=True, fill="both")
            for char in row:
                #각 문자에 해당하는 버튼 생성
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    #버튼을 클릭하면 on_click 메소드가 호출
                    #lambda를 사용하여 클릭된 버튼의 문자(ch)를 인자로 전달
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both") #프레임내에 버튼 배치
    #버튼 클릭시 실행될 메소드
    def on_click(self, char):
        if char == 'C': #C버튼을 누르면 계산식 초기화
            self.expression = ""
        elif char == '=': #=버튼을 누르면 eval 함수를 사용해 문자열 형태의 계산식을 실행하고 결과
            try:
                self.expression = str(eval(self.expression))
            except Exception: #계산중 오류가 발생하면 에러 메시지 표시
                self.expression = "에러"
        else: #숫자나 연산자 버튼을 누르면 계산식 문자열에 해당문자 추가
            self.expression += str(char) 
        #입력창의 내용을 모두 지우기
        self.entry.delete(0, tk.END)
        #새로 업데이트된 계산식을 입력창에 삽입
        self.entry.insert(tk.END, self.expression)