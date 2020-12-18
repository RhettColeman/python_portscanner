import socket #Allows communication with other machines using TCP/UDP
import termcolor #Allows for colored output

def scan(target,ports): #Inputs User data to set up a port range.
    print(f'\n Starting scan for {target}...')
    for port in range(1,ports+1):
        scan_port(target, port)

def scan_port(ipaddress, port): #Scans each port 1 by 1 using the range set above.
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'[+] {port} is Port Open')
        sock.close()
    except:
        print(f'[-] {port} is Port Closed')

if __name__ == '__main__':
    #User Input
    targets = input('[*] Enter Targets (IP address) to scan (split them by , ): ')
    ports = int(input('[*] Enter how many ports you want to scan (1-65535): '))

    #Start Scanner based on 1 or multiple entries
    if ',' in targets:
        print('[*] Scanning Multiple Targets')
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(''),ports)
    else:
        scan(targets,ports)