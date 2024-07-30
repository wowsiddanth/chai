import threading
from server import Server

# Global testing instance
test_server = Server()

def test_init():
    assert test_server.mappings == {}

def test_register_get():

    @test_server.register_get("example_1")
    def example_1():
        return True

    assert "example_1" in test_server.mappings and test_server.mappings["example_1"]()

def test_start_valid_get():
    t = threading.Thread(target=test_server.start, args=[8000])
    t.start()

def test_start_invalid_get():
    pass

test_start_valid_get()

