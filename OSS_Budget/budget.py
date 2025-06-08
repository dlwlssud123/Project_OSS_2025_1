import datetime 
from expense import Expense
#여러 expense 객체를 관리하고 가계부의 주요기능을 수행
class Budget: 
    def __init__(self): #추가된 exnpense 객체들을 저장하는 리스트, 리스트를 초기화
        self.expenses = []

    def add_expense(self, category, description, amount): #새로운 지출 내역을 추가
        today = datetime.date.today().isoformat() #현재 날짜를 자동으로 지정
        expense = Expense(today, category, description, amount) 
        self.expenses.append(expense) 
        print("지출이 추가되었습니다.\n")

    def list_expenses(self): #현재까지 추가된 모든 지출내역을 번호를 매겨 출력
        if not self.expenses: #지출 내역이 없을때 출력
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self): #현재까지의 모든 지출금액의 합계를 출력
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


