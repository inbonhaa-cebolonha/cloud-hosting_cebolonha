import os
from cloudlink import server
from cloudlink.server.protocols import clpv4

cl = server()
protocolo = clpv4(cl)

batuques = int(os.environ.get("PORT", 3000))
cl.run(ip="0.0.0.0", port=batuques)
