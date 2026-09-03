def display(s):
    print("*" * 5)
    print(s)
    print("-" * 5)


display("hello")
display("jeapedu")


def port(p=8080):
    print(f"port = {p}")


port()
port(80)


def host(ip, port=8080):
    print(f"IP is {ip}:{port}")


host("127.0.0.1")
host("127.0.0.1", 80)


def add(x, y):
    return x + y


print(add(1, 2))
