from engine import Value


def main_loop():
    a = Value(2)
    b = Value(3)
    c = a + b
    c.backward()
    

if __name__ == '__main__':
    main_loop()