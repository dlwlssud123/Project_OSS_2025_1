
class Expense: #단일 지출 내역을 나타내는 클래스
    def __init__(self, date, category, description, amount): #날짜, 지출카테고리, 설명, 금액
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self): #지출내역을 출력할때의 형식 정의
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"