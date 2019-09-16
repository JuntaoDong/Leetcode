from typing import List

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		if numRows==0:
			return []
		S=[[1]]
		for i in range(numRows-1):
			A=S[-1]
			S.append([sum(x) for x in zip(A+[0], [0]+A)])
		return S