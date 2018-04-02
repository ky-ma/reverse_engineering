import sys
import re
import os
import string
import pdb


data = [
0x64,						#00
0x64,						#01
0x63,						#02
0x63,						#03
0x62,						#04
0x61,						#05
0x60,						#06
0x58,						#07
0x44,						#08
0x42,						#09
0x42,						#0a
0x42,						#0b
0x42,						#0c
0x42,						#0d
0x42,						#0e
0x41,						#0f
0x40,						#10
0x40,						#11
0x40,						#12
0x60,						#13
0x3f,						#14
]

check = 0xf0
r0 = 0x00	#Data 1 Offset
r1 = 0x00	#Data 0 Offset
r3 = 0x00	#r5
r4 = data	#Data
r5 = 0x00	#Input
r7 = 0x00	#Storage

start = 0x00
end = 0xff

print "  %-23s %7s %4s %6s %11s %6s %6s %6s %6s" % ('Description','data', 'r5', 'r3', 'r4_1', 'r4_0', 'r7', 'r1', 'r0')
for i in xrange(start, end + 1):
	r5 = i
	r0 = check

	if r5 >= r0:
		#print "r5 GREATER or EQUAL to 0xf0, r5 = 0x%0.2x, returning %x" % (r5, (r4[15]))
		print "%-28s 0x%0.2x   0x%0.2x  0x%4.4x     %4s   %4s   %4s   0x%0.2x   0x%0.2x" % ('1st BRANCH r5 >= f0',i,r5, r3, '-NA-', '-NA-', '-NA-', r1, r4[0x0f])
	else:
		r3 = r5
		#print "before shifting r5 = 0x%0.2x" % r5
		#print "before shifting r3 = 0x%0.2x" % r3
		r3 = (r3 & 0x0f)
		r5 = r5 >> 4
		r3 = r3 << 12
		#print "after shifting r5 = 0x%0.2x" % r5
		#print "after shifting r3 = 0x%0.2x" % r3
		r1 = r4[0 + r5]
		r0 = r4[1 + r5]
		r4_1 = 0 + r5	#subscript for r1
		r4_0 = 1 + r5	#subscript for r0
		#print "r1 = 0x%0.2x, r0 = 0x%0.2x" % (r1, r0)
		print "%-28s 0x%0.2x   0x%0.2x  0x%4.4x     %4s   %4s   %4s   0x%0.2x   0x%0.2x" % ('Before BRANCHES', i, r5, r3, r4_1, r4_0, '-NA-', r1, r0)
		if r0 >= r1:
			r0 = r0 - r1
			r0 = r0 * r3
			r0 = r0 >> 16
			r0 = r1 + r0
			#print "r0 >= r1, r0 = 0x%0.2x" % r0
			print "%-28s 0x%0.2x   0x%0.2x  0x%4.4x     %4s   %4s   %4s   0x%0.2x   0x%0.2x" % ('2nd BRANCH r0 >= r1', i, r5, r3, r4_1, r4_0, '-NA-', r1, r0)
			#import pdb
			#pdb.set_trace()
		else:
			r7 = r0
			r1 = r1 - r0
			r1 = r1 * r3
			r0 = r7
			r1 = r1 >> 16
			r0 = r0 - r1
			#print "r0 < r1, r0 = 0x%0.2x" % r0
			print "%-28s 0x%0.2x   0x%0.2x  0x%4.4x     %4s   %4s   0x%0.2x   0x%0.2x   0x%0.2x" % ('END r0 < r1', i, r5, r3, r4_1, r4_0, r7, r1, r0)
