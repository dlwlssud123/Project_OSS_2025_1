import tkinter as tk
from calc import Calculator 


if __name__ == "__main__":
    root = tk.Tk() #Tkinter의 메인 윈도우 객체(root)를 생성
    calc = Calculator(root) #Calculator 클래스의 객체를 생성하여 계산기 GUI를 초기화
    root.mainloop() #root.mainloop()를 호출하여 Tkinter 이벤트 루프를 시작하고, 사용자가 GUI와 상호작용할 수 있도록