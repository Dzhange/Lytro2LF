import os, sys

tar_dir = sys.argv[1]
print('tar_dir is ' + tar_dir)
all_names = os.listdir(tar_dir)
all_names.sort(key = lambda x : x[4:8])

count = 0

flag = ' '
view_path = ''

while len(all_names) > 0:
	cur_img = all_names[0]
	cur_flag = cur_img[4:8]
	print("flag is " + flag + "cur_flag is "+ cur_flag )
	if cur_flag != flag :
		flag = cur_flag
		count += 1
		print("change flag to ", flag)
		view_path = tar_dir + 'view' + str(count) + '/'	
		if not os.path.exists(view_path):
			os.makedirs(view_path)

	os.rename(tar_dir+cur_img,view_path+cur_img)
	all_names.pop(0)

