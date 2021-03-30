from importlib import reload as Rfrsh
import hmmm

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1 ■■■ f(5) = 5 ■■■ f(9) = 34

#ZAne ThummBorst
#I pledge my honor that I have abided by the Stevens Honor System.

RecFibSeq = """ # You may not need all lines
00 read r1
01 setn r11  1           
02 setn  r15 42                           
03 calln r14 7          
04 nop                  
05 write r10            
06 halt                 
07 jnezn r1  11         
08 setn  r13 0          
09 setn r10 0                  
10 jumpr r14            
11 pushr r1  r15        
12 pushr r14 r15         
13 addn  r1 -1          
14 nop                  
15 calln r14 7          
16 popr  r14 r15                  
17 popr  r1 r15        
18 add   r13 r10 r11
19 copy  r10 r11
20 copy  r11 r13
21 jumpr r14
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = False

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
