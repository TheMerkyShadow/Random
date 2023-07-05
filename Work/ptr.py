import math
import sys
import os

def format_trunc(number):
    truncated_number = int(number * 100) / 100 
    formatted_number = "{:.2f}".format(truncated_number)     
    return formatted_number

N = int( input( "Opps for AA: ") or "0" )
SMB = int( input("SMB to Deduct: ") or "0" ) 
N = ( N - SMB )

PTR = float( input("PTR(%): ") ) / 100
PTR_Numb = ( N * PTR )

for X in range(1,50):
    PTR = (PTR_Numb+X) / (N+X)
    print( X, str( format_trunc(PTR) ) )
    if( PTR >= 0.70 ):
        sys.exit()
