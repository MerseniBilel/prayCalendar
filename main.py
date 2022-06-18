import json
import requests

prays = []




def clearData(filename, output):
    # read json file
    with open(filename) as json_file:
        # json data
        data = json.load(json_file)
        # loop 12 month
        for i in range(1,13):
            # current month
            month = data['data'][str(i)]
            theDay = {}
            # loop days in current month
            for day in month:
                # current day
                dayPray = {};
                dayPray['Fajr'] = day['timings']['Fajr'][:6];
                dayPray['Dhuhr'] = day['timings']['Dhuhr'][:6];
                dayPray['Asr'] =  day['timings']['Asr'][:6];
                dayPray['Maghrib'] = day['timings']['Maghrib'][:6];
                dayPray['Isha'] = day['timings']['Isha'][:6];
                theDay[day['date']['readable']] = dayPray;
            # append current month to list
            prays.append(theDay);    
  
    # write to json file
    with open(output, 'w') as outfile:
        json.dump(prays, outfile)


def getData(url):
    # get data from url
    response = requests.get(url)
    # convert to json
    data = response.json()
    # write to json file
    with open('prays.json', 'w') as outfile:
        json.dump(data, outfile)
    


def main():
    url = 'http://api.aladhan.com/v1/calendar?latitude=37.169375&longitude=10.033648&method=3&year=2021&annual=true'
    getData(url)
    clearData('prays.json', '2021.json')
    
    
   
__name__ == '__main__' and main()
