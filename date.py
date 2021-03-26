from datetime import datetime, timedelta
import json

x = {"date": "2020-03-30"}

days_plus = datetime.strptime(x["date"], "%Y-%m-%d") + timedelta(days=22)
print(days_plus)
