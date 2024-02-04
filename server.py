import socket
import os
import json
from faker import Faker

fake = Faker()
config = json.load(open("config.json"))
SERVER_ADDRESS = config["server_address"]


if __name__ == "__main__":
    try:
        os.unlink(SERVER_ADDRESS)
    except FileNotFoundError:
        pass
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        print("START")
        sock.bind(SERVER_ADDRESS)

        while True:
            print("\nWaiting to receive message...\n")
            data, client_address = sock.recvfrom(4096)
            print("=> {}".format(data.decode("utf-8")))

            if data:
                message = fake.text().encode("utf-8")
                sent = sock.sendto(message, client_address)
                print("\nSent message to client.")
    finally:
        os.unlink(SERVER_ADDRESS)
        print("\nclosing socket")
        sock.close()
