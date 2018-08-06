import matplotlib.pyplot as plt

x = []
y = []
p = {}
f = open("xrd.txt","r")
lines = f.readlines()
lines = lines[6:]

for line in lines:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))

for i in range(1,len(y)-1):
    if y[i-1] < y[i] and y[i+1] < y[i] and y[i] > 1000:
        p[y[i]] = x[i]
        
print(sorted(p.items(),reverse=True))

plt.plot(x,y,linewidth=0.8)
plt.show()
