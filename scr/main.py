#!usr/bin/env python3
import subprocess
from config import airpods_address


devices_address = airpods_address


def getting_connection_status(address: str) -> None:
    status = subprocess.check_output(f"bluetoothctl info {address}",
                                     shell=True).decode("utf-8")
    return "Connected: yes" in status


def connecting_device(address: str, status: bool = False) -> None:
    if not status:
        subprocess.run(["bluetoothctl", "connect", address])
    else:
        subprocess.run(["bluetoothctl", "disconnect", address])


def handling_connection(addres: str) -> None:
    status = getting_connection_status(addres)
    connecting_device(addres, status)


if __name__ == '__main__':
    handling_connection(devices_address)
