import BAC0
# import socket
import time
# import logging

# from tornado.escape import json_decode, json_encode
# from tornado.ioloop import IOLoop
# from tornado import gen
# from tornado.options import define, options, parse_command_line
# from tornado.web import Application, RequestHandler

# from tornado.options import define, options, parse_command_line

# define("port", default=8888, help="run on the given port", type=int)
# define("debug", default=True, help="run in debug mode")

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# ip_address = s.getsockname()[0]
# s.close()

test = BAC0.connect(
    ip="10.10.1.29/24"
)
test.disconnect()

# class BacnetDevice(object):
#     def __init__(self):
#         # self._daemon = BAC0.lite(
#         #     ip=f"{ip_address}/24",
#         #     port="47808",
#         # )
#         # self._daemon.disconnect()
#         print("Hello")

#     def reset(self):
#         # fetch from database
#         print("Trying to reset device")
#         self._daemon.disconnect()
#         # self._daemon = BAC0.lite(
#         #     ip=f"{ip_address}/24",
#         #     port="47808",
#         # )

#     def session(self):
#         return self._daemon

# class MainHandler(RequestHandler):
#     def get(self):
#         self.write("Hello, world")

# class DiscoverHandler(RequestHandler):
#     def initialize(self, bacnet_device):
#         self._bacnet_device = bacnet_device

#     def get(self):
#         self._bacnet_device.reset()
#         self.write("Something")

# def main():
#     parse_command_line(final=False)
#     bacnet_device = BacnetDevice()

#     app = Application(
#         [
#             (r"/", MainHandler),
#             (r"/discover", DiscoverHandler, dict(bacnet_device=bacnet_device)),
#         ],
#         debug=options.debug
#     )
#     app.listen(options.port)

#     print("Listening on http://localhost:%d" % options.port)
#     IOLoop.current().start()

# if __name__ == "__main__":
#     main()
