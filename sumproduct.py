A = [0,2,6,3,15,5,8,4,5,0]


def read_data(file_name):
    with open(file_name, 'r') as f:
        # add N,M
        [N, M] = [int(x) for x in f.readline().split()]

        # add Q
        Q = []
        for i in range(0, N):
            Q_ = [int(x) for x in f.readline().split()]
            Q_.insert(0, 0)
            Q.append(Q_)

        # add d
        d = []
        for i in range(0, M+1):
            d_ = [int(x) for x in f.readline().split()]
            d.append(d_)
        q = [int(x) for x in f.readline().split()]
    return N, M, Q, d, q


N, M, Q, d, q = read_data("./data/data_20_15.txt")
Sum_q = [0 for i in range(len(q))]
Sum_d = 0
for i in range(len(A)-1):
    for j in range(len(q)):
        Sum_q[j]+=Q[j][A[i]]
    Sum_d += d[A[i]][A[i+1]]
print(Sum_q)
print(Sum_d)
print(q)
print(Sum_q>=q)
