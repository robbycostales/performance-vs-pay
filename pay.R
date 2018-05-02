
y16 = read.table("clean/2016.csv", header = TRUE, sep = ",")
y17 = read.table("clean/2017.csv", header = TRUE, sep = ",")
data = read.table("clean/2016-2017.csv", header = TRUE, sep = ",")di


data = data[ which(data$Pos1=='M' 
              | data$Pos2 == 'F'), ]

dimsdata = data.frame(scale(data[, c("R1", "R2", "BaseSalary1", "BaseSalary2", "Compensation1", "Compensation2", "Apps1", 
                            "Apps2", "SubApps1", "SubApps2", "Mins1", "Mins2", "Goals1", "Goals2", "Assists1", "Assists2", "Yel1",         
                            "Yel2", "Red1", "Red2", "SpG1", "SpG2", "PS1", "PS2", "AerialsWon1", "AerialsWon2", "MotM1",
                            "MotM2", "Rating1", "Rating2")]))

mod <- lm( (BaseSalary2 - BaseSalary1) ~ Mins1 +Goals1 + Assists1 + SpG1 + AerialsWon1 + MotM1 + Apps1 + SubApps1 + PS1 + Yel1 + Red1, data=sdata)

summary(mod)

plot(mod)


