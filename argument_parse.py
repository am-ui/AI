# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:23:54 2021

@author: ThisPC
"""

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help=" first number")
    parser.add_argument("number2", help= "second number")
    parser.add_argument("operation", help = "operation")
    
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1= int(args.number1)
    n2=int(args.number2)
    result = None
    
    if args.operation =="add":
        result = n1+n2
        
    elif args.operation == "subtract":
        result = n1 - n2
        
    else:
        result = n1*n2
        
    print(result)
        
        
    