newdict = {"city": "Moscow", "temperature": "20"}
print(newdict["city"])
newdict["temperature"] = str(int(newdict["temperature"]) - 5)
print(newdict)
print(newdict.get("country","Russia"))
newdict["date"] = "27.05.2019"
print(len(newdict))
print(newdict)

from dataclasses import dataclass
@dataclass
class info:
    city: str
    temperature: int

a = info("Moscow","20")
print(a)