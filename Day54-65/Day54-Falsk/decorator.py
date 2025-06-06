def make_underline(func):
    def wrapper():
        return "<u>"+func()+"</u>"
    return wrapper