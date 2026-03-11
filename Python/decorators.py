def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Finished running the function.")
    return wrapper

@announce
def greet():
    print("Hello, world!")
greet()