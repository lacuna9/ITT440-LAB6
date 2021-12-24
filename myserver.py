
import socket
import sys
import time
import errno
import math # FOR CALCULATION FUNCTION LIKE  LOG, SQUARE ROOT
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("[REMINDER!!!] Python Calculator sign (LOG <log>, SQUARE ROOT <sqrt>, EXPONENTIAL <exp>)\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n Instruct>
    while True:
        data = s_sock.recv(2048) #INPUT THE VALUE
        data = data.decode("utf-8")

        #CALCULATION PROCESS

        try:
            operation, value = data.split()
            op = str(operation)
            num = int(value)

            if op[0] == 'l':
                op = 'Log'
                answer = math.log10(num)
            elif op[0] == 's':
                op = 'Square root'
                answer = math.sqrt(num)
            elif op[0] == 'e':
                op = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('ERROR!')

            sendAnswer = (str(op) + '(' + str(num) + ') = ' + str(answer))
            print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n The Calculation is Done!! Result sent! \n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        except:
            print ('ERROR!!! Invalid input!!')

 #s_sock.send(str.encode(sendAnswer))

        if not data:
            break

        s_sock.send(str.encode(sendAnswer))
        #s_sock.sendall(str.encode(ok_message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8828)) #THE PORT IS CONNECTED
    print("waiting for client connection ...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('SORRY!! SOCKET ERROR!!')

            except Exception as e:
                print("OOPS!! SIGNAL INTERRUPTED!!")
                print(e)
                sys.exit(1)
    finally:
           s.close()

#byabbyazman
