n=int(input("Enter the number of sequence of Fibonacci: "))
fibo=[1,1]
for i in range(n-2):  # 8 kere iterate ettik.
  fibo.append(fibo[i]+fibo[i+1])
fibo
