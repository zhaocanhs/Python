# -*- coding:utf-8 -*-
# 作者：火小森

product_list = [('Iphone', 5800),
                ('Iphone', 9800),
                ('Mac_Pro', 800),
                ('Bike', 50800),
                ('Watch', 58200)
                ]
salary = input("Input your salary:")
i = 0
if salary.isdigit():  # 判断是否是数字，true,则不是数字，否在是数字
	salary = int(salary)
	shopp_list = []
	while True:
		# 方一
		# for item in product_list:
		# print(product_list.index(item), item)
		# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。直接把列表下标取出来
		# 方二
		for index, item in enumerate(product_list):
			print(index + 1, item)
		user_choice = input("选择要买什么？>>>:")
		if user_choice.isdigit():
			user_choice = int(user_choice)
			# len()返回一个数字，计算长度
			if user_choice < len(product_list) and user_choice >= 0:
				p_item = product_list[user_choice]
				if p_item <= salary:  # 买得起
					shopp_list.append(p_item)
					print("Added %s into shopping cart,your current balance is ")
		elif user_choice == 'q':
			print('exit....')
		else:
			print("invalid option")
