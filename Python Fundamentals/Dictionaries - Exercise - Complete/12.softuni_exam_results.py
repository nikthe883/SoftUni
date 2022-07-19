submission_participants = input().split("-")

results = {}
submissions = {}

while submission_participants[0] != "exam finished":

    if submission_participants[1] == "banned":
        del results[submission_participants[0]]
    else:

        if submission_participants[0] in results:
            if int(submission_participants[2]) > int(results[submission_participants[0]]):
                results[submission_participants[0]] = submission_participants[2]
        else:
            results[submission_participants[0]] = submission_participants[2]

        if submission_participants[1] in submissions:
            submissions[submission_participants[1]] += 1
        else:
            submissions[submission_participants[1]] = 1

    submission_participants = input().split("-")

print("Results:")
for k, v in results.items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in submissions.items():
    print(f"{k} - {v}")
