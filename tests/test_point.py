from mtpiclick.point import point

def test_point_constructor():
    home = point(123, 456)
    assert home.x == 123    
    assert home.y == 456
