def rolling_medians(values,k):
    if not values: return []
    out=[]
    for i in range(len(values)-k+1):
        a=sorted(values[i:i+k]); out.append((a[(k-1)//2]+a[k//2])/2)
    return out
