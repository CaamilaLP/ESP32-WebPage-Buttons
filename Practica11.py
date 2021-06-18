from machine import Pin
import machine as mc
import network
import socket
import gc

gc.collect()

# Configuración de las salidas
a = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
f = Pin(2, Pin.OUT)
g = Pin(15, Pin.OUT)
e = Pin(18, Pin.OUT)
d = Pin(19, Pin.OUT)
c = Pin(21, Pin.OUT)

# Configurar wifi
ssid = 'Sol'
password = 'S8y387qhewu'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while wlan.isconnected() == False:
    pass
print('Conexión Wifi %s establecida' % ssid)
print(wlan.ifconfig())   # Muestra datos de la red


# Función para mostrar página web
def webPage():
    html = """
    <html>
<head>
    <title> Bomba </title>
</head>
<body>
    <center>
        <h1> Servidor web ESP32</h1>

        <p><a href='/0'><button style='height:50px ;width: 100px; '>Num 0 </button></a></p>
        <p><a href='/1'><button style='height:50px ;width: 100px; '>Num 1 </button></a></p>
        <p><a href='/2'><button style='height:50px ;width: 100px; '>Num 2 </button></a></p>
        <p><a href='/3'><button style='height:50px ;width: 100px; '>Num 3 </button></a></p>
        <p><a href='/4'><button style='height:50px ;width: 100px; '>Num 4 </button></a></p>
        <p><a href='/5'><button style='height:50px ;width: 100px; '>Num 5 </button></a></p>
        <p><a href='/6'><button style='height:50px ;width: 100px; '>Num 6 </button></a></p>
        <p><a href='/7'><button style='height:50px ;width: 100px; '>Num 7 </button></a></p>
        <p><a href='/8'><button style='height:50px ;width: 100px; '>Num 8 </button></a></p>
        <p><a href='/9'><button style='height:50px ;width: 100px; '>Num 9 </button></a></p>


    </center>
</body>
</html>

    """
    return html


# Creamos un socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP
tcp_socket.bind(('',80))   # conexión abierta desde cualquier ip
tcp_socket.listen(3)   # Límite de peticiones en cola

while True:
    try:
        if gc.mem_free() < 10200:  # Garbage collector
            gc.collect()
        conn,addr = tcp_socket.accept()
        conn.settimeout(3.0)
        print("Nueva conexión desde: %s" %str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        print("Solicitud= %s" %str(request))
        request = str(request)

        # Num 0
        if request.find('/0')==6:
            a.on()
            b.on()
            c.on()
            d.on()
            e.on()
            f.on()
            g.off()

        # Num 1
        if request.find('/1')==6:
            a.off()
            b.on()
            c.on()
            d.off()
            e.off()
            f.off()
            g.off()

        # Num 2
        if request.find('/2')==6:
            a.on()
            b.on()
            c.off()
            d.on()
            e.on()
            f.off()
            g.on()

        # Num 3
        if request.find('/3')==6:
            a.on()
            b.on()
            c.on()
            d.on()
            e.off()
            f.off()
            g.on()

        # Num 4
        if request.find('/4')==6:
            a.off()
            b.on()
            c.on()
            d.off()
            e.off()
            f.on()
            g.on()

        # Num 5
        if request.find('/5')==6:
            a.on()
            b.off()
            c.on()
            d.on()
            e.off()
            f.on()
            g.on()

        # Num 6
        if request.find('/6')==6:
            a.on()
            b.off()
            c.on()
            d.on()
            e.on()
            f.on()
            g.on()

        # Num 7
        if request.find('/7')==6:
            a.on()
            b.on()
            c.on()
            d.off()
            e.off()
            f.off()
            g.off()

        # Num 8
        if request.find('/8')==6:
            a.on()
            b.on()
            c.on()
            d.on()
            e.on()
            f.on()
            g.on()

        # Num 9
        if request.find('/9')==6:
            a.on()
            b.on()
            c.on()
            d.on()
            e.off()
            f.on()
            g.on()

        # Mostrar página web
        response = webPage()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type:text/html\n")
        conn.send("Connection:close\n\n")
        conn.sendall(response)
        conn.close()

    except OSError as erro:
        conn.close()
        print('Conexión cerrada')














