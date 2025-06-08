from budget import Budget 

#사용자 인터페이스를 제공하고 budget 클래스의 메소드를 호출하여 가계뿌 기능을 실해
def main(): 
    budget = Budget() #budget 객체 생성

    while True: #무한 루프를 통해 사용자에게 메뉴를 보여주고 입력을 받음
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ") 

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try: #try 구문을 통해 잘못된 금액 입력시 예외 처리
                amount = int(input("금액(원): "))
            except ValueError: 
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
