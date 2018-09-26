# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
adjective1 = raw_input("")
famousPerson1 = raw_input("")
adjective2 = raw_input("")
noun1 = raw_input("")
verb1= raw_input("")
adjective3 = raw_input("")
adjective4 = raw_input("")
noun2= raw_input("")
noun3= raw_input("")
verb2= raw_input("")
adjective6 = raw_input("")
noun4 = raw_input("")
bodyPart= raw_input("")
adjective5 = raw_input("")
verb2 = raw_input("Enter one more verb:")
famousPerson2 = raw_input("A famous person you sort of like, but not you're favorite:")
youDecide = raw_input("Fill in the bank for the storys ending: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "There was once was a" + adjective1 + "criminal named," + famousPerson1 + "who pleaded insaity after serving a " + adjective2 + \
"sentence to" + noun1 "for" + verb1 + "." \
"They thought they had escaped" + adjective3 \
"larbor and serving the rest of their sentence in a" + adjective4 + noun2 + "."\
"However, they were moved to" + noun3 "where they had to" + verb2 + adjective6 + noun4 + "."\
"Upon their arrival," + famousPerson2 + "remove their" + bodyPart + " and devour it right in front of them."\
"In" + adjective5 + verb2  + famousPerson1 + youDecide"." # I got lazy ;)
# finally we print the story
print (story)