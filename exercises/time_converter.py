def main():
    max_long = 9223372036854775807
    hours = max_long / 3600000
    days = hours / 24
    years = days / 365
    print("{0} hours, {1} days, {2} years".format(hours, days, years))

if __name__ == '__main__':
    main()