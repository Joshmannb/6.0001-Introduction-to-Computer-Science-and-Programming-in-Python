import time
from datetime import datetime
a = datetime.now()
time.sleep(1)
b = datetime.now()
print(b - a)