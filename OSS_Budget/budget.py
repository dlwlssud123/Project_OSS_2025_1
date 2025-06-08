import datetime 
from expense import Expense
import datetime
import csv #csv 모듈 불러오기
#여러 expense 객체를 관리하고 가계부의 주요기능을 수행
class Budget: 
    def __init__(self, filepath = "expenses.csv"): #추가된 exnpense 객체들을 저장하는 리스트, 리스트를 초기화
        self.filepath = filepath #파일 경로를 속성으로 저장
        self.expenses = []
        self.load_expenses() #프로그램 시작시 데이터 불러오기

    def add_expense(self, category, description, amount): #새로운 지출 내역을 추가
        today = datetime.date.today().isoformat() #현재 날짜를 자동으로 지정
        expense = Expense(today, category, description, amount) 
        self.expenses.append(expense) 
        self.save_expenses() #지출추가후 바로 파일에 저장
        print("지출이 추가되고 저장되었습니다.\n")

    def list_expenses(self, start_date = None, end_date = None): 
        #현재까지 추가된 모든 지출내역을 번호를 매겨 출력
        #start date와 end date가 주어지면 해당 기간으로 필터링하여 출력
        items_to_display = self.expenses

        #사용자 지정 날짜가 있는경우에만 필터링 수행
        if start_date and end_date:
            items_to_display = [
                e for e in items_to_display
                if start_date <= datetime.date.fromisoformat(e.date) <= end_date
            ]

        if not items_to_display: #지출 내역이 없을때 출력
            print("지출 내역이 없습니다.\n")
            return

        print("\n[지출 목록]")
        for idx, e in enumerate(items_to_display, 1):
            print(f"{idx}. {e}")
        
            print() #목록 출력 후 한줄 띄우기

    def total_spent(self): #현재까지의 모든 지출금액의 합계를 출력
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
    def load_expenses(self): #csv파일에서 지출내역 불러오기
        try:
            with open(self.filepath, 'r', encoding = 'utf-8', newline = '') as f:
                reader = csv.reader(f)
                header = next(reader) #헤더(첫 줄) 건너뛰기
                for row in reader:
                    #파일에서 읽은 데이터로 exnpense 객체 생성
                    #row -> [date, category, description, amount]
                    expense = Expense(row[0], row[1], row[2], int(row[3]))
                    self.expenses.append(expense)
        except FileNotFoundError:
            #파일이 없으면 처음 실행으로 돌아가기
            return
        except StopIteration:
            #파일이 비어있는 경우
            return
    def save_expenses(self):
        #현재 지출 내역을 csv파일에 저장
        with open(self.filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # 1. 헤더 작성
            writer.writerow(['date', 'category', 'description', 'amount'])
            # 2. 각 지출 내역을 한 줄씩 작성
            for expense in self.expenses:
                writer.writerow([expense.date, expense.category, expense.description, expense.amount])

                  



