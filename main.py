import network
import socket

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
            <body><h1>Hello World</h1></body></html>
         """
  return html

def init_wifi_network(ssid: str, password: str):
    """Function to set up the device in Access Point (AP) mode.

    Args:
        ssid (str): The name of the network.
        password (str): The password for the network.
    """
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while not ap.active():
        pass
    
    print('Network Is Active')
    print(f'IP Address:{ap.ifconfig()[0]}')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    
    # only allow one connection at a time
    s.listen(1)

    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      print('Content = %s' % str(request))
      response = web_page()
      conn.send(response)
      conn.close()

if __name__ == '__main__':
    init_wifi_network('Carplay Dongle', 'password')