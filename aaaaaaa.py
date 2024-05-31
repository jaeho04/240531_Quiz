class Beverage:
    def __init__(self):
        self.menu = {
            "커피": 3000,
            "녹차": 2500,
            "아이스티": 3000}
    def 계산(self, 이름, 수량):
        if 이름 in self.menu:
            총_가격 = self.menu[이름] * 수량
            return 총_가격
        else:
            return None

음료 = Beverage()

음료_이름 = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
음료_수량 = int(input("수량을 입력하세요: "))

총_가격 = 음료.계산(음료_이름, 음료_수량)

if 총_가격 is not None:
    print(f"{음료_이름} {음료_수량}잔의 총 가격은 {총_가격}원 입니다.")
else:
    print("주문하신 음료는 메뉴에 없습니다.")