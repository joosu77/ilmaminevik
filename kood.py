from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

eesti = Point(59.428045, 24.592384)

p = 2

fig,ax = plt.subplots(figsize=(15,10),dpi=400)

for y in range(2005,2023):
    start = datetime(y-1, 12, 1)
    end = datetime(y, 3, 31)


    # Get daily data for 2018
    data = Daily(eesti, start, end)
    data = data.fetch()
    l = list(data.get('tavg'))
    kymp = [(lambda b,e: sum(l[b:e])/(e-b))(max(0,i-p//2),min(len(l)-1,i+p//2)) for i in range(len(l))]

    ax.plot(kymp, color=(lambda x: (x,1,1-x))(round(0.1*(y-2005)/1.7,2)), label=str(y))
    ax.annotate(str(y), (kymp.index(min(kymp)),min(kymp)))
ax.legend()
ax.set_title(f"2005-2022, {p} päeva keskmine")
fig.savefig(f"{p}.png")
