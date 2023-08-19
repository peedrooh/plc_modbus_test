import time

from pymodbus.client import ModbusTcpClient


def connect(plc_ip_adress):
    client = ModbusTcpClient(plc_ip_adress)
    client.connect()

    return client

def finish(client: ModbusTcpClient):
    client.close()

def run():
    flag = True
    while(True):
        flag = not flag
        client = connect("192.168.15.1")
        client.write_coil(0, flag)
        read = client.read_coils(0, 1)
        finish(client)

        print(f"Valor na saída Q0: {read.bits[0]}")
        time.sleep(2)

if __name__ == "__main__":
    run()