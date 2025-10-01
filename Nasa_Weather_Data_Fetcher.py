import requests as rq

# Timeline
# The timeline format is YYYYMMDD
start_date = input("Enter start date (YYYYMMDD): ")
end_date = input("Enter end date (YYYYMMDD): ")
lat = input("Enter latitude: ")
lon = input("Enter longitude: ")


start = str(start_date)
end = str(end_date)


# longitude
lg = str(lon)

# latitude
lt = str(lat)

url = f'https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M&community=SB&longitude={lg}&latitude={lt}&start={start}&end={end}&format=CSV'

response = rq.get(url)

def main(res):
    if res.status_code == 200:
        print('server online')
        print('Do you want to save this data in csv? Y/N')
        user_input1 = str(input(':- '))


        if user_input1.upper() == 'Y':
            user_input2 = str(input('Enter File Name For Saving:- '))
            with open(user_input2, 'w') as f:
                f.write(res.text)


        elif user_input1.upper() == 'N':
            print('File Not Saved')


        else:
            print('ERROR !, Something went wrong ;)')


    elif res.status_code == 422:
        print('Validation Error')

    elif res.status_code == 429:
        print('Too Many Requests')


main(response)
