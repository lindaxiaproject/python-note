class Player:
    def __init__(self, name: str, number: int, postion: str, age: int = 18) -> None:
        self.name = name
        self.number = number
        self.postion = postion
        self.age = age

    # 重写方法,修改响应结果
    def __repr__(self) -> str:
        return f'Player: {self.name}  {self.number}'
    # 重写方法
    def __eq__(self, __o: object) -> bool:
        return self.age == __o.age
    # 重写方法
    def __gt__(self, __o: object) -> bool:
        return self.age > __o.age


p1 = Player('SXT', 18, 'PG', 26)
# Player: SXT  18
print(p1)
