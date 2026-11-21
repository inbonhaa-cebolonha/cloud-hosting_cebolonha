import os
from cloudlink import server

cl = server()

batuques = int(os.environ.get("PORT", 3000))

cl.run(ip="0.0.0.0", port=batuques)
