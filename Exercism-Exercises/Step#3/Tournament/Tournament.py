def tally(rows):
    r = [row.split(";") for row in rows]
    keys = ["MP", "W", "D", "L", "P"]
    table = {k: {key: 0 for key in keys} for row in r for k in row[:2]}

    for row in r:
        table[row[0]]["MP"] += 1
        table[row[1]]["MP"] += 1

        if row[2] == "win":
            table[row[0]]["W"] += 1
            table[row[0]]["P"] += 3
            table[row[1]]["L"] += 1


        elif row[2] == "loss":
            table[row[1]]["W"] += 1
            table[row[1]]["P"] += 3
            table[row[0]]["L"] += 1


        elif row[2] == "draw":
            table[row[1]]["D"] += 1
            table[row[1]]["P"] += 1
            table[row[0]]["D"] += 1
            table[row[0]]["P"] += 1

    order = sorted(table.keys(), key=lambda a: (-table[a]["P"], a.lower()))

    result = ["Team                           | MP |  W |  D |  L |  P"]

    f = "{:30} |{:3} |{:3} |{:3} |{:3} |{:3}"

    for teams in order:
        result.append(f.format(teams, table[teams]["MP"], table[teams]["W"],
                               table[teams]["D"], table[teams]["L"], table[teams]["P"]))

    return result
