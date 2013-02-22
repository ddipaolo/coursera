"""The Viterbi Algorithm

Input: a sentence x_1 ... x_n, parameters q(s|u,v) and e(x|s)

Initialization:  Set pi(0, *, *) = 1

Definition: S_-1 = S_0 = {*}, S_k = S for k in {1..n}

Algorithm:

  For k = 1 .. n
     For u in S_k-1, v in S_k
        pi(k,u,v) = max_(w in S_k-2) (pi(k-1,w,u) * q(v|w,u) * e(x_k|v))

  Return max_(u in S_n-1,v in S_n) (pi(n,u,v) * q(STOP|u,v))
"""
