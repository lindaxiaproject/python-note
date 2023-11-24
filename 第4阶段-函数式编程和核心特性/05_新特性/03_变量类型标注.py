from typing import List, Set, Dict, Tuple

# 对于简单的 Python 内置类型，只需使用类型的名称
a: int = 1
b: float = 1.0
c: bool = True
d: str = "test"
e: bytes = b"test"
# 对于 collections ，类型名称用大写字母表示，并且
# collections 内类型的名称在方括号中
f: List[int] = [1]
g: Set[int] = {6, 7}
# 对于映射，需要键和值的类型
h: Dict[str, float] = {'field': 2.0}
# 对于固定大小的元组，指定所有元素的类型
i: Tuple[int, str, float] = (3, "yes", 7.5)
# 对于可变大小的元组，使用一种类型和省略号