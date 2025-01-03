import random

def simulate_case2(num_runs):
  """Simulates Case 2 (guaranteed alloy only if no previous alloy, with reset) and returns statistics."""
  w_0 = 17
  total_weight = 307212
  alloys = 0
  guaranteed_alloys = 0
  random_alloys = 0
  tries = 0

  for i in range(1, num_runs + 1):
    tries += 1
    w_new = w_0 * (1 + ((2 * tries) * 1000) / 1000000)
    prob_alloy = (w_new * 19) / total_weight
    if random.random() < prob_alloy:
      alloys += 1
      random_alloys += 1
      tries = 0  # Reset tries
    if tries == 1000:
      alloys += 1
      guaranteed_alloys += 1
      tries = 0  # Reset tries

  avg_runs_per_alloy = num_runs / alloys if alloys > 0 else 0

  return {
      "avg_runs_per_alloy": avg_runs_per_alloy,
      "random_alloys": random_alloys,
      "guaranteed_alloys": guaranteed_alloys,
      "total_alloys": alloys,
  }

# Run simulations
num_simulations = 10000
num_runs = 10000

total_results = {
    "avg_runs_per_alloy": 0,
    "random_alloys": 0,
    "guaranteed_alloys": 0,
    "total_alloys": 0,
}

for _ in range(num_simulations):
  results = simulate_case2(num_runs)
  for key in results:
    total_results[key] += results[key]

# Average the results
for key in total_results:
  total_results[key] /= num_simulations

print(f"Average runs per alloy: {total_results['avg_runs_per_alloy']:.2f}")
print(f"Random alloys dropped: {total_results['random_alloys']:.2f}")
print(f"Guaranteed alloys dropped: {total_results['guaranteed_alloys']:.2f}")
print(f"Total alloys dropped: {total_results['total_alloys']:.2f}")