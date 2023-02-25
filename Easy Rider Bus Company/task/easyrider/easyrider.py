import json
from collections import Counter

bus_info = dict()
for data in json.loads(input()):
   bus_info.setdefault(data["stop_type"], []).append(data["stop_name"])
counter = Counter(sum([i for i in bus_info.values()], []))
wrong_stops = [x for x in counter if x in bus_info['O'] and counter[x] > 1]
wrong_stops += [y for x, y in bus_info.items() if y in bus_info['O'] and bus_info['F|S']]
print('On demand stops test:', f'Wrong stop type: {sorted(wrong_stops)}' if len(wrong_stops) else 'OK')