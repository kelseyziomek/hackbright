print "Welcome to the survey!"
name = raw_input("What is your name:")
color = raw_input("What is your favorite color?")
hobby = raw_input("What is your favorite hobby?")
movie = raw_input("What is your favorite movie?")
book = raw_input("What is your favorite book?")
vacation = raw_input("What is your favorite destination for vacation?")
#print name+"'s favorite color is "+color+"."
#print name+"'s favorite hobby is "+hobby+"."
#print name+"'s favorite movie is "+movie+"."
#print name+"'s favorite book is "+book+"."
#print name+"'s favorite vacation spot is "+vacation+"."

def print_survey_results(name, color, hobby, movie):
    print name+"'s favorite color is "+color+"."
    print name+"'s favorite hobby is "+hobby+"."
    print name+"'s favorite movie is "+movie+"."
print_survey_results(name, color, hobby, movie)
