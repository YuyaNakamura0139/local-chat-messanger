import socket
import json
import os


config = json.load(open("config.json"))
SERVER_ADDRESS = config["server_address"]
CLIENT_ADDRESS = config["client_address"]


if __name__ == "__main__":
    try:
        os.unlink(CLIENT_ADDRESS)
    except FileNotFoundError:
        pass

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        sock.bind(CLIENT_ADDRESS)
        while True:
            print("\nPlease enter a character.")
            stdin = input().encode("utf-8")
            sock.sendto(stdin, SERVER_ADDRESS)

            print("\nWaiting ...")
            data, server = sock.recvfrom(4096)
            print("\n=> {}".format(data.decode("utf-8")))

    finally:
        os.unlink(CLIENT_ADDRESS)
        print("\nclosing socket")
        sock.close()
