#  Представьте Вы работаете в Мобильной Компании и вас попросили создать
#  генератор номеров. Создайте функцию gen_number() которая генерирует телефонный номер с
#  кодом 0444 _ _ _ _ _ _. Номера которые вы можете
#  генерировать могут содержать в себе только числа 145790.
#  Пример: 0444150971 0444111777 0444457901
import random
def gen_number():
    num = ''
    for x in range(6): #Количество символов (6)
        num = num + random.choice(list('145790')) #Символы, из которых будет составлен ваш номер
    print('Hello, your number is', "0444" + num)

gen_number()