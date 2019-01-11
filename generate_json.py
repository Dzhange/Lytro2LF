import json
from pprint import pprint

with open('template.json') as f:
    data = json.load(f)

number = 9
max_range = 0.5

step = max_range/((number-1)/2)

data["viewStereoBaseline"] = step


for row in range(1,number+1):
	for col in range(1,number+1):
		
		U_value = max_range - step * (row-1)
		V_value = max_range - step * (col-1)

		data["viewPerspectiveU"] = U_value
		data["viewPerspectiveV"] = V_value

		name = str(row)+'_'+str(col)

		with open('./recipe_'+str(number)+'X'+str(number)+'/'+name+'.json', 'w') as outfile:
		    json.dump(data, outfile)
