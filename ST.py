from gevent.backdoor import BackdoorServer
server = BackdoorServer(('148.70.186.152', 8885),
                        banner="Hello from gevent backdoor!",
                        locals={'foo': "From defined scope!"})
server.serve_forever()