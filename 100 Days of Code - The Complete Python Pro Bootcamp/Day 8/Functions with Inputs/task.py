def greet():
    print("hello")
    print("welcome")
    print("bye")

greet()

def greet_with_name(name):
    print(f"hello {name}")
    print(f"welcome, {name}")
    print(f"bye, {name}")

greet_with_name("manas")
greet_with_name(123)

def greet_with(name,location):
    print(f"hello {name} from {location}")

greet_with("manas","odisha,india")

greet_with(location="singapore", name="aayush")