import uuid
import socket
import platform
import psutil
import os


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_uuid():
    return str(uuid.uuid1()).replace('-', '')


def get_hostname():
    return socket.gethostname()


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def get_platform():
    return platform.platform()


def get_arch():
    return platform.architecture()[0]
