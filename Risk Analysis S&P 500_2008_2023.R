# Install necessary packages
install.packages('dplyr', repos='http://cran.us.r-project.org')
install.packages('lubridate', repos='http://cran.us.r-project.org')
install.packages('ggplot2', repos='http://cran.us.r-project.org')
install.packages('forecast', repos='http://cran.us.r-project.org')
install.packages('tidyr', repos='http://cran.us.r-project.org')
install.packages('PerformanceAnalytics', repos='http://cran.us.r-project.org')

# Load necessary libraries
library(dplyr)
library(lubridate)
library(ggplot2)
library(forecast)
library(tidyr)
library(PerformanceAnalytics)

# Load the dataset
file_path <- 'C:/Users/artur/Downloads/New folder/SandP_stocks_data_2008_2023.csv'
df <- read.csv(file_path)

# Convert the date column to Date type
colnames(df)[1] <- 'Date'
df$Date <- as.Date(df$Date, format='%Y-%m-%d')

# Filter the dataset to include only the top 10 companies
# Top 10 companies identified previously
top_10_companies <- c('TSLA', 'NFLX', 'AVGO', 'NVDA', 'ODFL', 'DXCM', 'TDG', 'DPZ', 'FICO', 'REGN')
df_top_10 <- df %>% select(Date, all_of(top_10_companies))

# Calculate daily returns for the top 10 companies
daily_returns <- df_top_10 %>%
  mutate(across(-Date, ~ (log(. / lag(.))))) %>%
  na.omit()

# Calculate risk metrics: VaR, CVaR, and standard deviation
risk_metrics <- daily_returns %>%
  select(-Date) %>%
  summarise_all(list(
    VaR = ~ VaR(., p = 0.95, method = 'historical'),
    CVaR = ~ CVaR(., p = 0.95, method = 'historical'),
    StdDev = ~ sd(.)
  ))

# Print risk metrics grouped by each company
for (company in top_10_companies) {
  cat(paste0("Risk metrics for ", company, ":\n"))
  cat(paste0("  VaR: ", risk_metrics[[paste0(company, "_VaR")]], "\n"))
  cat(paste0("  CVaR: ", risk_metrics[[paste0(company, "_CVaR")]], "\n"))
  cat(paste0("  StdDev: ", risk_metrics[[paste0(company, "_StdDev")]], "\n"))
  cat("\n")
}

