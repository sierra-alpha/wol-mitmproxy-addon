from datetime import datetime, timedelta

import logging

import socket

from mitmproxy import http

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def request(flow: http.HTTPFlow) -> None:
    send_wol("54:A0:50:50:89:DE")
    send_wol("90:E2:BA:16:55:2C")
    send_wol("B6:BB:0E:E2:3C:28")


# 192.168.1.252: "54:A0:50:50:89:DE"
# 192.168.1.252: "90:E2:BA:16:55:2C"
# 192.168.1.252: "B6:BB:0E:E2:3C:28"


def send_wol(mac_address):

    # Move this validation to the loading stage to fail early
    valid_mac_address = (
        mac_address
        if len(mac_address) == 12
        else (
            mac_address.replace(mac_address[4], "")
            if len(mac_address) == 14
            else (
                mac_address.replace(mac_address[2], "")
                if len(mac_address) == 17
                else None
            )
        )
    )

    if not valid_mac_address:
        raise ValueError("Incorrect MAC address format - given: {}".format(mac_address))

    logger.info("Sending WOL, targeting MAC: {}".format(mac_address))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(
        bytes.fromhex("F" * 12 + valid_mac_address * 16), ("255.255.255.255", 9)
    )


if __name__ == "__main__":
    request(None)
