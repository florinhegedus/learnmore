from engine import Value
from utils import draw_dot


def main_loop():
    a = Value(-2)
    b = Value(3)
    c = Value(4)
    d = Value(5)
    res = a.relu() ** 3 + b * c + d
    res.backward()
    print(res)
    dot = draw_dot(res)
    dot.render('graphs/gout')
    

if __name__ == '__main__':
    main_loop()
