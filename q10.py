organise_scores()
TEAM X
def organise_scores(scores,descending):
    if descending == True:
        scores.sort(reverse=True)
    else:
        scores.sort()
    return scores
scores = [int(x) for x in input().split()]
descending = input()
if descending == "True":
    descending = True
else:
    descending = False
organise_scores(scores,descending)
