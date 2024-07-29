import socket

class Server:

    def __init__(self):
        self.mappings = {}

    # ------------------ Declare GETs ----------------------------

    def define_get(self, func):
        """Defines a GET endpoint."""
        self.mappings[func.__name__] = func
        print(self.mappings)

        def wrapper(*args, **kwargs):

            """
            if func is mappings["GET"]:
                return mappings["GET"](*args, **kwargs)
            else:
                mappings["GET"] = func
                return 1
            """

            print(self.mappings)

        return wrapper



server = Server()

def ok_200(content: str) -> bytes:
    return f"""HTTP/1.1 200 OK
               Content-Type: text/html

               {content}
               """.encode()

@server.define_get
def test_method():
    print('hello world')

def listen():
    return 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8000))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)
                print(data)
                conn.sendall(ok_200('<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'))
                break

listen()


