# -*- coding: utf-8 -*-
import tkinter as tk
from calc import Calculator #calc.py 파일에서 Calculator 클래스 가져오기

#이 스크립트가 직접 실행될 때만 아래 코드 실행
if __name__ == "__main__":
    root = tk.Tk() #Tkinter의 메인 윈도우 생성
    calc = Calculator(root) #클래스의 객체를 생성, 메인 윈도우 넘기기
    root.mainloop() #윈도우가 화면에 나타나고 사용자의 입력을 기다리는 이벤트 루프 시작
