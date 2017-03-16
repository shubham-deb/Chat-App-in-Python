# chat_client.py

import sys, socket, select
from tkinter import *

'''
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.insert(10,msg)
   e2.delete(0,END)
'''  
def chat_client():
    '''
    
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    '''

    master = Tk()
    Label(master, text="CONVERSATION").grid(row=0)
    Label(master, text="").grid(row=102)
    e1 = Entry(master,bd=5,width=100)
    e2 = Entry(master,bd=5,width=100)

    e1.grid(row=1, column=0,rowspan=100,columnspan=100,ipady=50)
    e2.grid(row=103, column=0,rowspan=100,columnspan=100,ipady=50)

    Button(master, text='Quit', command=master.quit).grid(row=204, column=0, sticky=W, pady=4)
    Button(master, text='Show').grid(row=204, column=1, sticky=W, pady=4)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    host="localhost"
    port=9009
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()
     
    print ('Connected to remote host. You can start sending messages')
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
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
                    e1.insert(10,str(data))
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
                # user entered a message
            msg = sys.stdin.readline()
            e1.insert(10,msg)
            e2.delete(0,END)
            s.send(e2.get())
            sys.stdout.write('[Me] '); sys.stdout.flush()
    mainloop( )

if __name__ == "__main__":
    sys.exit(chat_client())
