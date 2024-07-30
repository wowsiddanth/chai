from chai import Chai

app = Chai()
count = 0

@app.register_get(path="/app/users/")
def get_users():
    return "All users!"

@app.register_post(path='/')
def increment_count():
    counted = count + 1
    return {'counted': counted}

app.boil(8000, guarantee_port=True)


