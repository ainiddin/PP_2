from datetime import datetime , timedelta
from random import randint
a = datetime.now()
b = datetime.now()-timedelta(hours=randint(1,20))
c = a - b  
print(c.total_seconds(),"seconds")  