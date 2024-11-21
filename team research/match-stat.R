library(readr)

#import dataset
match_stat <- read.csv('/Users/ekow/Desktop/CN&SS/team research and dev/match-stat.csv')
print(match_stat)
summary(match_stat)
#length(rows) = 113514
#variables(columns) = 25

#checking missing values (independent variable)
ftr <- na.omit(match_stat$FTR)
summary(ftr)
#checking missing values (dependent variable)
hst <- na.omit(match_stat$HST)
str(hst) #56024 missing values

#clean data without missing values in dependent variable
match_stat_clean <- match_stat[!is.na(match_stat$HST),]

#drop "D" value from independent variable
match_stat_clean <- match_stat_clean[match_stat_clean$FTR != "D", ,drop = FALSE]
head(match_stat_clean, 100)

#histogram of dependent variable
hist(match_stat_clean$HST, breaks = 25, xlim = c(-2, 25), ylim = c(0, 7000), col = "lightgreen")
m_hst <- mean(match_stat_clean$HST) #mean
sd_hst <- sd(match_stat_clean$HST) #standard deviation
#Scale the normal distribution curve to match the histogram frequency
curve(dnorm(x, mean = m_hst, sd = sd_hst) * length(match_stat_clean$HST) * diff(hist(match_stat_clean$HST, plot = FALSE, breaks = 20)$breaks)[1] / 1,
      col = "blue", # Color of the curve
      lwd = 1.5,      # Line width
      add = TRUE)   # Add the curve to the existing histogram

#boxplot for differences in average
boxplot(match_stat_clean$HST ~ match_stat_clean$FTR, col = "lightyellow", pch = 20)
