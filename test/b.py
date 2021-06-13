def type_1(arr, data):
	arr[data[0]-1] = data[1]
	return arr

def type_2(arr, data):
	cnt = 0
	extracted_arr = arr[(data[0]-1):(data[1])]
	for num in extracted_arr:
		if data[2] <= num <= data[3]:
			cnt += 1
	print(cnt)

n = int(input())
arr = list(map(int, input().split()))
q_num = int(input())
q_type_datas = [list(map(int, input().split())) for _ in range(q_num)]

for type_data in q_type_datas:
	type = type_data[0]
	if type == 1:
		type_1(arr, type_data[1:])
	else:
		type_2(arr, type_data[1:])