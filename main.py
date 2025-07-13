def common_elements():
	l1 = []
	l2 = []
	_range = range(100)
	for i in _range:
		if i % 3 == 0:
			a = l1.append(i)
	for i in _range:
		if i % 5 == 0:
			a = l2.append(i)
	l1 = set(l1)
	l2 = set(l2)
	_set = l1.intersection(l2)
	return _set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")