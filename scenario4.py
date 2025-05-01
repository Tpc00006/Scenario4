

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    ## Scenario 4: SpeedCart Online

    ### 1. Model Formulation

    **Decision Variables**

    - $x_m \in\{0,1\}$ for each candidate fulfillment center _m_ (Newark, Atlanta, Dallas, LA)  
    - $f_{m}≥0$: weekly flow from Kansas City to center _m_  
    - $g_{m,r}≥0$: weekly flow from center _m_ to region cluster _r_ (NY, CHI, ATL, DAL, LA)

    **Constraints**

    1. KC capacity 700: $∑_m f_m ≤ 700$
    2. Center capacity 500 if built: $f_m ≤ 500 x_m, \; ∑_r g_{m,r} ≤ 500 x_m$
    3. Flow balance: $f_m = ∑_r g_{m,r}$
    4. Demand: $∑_m g_{m,r} = D_r$

    **Objective**

    $$
    \min \sum_m F_m x_m + 0.7 \sum_m dist(KC,m) f_m + 0.7 \sum_{m,r} dist(m,r) g_{m,r}
    $$
    """,
    name="_"
)


@app.cell
def _():
    ### 2. Data Definition
    supplies = [("KC", (2136,711), 700)]
    dcs = [
        ("Newark",    (3896,892), 130_000, 500),
        ("Atlanta",   (3015,117), 110_000, 500),
        ("Dallas",    (1945, 10), 110_000, 500),
        ("LA",        (  95,151), 130_000, 500),
    ]
    demands = [
        ("NYC",     (3911,890),  90,130),
        ("Chicago", (2736,1020), 80,120),
        ("ATL",     (3015,117),  70,100),
        ("DAL",     (1945,10),   60, 90),
        ("LA",      (95,151),   100,150),
    ]
    transport_cost = 0.7
    prob = {"low":0.3, "high":0.7}
    return dcs, demands, prob, supplies, transport_cost


@app.cell
def _(cl, dcs, demands, lo, prob, supplies, transport_cost):
    ### 3. Python/Gurobi Code
    import gurobipy as gp
    from gurobipy import GRB
    import math

    def dist4(a,b): return math.hypot(a[0]-b[0], a[1]-b[1])

    def solve_speedcart(case):
        m=gp.Model(); m.Params.OutputFlag=0
        x={m_:m.addVar(vtype=GRB.BINARY,name=f"x_{m_}") for m_,_,_,_ in dcs}
        f={m_:m.addVar(lb=0,name=f"f_{m_}") for m_,_,_,_ in dcs}
        g={(m_,r):m.addVar(lb=0,name=f"g_{m_}_{r}") for m_,_,_,_ in dcs for r,_,_,_ in demands}
        m.update()
        expr=gp.quicksum(fc*x[m_] for m_,_,fc,_ in dcs)
        for m_,coordm,_,_ in dcs:
            expr+=transport_cost*dist4(supplies[0][1],coordm)*f[m_]
            for r,coordr,low,high in demands:
                expr+=transport_cost*dist4(coordm,coordr)*g[m_,r]
        m.setObjective(expr,GRB.MINIMIZE)
        m.addConstr(sum(f[m_] for m_,_,_,_ in dcs)<=supplies[0][2])
        for m_,_,_,cap in dcs:
            m.addConstr(f[m_]<=cap*x[m_])
            m.addConstr(sum(g[m_,r] for r,_,_,_ in demands)<=cap*x[m_])
            m.addConstr(f[m_]==sum(g[m_,r] for r,_,_,_ in demands))
        for r,_,low,high in demands:
            req=low if case=='low' else high
            m.addConstr(sum(g[m_,r] for m_,_,_,_ in dcs)==req)
        m.optimize()
        return [m_ for m_ in x if x[m_].X>0.5], m.ObjVal

        lo,cl=solve_speedcart('low')
    hi,ch=solve_speedcart('high')
    A=ch; B_lo=cl; B_hi=ch  # assume no second cost
    EVA=prob['low']*A+prob['high']*A
    EVB=prob['low']*B_lo+prob['high']*B_hi
    print("Scenario 4")
    print(lo,cl)
    print(hi,ch)
    print(EVA,EVB)
    print("Recommend:","Build broadly" if EVA<EVB else "Minimal build")
    return


app._unparsable_cell(
    r"""
    ### 4. Results Interpretation & Recommendation

    1. **Low**: open `lo` (cost `cl`)  
    2. **High**: open `hi` (cost `ch`)  
    3. **Expected cost**: `EVA` vs `EVB`; choose smaller  
    4. **Comment** on service speed and growth readiness
    """,
    name="_"
)


@app.cell
def _():
    import marimo as mo
    return


if __name__ == "__main__":
    app.run()
