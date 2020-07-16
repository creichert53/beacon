import BAC0
import socket
import time
import netifaces
import netaddr
import os, logging, json

from sanic import Sanic
from sanic.response import json as json_response

with open('bacnet/vendors.json') as json_file:
    vendors = json.load(json_file)

adapters = os.listdir("/sys/class/net/")
addrs = netifaces.ifaddresses(adapters[2])
ipinfo = addrs[netifaces.AF_INET][0]
address = ipinfo["addr"]
netmask = ipinfo["netmask"]

# Create ip object and get
cidr = netaddr.IPNetwork("%s/%s" % (address, netmask))


# Async API server
app = Sanic("Beacon")


# Object for handling common BACnet tasks
class BacnetDevice(object):
    def __init__(self):
        self._define_local_device()

    def _define_local_device(self):
        self._daemon = BAC0.connect(ip=str(cidr), port="47808", deviceId="35")

    def reset(self):
        # fetch from database
        self._daemon.disconnect()
        self._define_local_device()

    def discover_devices(
        self, networks='known', limits=(0, 4194303), global_broadcast=False
    ):
        self._daemon.discover(networks, limits, global_broadcast)
        discovered_devices = dict(self._daemon.discoveredDevices if self._daemon.discoveredDevices is not None else {})
        props = [BAC0.device(key[0], key[1], self._daemon, poll=0).properties.asdict for key, v in discovered_devices.items()]
        for prop in props:
            del prop["pss"]
            del prop["network"]
            prop["vendor_name"] = next((vendor["Organization"] for vendor in vendors if vendor["Vendor ID"] == prop["vendor_id"]), None)
        print(props)
        return props

    def session(self):
        return self._daemon

# Set a BACnet device on the server that can be interrogated by the API calls.
app.config.DEVICE = BacnetDevice()

@app.route("/")
async def test(request):
    return json_response({"hello": "world"})

@app.route("/api/discover")
async def discover(request):
    props = app.config.DEVICE.discover()
    return json_response(props)


if __name__ == "__main__":
    port = 8888
    print(f"Listening on http://{address}:{port}")
    app.run(host="0.0.0.0", port=port)
