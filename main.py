arr = [(2,'asb'),(1,'bas'),(3,'abb'),(5,'bcc'),(2,'c')]
arr.sort(key = lambda x: id(x[1]))
print(arr)