library(bsts)
y<-c(1.0,2.0,3.0,4.0,4.5)
ss<-AddStaticIntercept(list(), y)
bsts(y, ss, niter=100, seed=1)
