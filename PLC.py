import snap7
import ctypes

plc = snap7.client.Client()
plc.connect("192.168.0.5", 0, 1)
#plc.get_connected()


def read_data(size_of_data):
    DB_bytearray = plc.db_read(1, 0, size_of_data)

    total_prod = snap7.util.get_int(DB_bytearray, 0)
    prod_rate = snap7.util.get_real(DB_bytearray, 2)
    message = snap7.util.get_string(DB_bytearray, 6)

    print(f"total: {total_prod}, prod rate: {prod_rate}, message: {message}")