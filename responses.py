def ok_200(content: str, content_type: str='text/html') -> bytes:
    return f"""HTTP/1.1 200 OK
               Content-Type: {content_type}

               {content}
               """.encode()

def not_found_404():
    return f"""HTTP/1.1 404 Not Found
              Content-Length: {len("404 Not Found")}\r\n

              404 Not Found
              """.encode()
