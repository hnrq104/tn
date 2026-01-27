import math

def calculate_fraction_from_cc(cc:list[int]):
    prev_x, current_x = 1, cc[0]
    prev_y, current_y = 0, 1

    for a in cc[1:]:
        cx,cy = current_x, current_y
        current_x = a*current_x + prev_x
        current_y = a*current_y + prev_y
        prev_x, prev_y = cx, cy


''' yields the (an, pn, qn)'''
def continued_frac_representation(x):
    a = math.floor(x)
    alpha = x - a
    current_p, prev_p = a, 1
    current_q, prev_q = 1, 0
    
    while True:
        yield a, current_p, current_q
        if alpha == 0:
            return
        y = 1/alpha
        a = math.floor(y)
        alpha = y - a

        cp,cq = current_p, current_q
        current_p = a*current_p + prev_p
        current_q = a*current_q + prev_q
        prev_p = cp
        prev_q = cq

N = 10
cc_gen = continued_frac_representation(math.pi)

cc = []
pq = []

for _ in range(100):
    a, p, q = next(cc_gen)
    cc.append(a)
    pq.append((p,q))
    # print(f"{a} {p} {q} {p/q:.10f} {(p/q)**2:.10f}")

print(cc)
