from datetime import datetime , timedelta

a=datetime.now() - timedelta(days=5)
print(a.strftime("%Y.%m.%d"))