from app import greet

def test_greet():
    assert greet("Trevor") == "Hello, Trevor!"
    assert greet("Carson") == "Hello, Carson!"