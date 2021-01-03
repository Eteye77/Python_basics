#Dictionaries allow you to store information in key value pairs
# the words are keys
# for dictionaries you use curly brackets
#[] can be replaced with .get
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Luv", "Not a valid key"))