"""
Маша продает куклы ручной работы на маркетплейсе. Для оптимизации стоимости звонков клиентам она хочет собрать
информацию по мобильным операторам, которыми пользуются заказчики. Таким образом, зная номер мобильного телефона,
нужно определить код оператора связи. Номера представлены в виде 11-значных чисел, где первая цифра - код страны,
следующие три цифры – код оператора, а остальные 7 – номер абонента.
"""


def get_operator_code(s: str) -> str:
    s = str(s)
    if len(s) == 0:
        return ''
    else:
        return s[1:4]


if __name__ == "__main__":
    input_str = input()
    print(get_operator_code(input_str))
