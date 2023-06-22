import datetime

from scapy.all import *


def capturar_pacotes(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 4:
            data = {
                'Endereço MAC do Dispositivo': pkt.addr2,
                'SSID da Rede': pkt.info.decode(),
                'Horário da Captura': str(datetime.datetime.now()),
                'Sinal do Pacote (dBm)': pkt.dBm_AntSignal,
                'Canal da Rede': pkt[Dot11Elt:3].info,
                'Potência de Transmissão (dBm)': pkt.dBm_AntSignal + pkt[RadioTap].dBm_AntSignal,
                'Criptografia': pkt[Dot11Elt:5].info,
                'Tipo de Autenticação': pkt[Dot11Elt:13].info,
                'Taxa de Transmissão (Mbps)': pkt[Dot11Elt:15].info,
                'Informações Adicionais': pkt[Dot11Elt:22].info
            }
            print(data)
            with open('log.txt', 'a') as arquivo:
                arquivo.write(str(data) + '\n')

def main():
    sniff(iface='en0  ', prn=capturar_pacotes)

if __name__ == '__main__':
    main()
