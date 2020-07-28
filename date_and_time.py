# prints out date and time two different ways

import datetime
from datetime import datetime

entire = datetime.now().replace(microsecond=0)
print(entire)
print(entire.strftime("%x %X"))
