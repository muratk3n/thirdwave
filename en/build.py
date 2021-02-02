import datetime, sys, os

if sys.argv[1] == 'week':
    my_date = datetime.date.today() # if date is 01/01/2018
    year, week_num, day_of_week = my_date.isocalendar()
    print("Week #" + str(week_num) + " of year " + str(year))

if sys.argv[1] == 'years':
    for year in range(2007,2022):
        os.system("echo '# %d\n' > %d/README.md" % (year,year))
        os.system("python -u gen.py %d >> %d/README.md" % (year,year))
