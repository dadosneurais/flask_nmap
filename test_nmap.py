
import nmap

def scan_ip(ip):
    nmp = nmap.PortScanner()
    nmp.scan(ip)

    state = nmp[ip].state()
    ports = nmp[ip]['tcp'].keys()

    if state == 'up':
        result = {
            'ip': ip,
            'ports': ports
        }
    else:
        result = {
            'ip': ip,
            'error': 'IP is down or scanning failed'
        }
    return result

