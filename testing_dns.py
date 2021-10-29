import socket
import argparse 

def get_ip(dn):
    """
    Returns first ip address that corresponds 
    to domain name.
    """
    try:
        data = socket.gethostbyname(dn)
        ip = repr(data)
        return ip
    except Exception:
        return False


def get_ipx(dn):
    """
    Returns all ip addresses that corresponds 
    to domain name.
    """

    try:
        data = socket.gethostbyname(dn)
        ip = repr(data[2])
        return ipx
    except Exception:
        return False


def get_ptr(ip):
    """
    This method returns the 'True Host' name for a
    given IP address
    """
    try:
        data = socket.gethostbyaddr(ip)
        host = repr(data[0])
        return host
    except Exception:
        return False

def get_cname(dn):
    """
    This returns cnames for dn
    """
    try:
        data = socket.gethostbyname_ex(dn)
        alias = repr(data[1])
        #print repr(data)
        return alias
    except Exception:
        return False


def main(): 
    print(get_ptr('8.8.8.8'))
    print(get_cname('www.google.com'))
    print(get_ipx('www.google.com'))
    print(get_ip('www.yahoo.com'))

if __name__ == '__main__':
    main()
