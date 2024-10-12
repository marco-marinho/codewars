MOD = 998244353
inverse=[0,1]
for i in range(2,80001):
    inverse.append(((i-inverse[MOD%i])*(MOD//i)+MOD%i)%MOD)

def height(n, m):  
    ret, trm = 0, 1
    m %= MOD
    for i in range(1, n + 1): 
        trm = trm * (m - i + 1) * inverse[i] % MOD
        ret = (ret + trm) % MOD
    return ret % MOD   