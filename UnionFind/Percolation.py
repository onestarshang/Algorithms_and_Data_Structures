#coing:utf-8
"""
author : onestar shang
email : onestar1967@gmail.com
"""

import sys, os, time
import random
from math import *
from WeightedQuickUnionUF import WeightedQuickUnionUF

class Percolation:
    
    def __init__(self, N):
        """create N-by-N grid, with all sites blocked"""
        self.wqUF = WeightedQuickUnionUF(N*N+2)
        self.fullUF = WeightedQuickUnionUF(N*N+1)
        self.N = N
        self.filled = []
        for i in range(N*N+2):
            self.filled.append(0) #if filled == 0; blocked
        self.top = 0
        self.bottom = N*N+1
        pass
    
    def isOpen(self, i, j):
        """is site (row i, column j) open?"""
        return self.__isValid(i, j) and self.filled[self.__idx(i, j)]
    
    def open(self, i, j):
        """open site (row i, column j) if it is not already"""
        if self.__isValid(i, j):
            idx = self.__idx(i, j)
            self.filled[idx] = 1 #open self
            if self.__isValid(i+1, j) and self.isOpen(i+1, j) : #if right opened
                self.wqUF.union(idx, self.__idx(i+1, j))
                self.fullUF.union(idx, self.__idx(i+1, j))
            
            if self.__isValid(i-1, j) and self.isOpen(i-1, j) : #if left opened
                self.wqUF.union(idx, self.__idx(i-1, j))
                self.fullUF.union(idx, self.__idx(i-1, j))
                
            if self.__isValid(i, j+1) and self.isOpen(i, j+1) : #if below opened
                self.wqUF.union(idx, self.__idx(i, j+1))
                self.fullUF.union(idx, self.__idx(i, j+1))
                
            if self.__isValid(i, j-1) and self.isOpen(i, j-1) : #if up opened
                self.wqUF.union(idx, self.__idx(i, j-1))
                self.fullUF.union(idx, self.__idx(i, j-1))
            
            if i == 1:
                self.wqUF.union(self.top, self.__idx(i, j))
                self.fullUF.union(self.top, self.__idx(i, j))
            if i == self.N:
                self.wqUF.union(self.__idx(i, j), self.bottom)
        pass
    
    def percolates(self):
        """does the system percolate?"""
        return self.wqUF.connected(self.top, self.bottom)
    
    def isFull(self, i, j):
        """is site (row i, column j) full?"""
        idx = self.__idx(i, j)
        return self.__isValid(i, j) and self.fullUF.connected(self.top, idx)
    
    def __idx(self, i, j): #private
        return (i-1)*self.N + j
    
    def __isValid(self, i, j):
        if i >= 1 and i <= self.N and j >= 1 and j <= self.N:
            return True
        else:
#            print 'not valided...'
            return False


class PercolationStats :
    
    def __init__(self, N, T):
        """perform T independent computational experiments on an N-by-N grid"""
        self.frc = []
        self.N = N
        self.T = T
        
    
    def mean(self):
        """sample mean of percolation threshold"""
        res = 0.0
        for i in self.frc:
            res += i
        return res/(self.T)
    
    def stddev(self):
        """sample standard deviation of percolation threshold"""
        mean_r = self.mean()
        res2 = 0.0
        for i in self.frc:
            res2 += pow((i-mean_r), 2)
        stddev_r = res2/(self.T-1)
        return sqrt(stddev_r)
    
    def confidenceLo(self):
        """returns lower bound of the 95% confidence interval"""
        return self.mean() - 1.96*self.stddev()/sqrt(self.T)
    
    def confidenceHi(self):
        """returns upper bound of the 95% confidence interval"""
        return self.mean() + 1.96*self.stddev()/sqrt(self.T)
    
    def doTEST(self):
        for i in range(self.T):
            p = Percolation(self.N)
            opened = 0
            while not p.percolates():
                _i_idx = random.randint(1, self.N+1)
                _j_idx = random.randint(1, self.N+1)

                if p.isOpen(_i_idx, _j_idx):
                    continue
                
                opened += 1
                p.open(_i_idx, _j_idx)
                
            self.frc.append((opened*1.0)/(self.N*self.N))


if __name__=='__main__':
#    testp = Percolation(5)
#    
#    testp.open(2,3)

    if len(sys.argv) == 3:
        N = int(sys.argv[1])
        T = int(sys.argv[2])
        
        pstat = PercolationStats(N, T)
        pstat.doTEST()
        
        r1 = "mean                      = %s"%(pstat.mean())
        r2 = "stddev                    = %s"%(pstat.stddev())
        r3 = "confidence interval       = %s , %s"%(pstat.confidenceLo(), pstat.confidenceHi())
        
        res = r1 + "\n" + r2 + "\n" + r3
        f = open('resutl.txt', 'w')
        f.write(res)
        f.close()
    pass
