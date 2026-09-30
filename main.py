def hello_world(name="world"):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    try:
        name = input("Enter your name: ").strip()
    except EOFError:
        name = ""
        print()
    hello_world(name or "world")
