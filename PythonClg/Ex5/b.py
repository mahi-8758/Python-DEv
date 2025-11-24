date_string = input("Enter birthday (day,month,year): ")
date_list = date_string.split(",")
birthdays = {
    "day": date_list[0].strip(),
    "month": date_list[1].strip(),
    "year": date_list[2].strip()
}
print("BIRTHDAY INFORMATION")
print(f"Input: {date_string}")
print(f"Split Result: {date_list}")
print(f"Dictionary: {birthdays}")
formatted_birthday = "-".join([birthdays["day"], birthdays["month"], birthdays["year"]])
print(f"Formatted Birthday: {formatted_birthday}")
