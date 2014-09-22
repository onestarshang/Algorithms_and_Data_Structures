#coding:utf-8
"""
/****************************************************************************
 *  Execution:  python WeightedQuickUnionUF.py input.txt
 *
 *  Weighted quick-union (without path compression).
 *
 ****************************************************************************/
"""

import sys, os, time

class WeightedQuickUnionUF:
    
    def __init__(self, N):
        self.count = N        #number of components
        self.id = []          #id[i] = parent of i
        self.sz = []          #sz[i] = number of objects in subtree rooted at i
        for i in range(N):
            self.id.append(i)
            self.sz.append(1)
        
    def UFcount(self):
        """Return the number of disjoint sets."""
        return self.count
    
    def find(self, p):
        """Return component identifier for component containing p"""
        while p != self.id[p]: ###优化：只寻找lgN（约）步（树高）
            p = self.id[p]
        return p
    
    def connected(self, p, q):
        """Are objects p and q in the same set?"""
        return (self.find(p) == self.find(q))
    
    def union(self, p, q):
        """Replace sets containing p and q with their union."""
        i = self.find(p)
        j = self.find(q)
        if i == j: 
            return
        if self.sz[i] < self.sz[j]: #make smaller root point to larger one
            self.id[i] = j          ###优化：较矮的树接到较高的树根下
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        
        self.count -= 1
        pass
 
 
def test():
    """ 7-2 5-1 8-7 0-3 0-1 8-6 6-0 6-4 3-9 """
    """3-9 1-5 1-7 4-6 8-7 7-0 6-3 6-1 7-2 """
    """2-7 9-0 4-6 5-8 3-5 2-5 4-0 5-9 9-1 """
    pass
    
    
if __name__ == '__main__':
    if len(sys.argv) == 2 :
        N = int(sys.argv[1])
        f = open('input1.txt')  # no EXCEPTIONS...
        uf = WeightedQuickUnionUF(N)
        for l in f:
            p = int(l.split(' ')[0])
            q = int(l.split(' ')[1])
            if uf.connected(p, q):
                print "connected : %s  %s"%(p, q)
                continue
            uf.union(p, q)
            print "%s   %s"%(p, q)
        print "# components: %d"%(uf.UFcount())
        print uf.id
        f.close()
    else:
        print "param error: enter a number..."
