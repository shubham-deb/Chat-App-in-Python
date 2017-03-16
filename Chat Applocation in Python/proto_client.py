# chat_client.py

import sys, socket, select
 
def chat_client():
    '''
    
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(22)
    host="localhost"
    port=9009
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()
    #print ('Connected to remote host. You can start sending messages')
    print ("Waiting for friends to connect : ")
    sys.stdout.write('[Me] ');
    sys.stdout.flush()
     
    while 1:
        socket_list = [s]
        #print "sockets are : ",socket_list
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print ('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
                # user entered a message
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())
