import pandas as pd
test = pd.read_csv('https://docs.google.com/spreadsheets/d/1Xpfs6p6yzCxH4RUm-hFX4csd7AH5-4N8OwwXTc1Db4Q/edit?gid=0#gid=0',
                   # Set first column as rownames in data frame
                   index_col=0,
                   # Parse column values to datetime
                   parse_dates=['Quradate']
                  )
print(test.head(5))  # Same result as @TomAugspurger
