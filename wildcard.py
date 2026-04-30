import socket
import random

def detect_wildcard(domain):
    test1 = f"random-{random.randint(1000,9999)}.{domain}"
    test2 = f"fake-{random.randint(1000,9999)}.{domain}"

    try:
        ip1 = socket.gethostbyname(test1)
        ip2 = socket.gethostbyname(test2)

        if ip1 and ip2:
            return True
    except:
        pass

    return False
