# Final Project: Supply Chain Network Design

## Project Overview

In this final project, each team will act as supply chain consultants hired by a company to optimize the build-out of **new distribution facilities**. The project integrates concepts from the last four modules of the course. Each team is a given a **distinct industry scenario** with different data, but all teams will solve a similar style of optimization problem. The core objectives  are to determine **where to open new facilities and how to route product flows** in order to meet customer demand at minimum cost, and to develop a **strategy under demand uncertainty**.

## Key Tasks

- Formulating a linear optimization model (using Gurobi in Python) for facility location and network flow.
- Solving the model to find the optimal network design.
- Performing a strategic analysis under uncertainty; the emphasis is on **interpreting results and making recommendations** rather than on complex coding.
- Each team will present a 10 to 15 minute strategy pitch to the class (as if presenting to the company's executives), focusing on insights, results, visuals, and recommendations.

## Common Assumptions

- All customer demand must be met (no shortages/back orders).
- Products flow from supply centers through distribution centers to customers (no direct shipping from suppliers to customers in the new design).
- Each potential facility and supply source has a capacity limit (throughput or production) as provided.
- Transportation cost is assumed to be linear with distance (given in each scenario).
- Demand has two possible levels (current "low" and future "high" growth) with a given probability for each scenario.

## Expected Deliverables

1. **Optimization Model & Analysis (Python/Gurobi)**: A well-documented Python script or Jupyter notebook that formulates the linear programming model and solves for the optimal facility locations and shipment plan for your scenario. This should include the formulation of decision variables (facility open/closed, shipment flows), constraints (supply capacities, facility capacities, demand satisfaction, etc.), and the objective function (minimizing total cost). The code should be clear and commented, but remember that complex code is not the focus, you may use techniques from class or even Gurobi's built-in modeling assistance. The important part is that your model correctly captures the scenario and produces a valid optimal solution. You should solve the model for at least the low-demand case and the high-demand case. (It's recommended to also use the model results to inform your uncertainty analysis, e.g., total costs in each scenario and which facilities would be used.)

2. **Scenario Strategy Presentation (10-15 minutes)**: A slide deck (PowerPoint, Google Slides, etc.) to present in class. Treat this as a consultant's executive briefing to the client company:

- Begin with an introduction of the company's situation and the problem statement in business terms.
- Explain your approach (briefly) to solving the network design problem (e.g., "we built an optimization model to evaluate potential distribution center locations and shipping plans"). **Do not include code on slides**, but it's appropriate to mention the tools (Python/Gurobi) and any assumptions in a non-technical way.
- Present the **results of your optimal network design**: Which facilities should be opened and where? What are the expected cost savings or service improvements? Use visuals such as maps, charts, or graphs to make this clear. For example, a map showing demand locations and the chosen warehouses, with lines indicating the flow of goods, would be very effective. Charts might include cost breakdown comparisons (status quo vs. new design, or low vs. high demand scenarios).
- Discuss the **uncertainty analysis**: Outline the demand scenarios (low vs high) and present a simple decision tree or table with the cost outcomes for different strategies. State the probabilities and calculate the **expected cost** or benefit for each strategy. Highlight any important metrics (e.g., the cost of being wrong - what if you under-invest and demand booms? or what if you over-invest and demand stays low?). This part should lead to a clear recommendation.
- **Recommendation and Conclusion**: Based on your analysis, what do you recommend the company do? For example: "We recommend opening two fulfillment centers - one in Los Angeles and one in Newark - which in the high-demand case yields $X in savings versus no expansion, and in the low-demand case still operates efficiently with only a $Y cost increase. The expected annual cost savings of this strategy is $Z. This balanced approach positions the company well for growth while controlling risk if growth is slower." Tailor your recommendation to your scenario's context.
- **Reflection (Meta slide)**: Include one slide (toward the end or as an appendix) reflecting on the modeling and coding aspect. This is where you briefly mention any challenges encountered in building the model or using Gurobi/Python, and key learnings from the process (e.g., "We learned how to formulate capacity constraints and the importance of data cleaning for distance calculations," or "One challenge was ensuring the binary facility decisions correctly applied to flow decisions - we resolved this with big-M constraints"). This slide gives insight into the work behind the scenes, but keep it high-level.

3. **Supporting Files**: Along with the presentation, submit your Python code and any supporting analysis (for example, an Excel sheet or PDF where you may have calculated the decision tree expected values, if not in the slides). The code and calculations will be reviewed for correctness and depth. However, during the presentation, you will focus on interpretation, so ensure your results in the slides are accurate and consistent with your code's output.

**Note**: All team members should be prepared to answer questions about the model and the scenario during the Q&A. The presentation should be cohesive and professional, as if you are pitching your solution to the company's executives who may not be technical - emphasize insights, not equations. Use plain language to explain the benefit of your optimization (e.g., "by opening the new warehouse, we cut the average shipping distance by 40%, leading to $500k annual savings").
