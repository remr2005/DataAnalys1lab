import prime_number_gen

def test_gen():
    assert prime_number_gen.gen(100) == 101
    assert prime_number_gen.gen(4) == 5
    assert prime_number_gen.gen(6) == 7