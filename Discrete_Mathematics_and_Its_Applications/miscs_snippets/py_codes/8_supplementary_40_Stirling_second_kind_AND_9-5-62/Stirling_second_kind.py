# https://rosettacode.org/wiki/Stirling_numbers_of_the_second_kind#Python
import math
computed = {}

def Stirling_2(n, k):
	key = str(n) + "," + str(k)

	if key in computed.keys():
		return computed[key]
	if n == k == 0:
		return 1
	if (n > 0 and k == 0):
		return 0
	if n == k:
		return 1
	if k > n:
		return 0
	result = k * Stirling_2(n - 1, k) + Stirling_2(n - 1, k - 1)
	computed[key] = result
	return result

Sum=0
n=4
"""
firstly `Stirling_2(n, k)` splits based on "DISTINGUISHABLE OBJECTS AND INDISTINGUISHABLE BOXES"
then `math.perm(3,k)` to let it be "DISTINGUISHABLE BOXES".

hinted by [assign_different_jobs_to_different_employees] from https://gateoverflow.in/222551/kenneth-rosen-edition-6th-exercise-6-question-11-page-no-457?show=222593#a222593
"""
for k in range(1,3+1):
  Sum+=math.perm(3,k)*Stirling_2(n, k)
print(Sum)

#########################################################################
# 9.5-62
#########################################################################
# https://stackoverflow.com/a/11328422/21294350
Stirling_2_range=lambda n,start_end:sum([Stirling_2(n, k) for k in range(start_end[0],start_end[1]+1)])
print(Stirling_2_range(4,(1,4)))