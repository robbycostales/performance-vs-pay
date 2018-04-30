import pandas

def combine(salary, stats):
    combined = []

    combined.append(["R", "Name", "Club", "Pos", "BaseSalary", "Compensation", "Apps", "SubApps", "Mins", "Goals", "Assists", "Yel", "Red", "SpG", "PS", "AerialsWon", "MotM", "Rating"])

    for index, row in salary.iterrows():
        if str(row["First Name"]).replace(" ", "") == "":
            print("occured1")
            name = str(row["Last Name"]).replace(" ", "")
        elif str(row["Last Name"]).replace(" ", "") == "":
            print("occured2")
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



if __name__ == "__main__":

        salary_16 = pandas.read_csv("manual/16salary.csv", sep="\t")

        stats_16 = pandas.read_csv("accent-free/16stats.csv", sep=",")

        salary_17 = pandas.read_csv("manual/17salary.csv", sep="\t")

        stats_17 = pandas.read_csv("accent-free/17stats.csv", sep="\t")

        y16 = combine(salary_16, stats_16)
        y17 = combine(salary_17, stats_17)

        y16.to_csv("clean/2016.csv")
        y17.to_csv("clean/2017.csv")
