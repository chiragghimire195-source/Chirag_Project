scores = [88, 45, 72, 95, 60, 38, 81]

pass_count = 0

for score in scores:
    if score >= 50:
        print(score, "- Pass")
        pass_count += 1
    else:
        print(score, "- Fail")

print("Total passed:", pass_count)