# So we can run this scipt under python 2 or 3
from __future__ import print_function
 
import sys                      # for sys.stderr.write()
import time                     # for strftime
from datetime import datetime   # for datetime.utcnow()
import random                   # to provide random data for this example
 
sys.stderr.write("TA-SimpleApp python script is starting up\n")                  
 
# output a single event
print (str(time.time()) + ", username=\"agent smith\", status=\"mediocre\", admin=noah, money=" + str(random.randint(1, 1000)))
 
# output three events, each one separated by a newline (each line will be a unique event)
for x in range(0, 3):
    strEvent = str(time.time()) + ", "
    strEvent += "username=\"" + random.choice(["Stryker", "Valkerie", "Disco Stu"]) + "\", "
    strEvent += "status=\"" + random.choice(["groovy", "hungry", "rage quit"]) + "\", "
    strEvent += "admin=" + random.choice(["lenny", "carl", "moe"]) + ", "
    strEvent += "money=" + str(random.randint(1, 1000))
    print (strEvent)
