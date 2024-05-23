#!/usr/bin/python3
class MyList(list):
	def print_sorted(self):
		sort_list = super().copy()
		sort_list.sort()
		print(sort_list)
