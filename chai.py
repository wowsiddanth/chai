import socket
import responses

from collections import defaultdict
from time import sleep, time 

class Chai:
    def __init__(self):
        self.mappings = {}
        self.mappings['GET'] = {}
        self.mappings['POST'] = {}

    # ------------------ Declare methods ----------------------------

    def register_get(self, path):
        def define_get(func):
            """Defines a GET endpoint."""
            # Register method in mappings
            self.mappings['GET'][path] = func

            def wrapper_get(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper_get

        return define_get


    def register_post(self, path):
        def define_post(func):
            """Defines a POST endpoint."""
            # Register method in mappings
            self.mappings['POST'][path] = func

            def wrapper_post(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper_post

        return define_post

    # ---------------------------------------------------------------

    def create_socket(self, port: int, guarantee_port=False):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Assign port
        while True:
            try:
                s.bind(('localhost', 8000))
                break
            except OSError:
                print('Port taken. Trying random port.')

                # Choose a random port
                if not guarantee_port:
                    port = 0

                sleep(1)

        self.s = s
        print(f'Server started on port {s.getsockname()[1]}')


    def boil(self, port, guarantee_port=False):
        """Starts the server."""
        self.create_socket(port, guarantee_port=guarantee_port)
        self.s.listen()

        while True:
            conn, _ = self.s.accept()

            with conn:
                data = conn.recv(1024)
                parameters = data.split(b' ')

                verb = parameters[0].decode()
                path = parameters[1].decode()

                print(f'{verb} request executed.')

                if path in self.mappings[verb]:
                    ans = self.mappings[verb][path]()
                    conn.sendall(responses.ok_200(ans))
                else:
                    conn.sendall(responses.not_found_404())
