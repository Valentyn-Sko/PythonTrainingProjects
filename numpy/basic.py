import numpy
import cv2

n = numpy.arange(27)
print(n)

n = n.reshape(3,9)
print(n)

n = n.reshape(3,3,3)
print(n)



some = [[123,12,132,12,22],[],[]]

m = numpy.asarray(some)
print(m)

im_g = cv2.imread('original.png', 0)
print(im_g)

cv2.imwrite('new.png', im_g[0:2,0:3])

for i in im_g.flat:
    print(i)


ims = numpy.hstack((im_g, im_g)) # tuple inside ()
print(ims)


ivs = numpy.vstack((im_g,im_g))
print(ivs)

lst = numpy.hsplit(ims, 5) #same vsplit
print(lst)