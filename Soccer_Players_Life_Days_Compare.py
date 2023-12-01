from datetime import datetime

# a dictionary/hash map, to map alphabetical user's input to a number 
class MonthConverter:

  def __init__(self):
    self.month_dict = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }

  # implementing the dictionary and error handling in case of unwanted user input
  def convert(self, month_name):
    month_name = month_name.lower()
    if month_name in self.month_dict:
      return self.month_dict[month_name]
    else:
      raise ValueError("Please enter a full month's name")

# date of birth request with implemented error handling
def dateOfBirth():
  year = int(input("What year were you born? "))
  if year < 1900 or year > datetime.today().year:
    raise ValueError("Provide a valid birth year")

  month_name = input("What month were you born? ")
  converter = MonthConverter()
  month = converter.convert(month_name)

  day = int(input("What day were you born? "))
  if day < 1 or day > 31:
    raise ValueError("Try a number between 1 and 31")

  # calculating delta between a given date and today's date using datetime library
  birth_date = datetime(year, month, day)
  today = datetime.today()
  difference = today - birth_date
  return difference.days

# initializing a user and requesting a user's name
class User:

  def __init__(self, name):
    self.name = name

u1 = User(input("What is your name? "))

# defining and initializing soccer players
class soccerCeleb:

  def __init__(self, name, dob):
    self.name = name
    self.dob = dob

  def celeb_date_convert(self):
    today = datetime.today()
    difference = today - self.dob
    return difference.days

Messi = soccerCeleb("Lionel Messi", datetime(1987, 6, 24))
Ronaldo = soccerCeleb("Cristiano Ronaldo", datetime(1985, 5, 24))
Mbappe = soccerCeleb("Kylian Mbappe", datetime(1998, 12, 24))
Lewandowski = soccerCeleb("Robert Lewandowski", datetime(1988, 2, 24))
Neymar = soccerCeleb("Neymar", datetime(1992, 5, 24))
Beckham = soccerCeleb("David Beckham", datetime(1975, 5, 2))
Ronaldinho = soccerCeleb("Ronaldinho", datetime(1980, 3, 21))
Boniek = soccerCeleb("Zbigniew Boniek", datetime(1956, 3, 3))

# getting the number of days the user has been alive
user_days_alive = dateOfBirth()

# extracting the players' names to the respective list by comparing the user's age to the soccer players' ages
older_than = []
younger_than = []
for player in [Messi, Ronaldo, Mbappe, Lewandowski, Neymar, Beckham,Ronaldinho, Boniek]:
  if user_days_alive > player.celeb_date_convert():
    older_than.append(player.name)
  else:
    younger_than.append(player.name)

#output printing
print("Congrats!" + u1.name)
print("You have been on this world for " + str(user_days_alive) + " days!")
print("Congrats! You are older than: " + ", ".join(older_than)) #joining strings with lists
print("And you are younger than: " + ", ".join(younger_than))
print(Messi.name, "has been alive for", Messi.celeb_date_convert(), "days.")
print(Ronaldo.name, "has been alive for", Ronaldo.celeb_date_convert(),
      "days.")
print(Mbappe.name, "has been alive for", Mbappe.celeb_date_convert(), "days.")
print(Lewandowski.name, "has been alive for", Lewandowski.celeb_date_convert(),
      "days.")
print(Neymar.name, "has been alive for", Neymar.celeb_date_convert(), "days.")
print(Beckham.name, "has been alive for", Beckham.celeb_date_convert(), "days.")
print(Ronaldinho.name, "has been alive for", Ronaldinho.celeb_date_convert(), "days.")
print(Boniek.name, "has been alive for", Boniek.celeb_date_convert(), "days.")
