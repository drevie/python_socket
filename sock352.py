import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from


def init(UDPportTx, UDPportRx):   # initialize your UDP socket here
    # Create a UDP/Datagram Socket
    udp_sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    # Bind the port to the Rx (receive) port number
    print UDPportRx
    server_address = (UDPportRx, 8080)
    udp_sock.bind(server_address)
    pass


class socket:

    def __init__(self):  # fill in your code here
        return

    def bind(self, address):
        # NULL FUNCTION FOR PART 1
        return

    def connect(self, address):  # fill in your code here
        self.sock.connect(address)
        return

    def listen(self, backlog):
        return

    def accept(self):
        (clientsocket, address) = (1, 1)  # change this to your code

        return (clientsocket, address)

    def close(self):   # fill in your code here
        return

    def send(self, buffer):
        bytessent = 0     # fill in your code here
        return bytessent

    def recv(self, nbytes):
        bytesreceived = 0     # fill in your code here
        chunks = []
        while bytesreceived < nbytes:
            chunk = self.sock.recv(min(nbytes - bytesreceived), 2048)
            if chunk == '':
                raise RuntimeError("socket contents broken")
            chunks.append(chunk)
            bytesreceived = bytesreceived + len(chunk)
        return bytesreceived
