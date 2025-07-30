from calculator import Calculator

calculator = Calculator()

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-6, -10)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(5.6, 4.3)  # Python посчитает сумму
res = round(res, 1)  # округлит ее до одного знака после запятой
print(res)  # напечатает сумму
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10

res = calculator.div(10, 2)
assert res == 5

# Было (неправильно - используются множества {}):
numbers = {} # Это пустой словарь, а не список!
res = calculator.avg(numbers)
assert res == 0

numbers = {1,2,3,4,5,6,7,8,9,5} # Это множество
res = calculator.avg(numbers)
assert res == 5

# Стало (правильно - используем списки []):
# Пустой список
numbers = []
res = calculator.avg(numbers)
assert res == 0

# Список чисел (включая дубликаты)
numbers = [1,2,3,4,5,6,7,8,9,5]  # 10 элементов
res = calculator.avg(numbers)
assert res == 5.0  # Сумма=50, среднее=5.0

# Тест деления на ноль с проверкой исключения
try:
    calculator.div(10, 0)
    assert False, "Ожидалось исключение ArithmeticError"
except ArithmeticError as e:
    assert str(e) == "На ноль делить нельзя"

# Тесты для avg()
# Пустой список
numbers = []
res = calculator.avg(numbers)
assert res == 0

# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = calculator.avg(numbers)
assert res == 5.0  # 50/10=5.0

# Другой список
numbers = [10, 20, 30]
res = calculator.avg(numbers)
assert res == 20.0  # 60/3=20.0

print("Все тесты пройдены успешно!")    
