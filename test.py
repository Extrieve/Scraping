from datetime import datetime

def time_conversion(time):
    hour = int(time[:2])
    conversion = hour % 12

    if hour == 24:
        return f'{conversion}{time[2:]} AM'
    elif hour == 12:
        return time + ' PM'

    if conversion != int(time[:2]):
        time = f'{conversion}{time[2:]} PM'
        return time
    return time + ' AM'


if __name__ == '__main__':
    now = datetime.now()
    current = now.strftime('%H:%M:%S')
    print(current)
    print(time_conversion(current))
    print(time_conversion('07:10:12'))

