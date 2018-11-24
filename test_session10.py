import session10

def test_volume_cylinder():
    assert session10.volume_cylinder(4, 3) == 150.79644737231007
    
def test_volume_sphere():
    assert session10.volume_sphere(1) == 4.1887902047863905