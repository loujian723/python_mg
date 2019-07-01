s = "Sorting1234"
value = "".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)))
print (value)
# sorted()  对所有可迭代的对象进行排序操作
'''
	sorted(iterable[, cmp[, key[, reverse]]])
	参数说明：

	iterable -- 可迭代对象。
	cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
	key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
	reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
'''

# isdigit() 检测字符串是否只有数字组成
# isupper() 检测字符串是否都为大写字母
# islower() 检测字符串是否都为小写字母
