'''Goal:  Learn to parse column-oriented text for humans

Most important lesson:  Parsing column-oriented text is fast, easy, fun, and reliable   <== THIS IS A LIE!

'''

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:
        #line = line.rstrip()
        #interface, ipaddr, status, protocol = line.split()
        interface = line[:31].rstrip()
        ipaddr = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
        
        if status.lower() == 'up':
            print '%-15s %s' % (ipaddr, interface)
        
