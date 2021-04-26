# Weighted Majority Algorithm

Given 1000 rounds of 16 experts with predictions (0 or 1) and the truth (0 or 1), implement and run the Weighted Majority algorithm with parameter η = 0.01, denoted by WM(η), with dataset sample.txt. Print number of mistakes made by algorithm, the best expert( who has the biggest weight), and calculate the regret bound.

B = number of mistakes made by best expert
m = number of experts
Formula for Regret Bound
2*(1+(η))*B + (2*log(m))/(η)

- Assign each 16 experts with a weight W of 1.00.
- Each round, add up the weights of experts who make the same prediction (0 or 1).
- Choose a policy (0 or 1) depending on the sum of weights of each expert.
- For example, if expert1(with weight 1.0) and expert2(with weight 0.8) chose policy 0 whereas expert3( weight 0.5) and expert4( weight 0.3) chose policy 1 then final policy is 0.
- After the truth is revealed (0 or 1), penalize the experts with different values to the truth by W = W * (1 - η).
- Keep count of number of times an expert has made.

