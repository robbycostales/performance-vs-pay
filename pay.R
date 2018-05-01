
y16 = read.table("clean/2016.csv", header = TRUE, sep = ",")
y17 = read.table("clean/2017.csv", header = TRUE, sep = ",")

summary(y16)
summary(y17)

for(i in 1:nrow(y16)) {
  row <- y16[i,]
  x = match(row$Name, y17$Name)
  print(x)
  
  
}
