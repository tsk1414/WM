# Weighted Majority Algorithm

Given 1000 rounds of 16 experts with predictions (0 or 1) and the truth (0 or 1), implement and run the Weighted Majority algorithm with parameter η = 0.01, denoted by WM(η), with dataset sample.txt.

- Assign each 16 experts with a weight W of 1.00.
- Each round, add up the weights of experts who make the same prediction (0 or 1).
- After the truth is revealed (0 or 1), penalize the experts with different values to the truth by W = W * (1 - η).
