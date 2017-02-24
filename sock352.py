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
udp_sock = type(syssock.socket)
server_addres = ""

send = ()
receive = ()
def init(UDPportTx, UDPportRx):   # initialize your UDP socket here
    print 'create udp socket here'
    # Create a UDP/Datagram Socket
    global udp_sock
    udp_sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    # Bind the port to the Rx (receive) port number
    print UDPportRx
    global server_address
    print(UDPportRx, UDPportTx)
    server_address = ('', int(UDPportRx))
    udp_sock.bind(server_address)
    global send
    global receive
    send = ('',int(UDPportTx))
    receive = ('',int(UDPportRx))
    pass


class socket:
    def __init__(self):  # fill in your code here
        print 'constructor'
        return

    def bind(self, address):
        # NULL FUNCTION FOR PART 1
        return

    def connect(self, address):  # fill in your code here
        print 'connect'
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
        payload_len = 63000

        # Create a new packet header with the SYN bit set in the flags (Use the struct.pack method)
        sock352PktHdrData = '!BBBBHHLLQQLL'
        header_len = struct.calcsize(sock352PktHdrData)
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len,
            checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        version = 0x1

        while True:
            #   add the packet to the outbound queue
            my_addr = ('localhost', 9999)
            self.address = my_addr
            print "sending data to " + str(receive)
            udp_sock.sendto(header, receive)
            print 'message was sent'
            #   set the timeout
            #sendSock.settimeout(0.2)
            try:
                udp_sock.settimeout(1)
                data, server = udp_sock.recvfrom(1024)
                 #      wait for the return SYN
                a, flags, c, d, e, f, g, h, i, ack, k, l = struct.unpack(sock352PktHdrData, data)
                if flags & 0x1 == 1 and ack == 1:
                    print 'we are connected'
                    return
                # sendSock.settimeout(0.0)      
               
                break
            except syssock.timeout:
                print ("timeout error")
                continue
                #        if there was a timeout, retransmit the SYN packet 
                #   set the outbound and inbound sequence numbers            

        return 1

    def listen(self, backlog):
        print 'listen'
        return

    def accept(self):
        print 'accept'
        (clientsocket, address) = (self, send)  # change this to your code

        return (clientsocket, address)

    def close(self):   # fill in your code here
        udp_sock.close()
        return

    def send(self, buffer):
        print "sending data to " + str(send)
        print buffer.__sizeof__()
        udp_sock.settimeout(.2)
        
        while(True):
            try:
                bytessent = udp_sock.sendto(buffer, send)     # fill in your code here
                return bytessent
            except syssock.timeout:
                continue

    def recv(self, nbytes):
        print "got into recv"
        chunks = []
        bytesreceived = 0
        while bytesreceived < nbytes:
            chunk = udp_sock.recv(min(nbytes - bytesreceived, 4096))
            if chunk == '':
                raise RuntimeError("socket contents broken")
            chunks.append(chunk)
            bytesreceived = bytesreceived + len(chunk)
        #bytesreceived = udp_sock.recv(nbytes)
        """
        bytesreceived = 0     # fill in your code here
        chunks = []
        while bytesreceived < nbytes:
            print 'hey'
            udp_sock.settimeout(1)
            try:
                chunk = udp_sock.recv(min(nbytes - bytesreceived, 4096))
                if chunk == '':
                    raise RuntimeError("socket contents broken")
                chunks.append(chunk)
                bytesreceived = bytesreceived + len(chunk)
            except syssock.timeout:
                print "recv timeout error"
        """
        return chunk