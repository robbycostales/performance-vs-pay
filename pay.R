
y16 = read.table("clean/2016.csv", header = TRUE, sep = ",")
y17 = read.table("clean/2017.csv", header = TRUE, sep = ",")

summary(y16)
summary(y17)

plot(y17$Goals, y17$BaseSalary)

