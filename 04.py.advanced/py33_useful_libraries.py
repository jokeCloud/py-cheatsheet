import re
from dateutil.tz import UTC, tzlocal, gettz
from datetime import date, time, datetime, timedelta
from random import random, randint, choice, shuffle
from statistics import mean, median, variance, pvariance, pstdev
from math import inf, nan, isinf, isnan
from math import log, log10, log2
from math import cos, acos, sin, asin, tan, atan, degrees, radians
from math import e, pi
from time import time
import pickle
import json
import csv


def read_csv_file(filename):
    with open(filename, encoding='utf-8') as file:
        return csv.reader(file, delimiter=';')


def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)


start_time = time()

duration = time() - start_time


print(random())
print(randint(0, 100))
random_el = choice([1, 2, 3, 4])
print(random_el)
s = shuffle([1, 2, 3, 4])
print(s)

d = date(year, month, day)
t = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
dt = datetime(year, month, day, hour=0, minute=0, second=0)
td = timedelta(days=0, seconds=0, microseconds=0,
               milliseconds=0, minutes=0, hours=0, weeks=0)


string = re.sub(regex, new, text, count=0)
list = re.findall(regex, text)
list = re.split(regex, text, maxsplit=0)

string = a.group()
string = a.group(1)
tupla = a.groups()
tupla = a.start()
inteiro = a.end()
