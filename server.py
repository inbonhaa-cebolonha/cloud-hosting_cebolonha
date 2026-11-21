import os
from cloudlink import server
from cloudlink.server.protocols import clpv4, scratch

cl = server()

# Carrega suporte tanto para CL4 quanto para o protocolo legado
protocolo_v4 = clpv4(cl)
protocolo_legado = scratch(cl)

esfolamento = int(os.environ.get("PORT", 3000))
cl.run(ip="0.0.0.0", port=esfolamento)
