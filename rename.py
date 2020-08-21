#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import math

number = 7
# 列出目录
path = sys.argv[1]
item_names = os.listdir(path)
item_names.sort()
print(item_names)

for item in item_names:
	if item[0] == '.':
		continue
	if item == "rename.py":
		continue
	all_views = os.listdir(path+item)
	all_views.sort()
	print(all_views)

	for view in all_views:
		if view[0] == '.':
			continue
		all_images = os.listdir(path+ item+'/'+view)
		all_images.sort()
		count = 0
		path_a = path+item+'/'+view+'/'	

		print("current path is "+ path_a)
		while(len(all_images) > 0):
			image = all_images[0] 
			print("image is " + image+"count is "+str(count))
			if image[0] == '.':
				continue			
			else:
				count += 1
				col = count % number
				if col == 0:
					col = str(number)
				else:
					col = str(col)

				row = int((count - int(col))/number+1)
				row = str(row)
				if row == str(number+1):
					row = str(number)
				os.rename(path_a+image,path_a+col+"_"+row+".png")
				print("new name is "+path_a+col+"_"+row+".png")
			all_images.pop(0)
