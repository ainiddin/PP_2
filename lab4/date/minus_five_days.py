from datetime import datetime , timedelta

a=datetime.now() - timedelta(5)
print(a.strftime("%Y.%m.%d"))