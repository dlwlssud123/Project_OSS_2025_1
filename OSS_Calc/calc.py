import tkinter as tk
#Tkinter 윈도우 객체
#expression: 현재 계산식 또는 결과가 저장되는 문자열 변수
#entry: 계산식이나 결과가 표시되는 Tkinter의 Entry 객체

class Calculator: #계산기의 GUI 요소와 계산 로직 관리
    def __init__(self, root): 
        self.root = root #Tkinter 윈도우(root)를 초기화 하고
        self.root.title("계산기") #계산기라는 제목을 설정
        self.root.geometry("300x400") #윈도우 크리를 300*400 픽셀으로 설정

        self.expression = ""  #계산식을 빈 문자열로 초기화

        # 입력창, 사용자가 입력하고 결과를 볼 수 있는 Entry 위젯을 생성하고 화면에 배치
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right") 
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성, 버튼들을 정의
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons: #루프를 통해 버튼을 생성하여 화면에 배치, 각 버튼은 클릭시 on_click 메소드를 호출
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char): #버튼이 클릭될때 호출되는 핵심 메소드, 버튼의 문자(char)를 인자로 받음
        if char == 'C': #exppression을 초기화
            self.expression = ""
        elif char == '=': #char가 '='인 경우 eval 함수를 사용하여 expression에 저장된 문자열 계산식을 평가하고 그 결과를 expression에 다시 저장,
            try:
                self.expression = str(eval(self.expression))
            except Exception: #계산 중 오류가 발생하면 expression을 에러로 설정
                self.expression = "에러"
        else:
            self.expression += str(char) #그외의 경우: 클릭된 문자를 expression에 추가

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



