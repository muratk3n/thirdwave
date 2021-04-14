import datetime, sys, os


ys = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2016,2018,2019,2020]
if sys.argv[1] == 'years':
    for year in ys:
        os.system("echo '# %d\n' > %d/README.md" % (year,year))
        os.system("python -u gen.py %d >> %d/README.md" % (year,year))
