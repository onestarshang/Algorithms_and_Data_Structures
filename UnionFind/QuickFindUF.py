#coding:utf-8
"""
/****************************************************************************
 *  Execution:  python QuickFindUF input.txt
 *
 *  Quick-find algorithm.
 *
 ****************************************************************************/
"""
import sys, os, time

class QuickFindUF:
    
    def __init__(self, N):
        """instantiate N isolated components 0 through N-1"""
        self.count = N
        self.id = []
        for i in range(N):
            self.id.append(i)
            
    def UFcount(self):
        """return number of connected components"""
        return self.count
    
    def find(self, p):
        """Return component identifier for component containing p"""
        return self.id[p]
    
    def connected(self, p, q):
        """are elements p and q in the same component?"""
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        """merge components containing p and q"""
        if self.connected(p, q): 
            return
        pid = self.id[p]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = self.id[q]
        self.count -= 1
        pass

def test():
    """5-2 4-2 2-1 7-9 7-8 3-0"""
    """4-6 9-0 5-1 7-6 5-6 0-8"""
    """7-6 5-8 0-6 4-3 9-1 8-2 """
    pass

if __name__=='__main__':
    if len(sys.argv) == 2 :
        N = int(sys.argv[1])
        f = open('input.txt')  # no EXCEPTIONS...
        uf = QuickFindUF(N)
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
