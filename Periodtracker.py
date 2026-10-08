print("===================================")
print("      🌸🩸Period Tracker🩸🌸")
print("===================================")

name = input("Enter your name: ")
print(f"Hey, {name}! lets track your period.")
print()
print("Your cycle length is the number of days")
print("from the first day of one period to the day before")
print("your next period starts.")
print()


last_period = input("When did your last period start? (Please enter in DD/MM/YYYY format):  ")

while len(last_period) != 10 or last_period[2] != "/" or last_period[5] != "/":
    print("Please enter a valid date in DD/MM/YYYY format.")
    last_period = input("When did your last period start? (Please enter in DD/MM/YYYY format): ")

day = int(last_period[0:2])
month = int(last_period[3:5])
year = int(last_period[6:10])

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

number_of_days = days_in_month[month - 1]

while True:
    try:
        cycle_length = input("How many days is your average cycle? ")
        cycle_length = int(cycle_length)
        if cycle_length >= 21 and cycle_length <= 35:
            break
        else:
            print("Please enter a cycle length between 21 and 35 days.")

    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        period_length = input("How many days does your period usually last? ")
        period_length = int(period_length)
        if period_length >= 1 and period_length <= 7:
            break
        else:
            print("Please enter a period length between 1 and 7 days.")
    except ValueError:
        print("Please enter a valid number.")

print()

print("Hello", name)
print("Your last period started on", last_period)
print("Your average cycle is", cycle_length, "days.")
print("Your period usually lasts", period_length, "days.")




original_day = day
original_month = month
original_year = year

print()
print("🌸 ESTIMATED CYCLE PHASES 🌸")
print()


print("🩸 Menstruation")
print("Your period. The uterus sheds its lining, causing menstrual bleeding.")
print()

menstruation_start_day = original_day
menstruation_start_month = original_month
menstruation_start_year = original_year
menstruation_end_day = original_day + period_length - 1

print("Menstruation_start:", menstruation_start_day, "/", menstruation_start_month, "/", menstruation_start_year)
print("Menstruation End Day:", menstruation_end_day, "/", menstruation_start_month, "/", menstruation_start_year)



print("🌱 Follicular Phase")
print("Your body prepares an egg for ovulation, and estrogen begins to rise.")
print()
ovulation_day = cycle_length - 14
follicular_end = ovulation_day - 1
days_to_follicular_end = follicular_end - 1
follicular_end_date = day + days_to_follicular_end

follicular_month = month

if follicular_end_date > number_of_days:
    follicular_end_date = follicular_end_date - number_of_days
    follicular_month = follicular_month + 1

print("Follicular phase ends:", follicular_end_date, "/", follicular_month, "/", year)


print("🥚 Ovulation")
print("An egg is released from the ovary. Fertility is highest around this time.")
print()
ovulation_day = cycle_length - 14
days_to_ovulation = ovulation_day -1 
ovulation_date = day + days_to_ovulation
ovulation_month = month
if ovulation_date > number_of_days:
    ovulation_date = ovulation_date - number_of_days
    ovulation_month = ovulation_month + 1
print("Ovulation_day is around;", ovulation_date, "/", ovulation_month, "/", year)



print("🌙 Luteal Phase")
print("Your body prepares for a possible pregnancy. If pregnancy does not occur,")
print("hormone levels fall and the next period begins.")
print()
luteal_start = ovulation_day + 1
days_to_luteal = luteal_start - 1

luteal_date = day + days_to_luteal
luteal_month = month

if luteal_date > number_of_days:
    luteal_date = luteal_date - number_of_days
    luteal_month = luteal_month + 1

print("Luteal phase starts:", luteal_date, "/", luteal_month, "/", year)



next_period_day = day + cycle_length
if next_period_day > number_of_days:
    next_period_day = next_period_day - number_of_days
    month = month + 1

print("Next period:", next_period_day, "/", month, "/", year)
print()

print(f"Hey, {name}! You’re doing amazing, girl. Be gentle with yourself, listen to your body, and remember, you’ve got this. 💕")


