from scapy.all import rdpcap, wrpcap, Raw, IP

# Ruta del archivo pcap original
input_pcap = 'C3.pcap'
# Ruta del archivo pcap modificado
output_pcap = 'C3_modificado.pcap'
# IP del cliente C3
client_c3_ip = '172.17.0.4'  # Reemplaza con la IP real del cliente C3

# Cargar la captura de Wireshark
packets = rdpcap(input_pcap)

# Iterar sobre los paquetes y modificar el cliente SSH especificado
for packet in packets:
    if packet.haslayer(Raw) and b'SSH-2.0-OpenSSH' in packet[Raw].load:
        if b'SSH-2.0-OpenSSH_8.3p1 Ubuntu-1ubuntu0.1' in packet[Raw].load:
            if packet[IP].src == client_c3_ip:
                packet[Raw].load = packet[Raw].load.replace(b'SSH-2.0-OpenSSH_8.3p1 Ubuntu-1ubuntu0.1', b'SSH-2.0-OpenSSH_?')

# Guardar los paquetes modificados en un nuevo archivo pcap
wrpcap(output_pcap, packets)
