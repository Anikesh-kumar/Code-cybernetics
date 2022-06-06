# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
low, high = 1500, 2700
k , n = 5, 7
while ( low <= high ) :
    low = low + k
    if ( low % n == 0 ) :
        print ( low )
