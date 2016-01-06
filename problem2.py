__author__ = 'runwei_zhang'
import csv
import operator
import math
import matplotlib.pyplot as plt
from datetime import datetime
import time

def experiment1():
    hist = dict()
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        count = 0.0  #10012260
        for row in reader:
            count += 1
            if row['Agency'] in hist:
                hist[row['Agency']] += 1
            else:
                hist[row['Agency']] = 1
    sorted_x = sorted(hist.items(), key=operator.itemgetter(1),reverse=True)
    print sorted_x[1][1]/count

def experiment2():
    complainBorough = dict()
    complain = dict()
    borough = dict()
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',') #,quotechar="'"
        for row in reader:
            if row['Borough'] not in complainBorough:
                complainBorough[row['Borough']] = {}
            if row['Complaint Type'] not in complainBorough[row['Borough']]:
                complainBorough[row['Borough']][row['Complaint Type']] = 0
            complainBorough[row['Borough']][row['Complaint Type']] += 1.0
            if row['Complaint Type'] not in complain:
                complain[row['Complaint Type']] = 1.0
            else:
                complain[row['Complaint Type']] += 1.0
            if row['Borough'] not in borough:
                borough[row['Borough']] = 1.0
            else:
                borough[row['Borough']] += 1.0
    maxbr,maxcp,maxval,totalcount = '','',0.0,sum(borough.values())
    for br in complainBorough:
        for cp in complainBorough[br]:
            if complainBorough[br][cp]*totalcount/borough[br]/complain[cp]>maxval:
                maxbr,maxcp = br,cp
    print maxbr, maxcp
    print complainBorough[maxbr][maxcp]
    print complain[maxcp]
    print complainBorough[maxbr][maxcp]*totalcount/borough[maxbr]/complain[maxcp]

def experiment3():
    hist = dict()
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        lonlist = []
        for row in reader:
        # for i in xrange(0,100000):
        #     row = next(reader)
            lonlist.append(row['Latitude'])
        lonlist = [x for x in lonlist if is_number(x)]
        sorted_list = sorted(lonlist)
        print min(sorted_list), max(sorted_list)
        percentile10 = int(math.ceil(len(sorted_list)*0.1))
        percentile90 = int(math.ceil(len(sorted_list)*0.9))
        print percentile10, percentile90
        print float(sorted_list[percentile90])-float(sorted_list[percentile10])

def experiment4():
    meanlat = 0.0
    meanlon =0.0
    count = 0.0
    cov_xx = 0.0
    cov_yy = 0.0
    cov_xy =0.0
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if is_number(row['Longitude']) and is_number(row['Latitude']):
                meanlon += float(row['Longitude'])
                meanlat += float(row['Latitude'])
                count += 1.0
        meanlon /= count
        meanlat /= count
        csvfile.seek(0)
        print meanlon, meanlat
        for row in reader:
            if is_number(row['Longitude']) and is_number(row['Latitude']):
                cov_xx += (float(row['Longitude'])-meanlon)* (float(row['Longitude'])-meanlon)
                cov_yy += (float(row['Latitude'])-meanlat)* (float(row['Latitude'])-meanlat)
                cov_xy += (float(row['Longitude'])-meanlon)* (float(row['Latitude'])-meanlat)
        cov_xx /= count
        cov_yy /= count
        cov_xy /= count
        print cov_xx, cov_yy, cov_xy
        print math.sqrt(cov_xx*cov_yy-cov_xy*cov_xy)*math.pi*111.13175*111.13175 * math.cos(math.radians(meanlat))

def experiment5():
    hist = dict()
    days = set()
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dt = datetime.strptime(row['Created Date'],'%m/%d/%Y %I:%M:%S %p')
            if dt.hour !=0 or dt.minute!=0 or dt.second!=0:
                if dt.hour not in hist:
                    hist[dt.hour] =1.0
                else:
                    hist[dt.hour] +=1.0
                if dt.date() not in days:
                    days.add(dt.date())
    print (max(hist.values())- min(hist.values()))/len(days)
    plt.bar(hist.keys(), hist.values())
    plt.show()

def experiment6():
    timelist = []
    with open('nyc311calls.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        flag = True
        for row in reader:
        # for i in range(0,1000000):
        #     row = next(reader)   #gets the first line
            if flag:
                flag = False
                continue
            dt = datetime.strptime(row['Created Date'],'%m/%d/%Y %I:%M:%S %p')
            if dt.hour !=0 or dt.minute!=0 or dt.second!=0:
                timelist.append(time.mktime(dt.timetuple()))
    timediff = dict()
    meantimediff = 0.0
    sigma = 0.0
    for i in xrange(0,len(timelist)-2):
        waittime = timelist[i]-timelist[i+1]
        if waittime<0:
            continue
        meantimediff += waittime
        if waittime not in timediff:
            timediff[waittime] =1
        else:
            timediff[waittime] +=1
    meantimediff /= len(timelist)-1
    sorted_table = sorted(timediff)
    print sorted_table[0], sorted_table[len(sorted_table)-1]
    print meantimediff
    for waittime in timediff:
        sigma += (waittime-meantimediff) * (waittime-meantimediff)
    sigma = math.sqrt(sigma/(len(timelist)-1))
    print sigma
    plt.bar(timediff.keys(), timediff.values())
    plt.show()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


if __name__ == "__main__":
    experiment6()