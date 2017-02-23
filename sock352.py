import binascii
import socket as syssock
import struct
import sys
import random

# Bit Flags
SOCK352_SYN = 0x01
SOCK352_FIN = 0x02
SOCK352_ACK = 0x04
SOCK352_RESET = 0x08
SOCK352_HAS_OPT = 0xA0


# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from
s = None


def init(UDPportTx, UDPportRx):   # initialize your UDP socket here
    if UDPportRx < 0 or UDPportRx > 65535:
        return -1

    if UDPportTx < 0 or UDPportTx > 65535:
        return -1

    if UDPportRx == 0:
        UDPportRx = 27182
    if UDPportTx == 0:
        UDPportTx = 27182

    s = socket()

    s.bind(('', UDPportRx))
    return 1

class socket:

    def __init__(self):  # fill in your code here
        return

    def bind(self, address):
        # NULL FUNCTION FOR PART 1
        return

    def connect(self, address):  # fill in your code here
        # Create a new sequence number
        sequence_no = random.randint(0, 1000)
        # Set Version to 0x1
        version = 0x1
        # protocol, opt_ptr, source_port, dest_port must be set to 0
        flags = SOCK352_SYN
        opt_ptr = 0
        checksum = 0
        protocol = 0
        source_port = 0
        dest_port = 0
        # Next
        ack_no = sequence_no + 1
        window = 0
        payload_len = 0

        # Create a new packet header with the SYN bit set in the flags (Use the struct.pack method)
        sock352PktHdrData = '!BBBBHHLLQQLL'
        header_len = struct.calcsize(sock352PktHdrData)
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len,
            checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        
        while True:
            # add packet to outbound queue
            s.sendto(header, address)

        # set the timeout

        #   wait for the return SYN

        #       if there was a timeout, retransmit the SYN packet

        # set the outbound and inbound sequence number


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

        sequence_no = random.randint(0, 1000)
        # Set Version to 0x1
        version = 0x1
        # protocol, opt_ptr, source_port, dest_port must be set to 0
        flags = SOCK352_SYN
        opt_ptr = 0
        checksum = 0
        protocol = 0
        source_port = 0
        dest_port = 0
        # Next
        ack_no = sequence_no + 1
        window = 0
        payload_len = 0
        sock352PktHdrData = '!BBBBHHLLQQLL'
        header_len = struct.calcsize(sock352PktHdrData)
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len,
            checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        
        # Create a new UDP packet with the header and buffer 
        # Send the UDP packet to the destinatoin and transmit port
        # Set the timeout
        # wait or check for the ack or timeout


        return bytessent

    def recv(self, nbytes):
        return
        bytesreceived = 0     # fill in your code here
        chunks = []
        while bytesreceived < nbytes:
            chunk = self.sock.recv(min(nbytes - bytesreceived), 2048)
            if chunk == '':
                raise RuntimeError("socket contents broken")
            chunks.append(chunk)
            bytesreceived = bytesreceived + len(chunk)
        return bytesreceived
