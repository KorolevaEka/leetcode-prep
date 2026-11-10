def pair_distance(values,k):
    lo=0; hi=max(values)-min(values)
    while lo<hi:
        mid=(lo+hi)//2
        count=sum(abs(a-b)<=mid for i,a in enumerate(values) for b in values[i+1:])
        if count<k: lo=mid+1
        else: hi=mid
    return lo
