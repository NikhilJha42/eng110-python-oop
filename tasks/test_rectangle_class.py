from rectangle_class import Rectangle, Square

rectangle_a = Rectangle(4, 5)
rectangle_b = Rectangle(5, 4)


def test_0_rectangle():
    assert rectangle_a.get_area() == 20


def test_1_rectangle():
    assert rectangle_a.get_perimeter() == 18


def test_2_rectangle():
    assert rectangle_b.get_area() == 20


def test_3_rectangle():
    assert rectangle_b.get_perimeter() == 18


def test_4_square():
    assert Square(3).get_area() == 9
