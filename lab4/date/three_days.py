from datetime import datetime , timedelta

print("date of yesterday :",(datetime.now()-timedelta(days=1)).strftime("%Y.%m.%d"))

print("date of today :",(datetime.now()).strftime("%Y.%m.%d"))

print("date of tomorrow :",(datetime.now()+timedelta(days=1)).strftime("%Y.%m.%d"))