def latest(scores):
   return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_list = sorted(scores)
    sorted_list.reverse()
    count = len(scores)

    if count == 1 or count == 2:
        return sorted_list
    else:
        return sorted_list[0:3]