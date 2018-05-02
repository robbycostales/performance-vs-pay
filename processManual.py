import pandas

def combine(salary, stats):
    combined = []

    combined.append(["R", "Name", "Club", "Pos", "BaseSalary", "Compensation", "Apps", "SubApps", "Mins", "Goals", "Assists", "Yel", "Red", "SpG", "PS", "AerialsWon", "MotM", "Rating"])

    for index, row in salary.iterrows():
        if str(row["First Name"]).replace(" ", "") == "nan":
            name = str(row["Last Name"]).replace(" ", "")
        elif str(row["Last Name"]).replace(" ", "") == "nan":
            name = str(row["First Name"]).replace(" ", "")
        else:
            name = str(row["First Name"]).replace(" ", "") +" "+ str(row["Last Name"]).replace(" ", "")

        stat_temp = stats.loc[stats["Player"].str.contains(name)]

        # get rid of rows where no such row was found
        if len(stat_temp)!=1:
            continue
        # otherwise we continue and include it

        R = stat_temp["R"]
        R = int(R)

        Name = name

        Club = str(row["Club"].replace(" ", ""))

        Pos = row["Pos"].replace("/", "-")
        Pos = Pos.split("-")
        Pos = str(Pos[0])

        BaseSalary = row["Base Salary"]
        BaseSalary = float(BaseSalary.replace("$", "").replace(",", ""))

        Compensation = row["Compensation"]
        Compensation = float(Compensation.replace("$", "").replace(",", ""))

        Apps = stat_temp["Apps"].values[0]
        Apps = Apps.split("(")
        try:
            SubApps = int(Apps[1].replace(")", ""))
        except:
            SubApps = 0
        Apps = int(Apps[0])

        Mins = int(stat_temp["Mins"].values[0])

        Goals = str(stat_temp["Goals"].values[0])
        if "-" in Goals:
            Goals = 0
        Goals = int(Goals)

        Assists = stat_temp["Assists"].values[0]
        if "-" in Assists:
            Assists = 0
        Assists = int(Assists)

        Yel = stat_temp["Yel"].values[0]
        if "-" in Yel:
            Yel = 0
        Yel = int(Yel)

        Red = stat_temp["Red"].values[0]
        if "-" in Red:
            Red = 0
        Red = int(Red)

        SpG = str(stat_temp["SpG"].values[0])
        if "-" in SpG:
            SpG = 0
        SpG = float(SpG)

        PS = stat_temp["PS%"].values[0]
        PS = float(PS)

        AeiralsWon = stat_temp["AeiralsWon"].values[0]
        if "-" in AeiralsWon:
            AeiralsWon = 0
        AeiralsWon = float(AeiralsWon)

        MotM = stat_temp["MotM"].values[0]
        if "-" in MotM:
            MotM = 0
        MotM = int(MotM)

        Rating = stat_temp["Rating"].values[0]
        Rating = float(Rating)

        combined.append([R, Name, Club, Pos, BaseSalary, Compensation, Apps, SubApps, Mins, Goals, Assists, Yel, Red, SpG, PS, AeiralsWon, MotM, Rating])


    combined = pandas.DataFrame(combined[1:],columns=combined[0])

    return combined

def combineClean(y1, y2):

    combined = []

    combined.append(["R1", "R2", "Name1", "Name2", "Club1", "Club2", "Pos1", "Pos2", "BaseSalary1", "BaseSalary2", "Compensation1", "Compensation2", "Apps1", "Apps2", "SubApps1", "SubApps2", "Mins1", "Mins2", "Goals1", "Goals2", "Assists1", "Assists2", "Yel1", "Yel2", "Red1", "Red2", "SpG1", "SpG2", "PS1", "PS2", "AerialsWon1", "AerialsWon2", "MotM1", "MotM2", "Rating1", "Rating2"])

    for index, row in y1.iterrows():
        stat_temp = y2.loc[y2["Name"].str.contains(row["Name"])]

        if len(stat_temp)!=1:
            continue

        R1 = row["R"]
        R2 = stat_temp["R"].values[0]

        Name1 = row["Name"]
        Name2 = stat_temp["Name"].values[0]

        Club1 = row["Club"]
        Club2 = stat_temp["Club"].values[0]

        Pos1 = row["Pos"]
        Pos2 = stat_temp["Pos"].values[0]

        BaseSalary1 = row["BaseSalary"]
        BaseSalary2 = stat_temp["BaseSalary"].values[0]

        Compensation1 = row["Compensation"]
        Compensation2 = stat_temp["Compensation"].values[0]

        Apps1 = row["Apps"]
        Apps2 = stat_temp["Apps"].values[0]

        SubApps1 = row["SubApps"]
        SubApps2 = stat_temp["SubApps"].values[0]

        Mins1 = row["Mins"]
        Mins2 = stat_temp["Mins"].values[0]

        Goals1 = row["Goals"]
        Goals2 = stat_temp["Goals"].values[0]

        Assists1 = row["Assists"]
        Assists2 = stat_temp["Assists"].values[0]

        Yel1 = row["Yel"]
        Yel2 = stat_temp["Yel"].values[0]

        Red1 = row["Red"]
        Red2 = stat_temp["Red"].values[0]

        SpG1 = row["SpG"]
        SpG2 = stat_temp["SpG"].values[0]

        PS1 = row["PS"]
        PS2 = stat_temp["PS"].values[0]

        AerialsWon1 = row["AerialsWon"]
        AerialsWon2 = stat_temp["AerialsWon"].values[0]

        MotM1 = row["MotM"]
        MotM2 = stat_temp["MotM"].values[0]

        Rating1 = row["Rating"]
        Rating2 = stat_temp["Rating"].values[0]

        combined.append([R1, R2, Name1, Name2, Club1, Club2, Pos1, Pos2, BaseSalary1, BaseSalary2, Compensation1, Compensation2, Apps1, Apps2, SubApps1, SubApps2, Mins1, Mins2, Goals1, Goals2, Assists1, Assists2, Yel1, Yel2, Red1, Red2, SpG1, SpG2, PS1, PS2, AerialsWon1, AerialsWon2, MotM1, MotM2, Rating1, Rating2])

    combined = pandas.DataFrame(combined[1:],columns=combined[0])

    return combined




if __name__ == "__main__":

        salary_16 = pandas.read_csv("manual/16salary.csv", sep="\t")

        stats_16 = pandas.read_csv("accent-free/16stats.csv", sep=",")

        salary_17 = pandas.read_csv("manual/17salary.csv", sep="\t")

        stats_17 = pandas.read_csv("accent-free/17stats.csv", sep="\t")

        y16 = combine(salary_16, stats_16)
        y17 = combine(salary_17, stats_17)

        y16.to_csv("clean/2016.csv")
        y17.to_csv("clean/2017.csv")

        data = combineClean(y16, y17)
        data.to_csv("clean/2016-2017.csv")
