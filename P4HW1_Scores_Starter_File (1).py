
# Ask for number of scores user want to enter

score_num = int(input("How many scores do you want to enter? "))

print()
#create empty list




print()


#find lowest score




#drop lowest score from new list



# calculate average



# determine letter grade for average

if avg >= 90:

    grade = "A"
elif avg >= 80:

    grade = "B"

elif avg >= 70:

    grade = "C"
elif avg >= 60:

    grade = "D"
else:

    grade = "F"

# display results

print("\n--------------Results-----------")
print("Lowest Score  : {}".format(lowest))
print("Modified List : {}".format(scores_modified))
print("Scores Average: {:.2f}".format(avg))
print("Grade         : {}".format(grade))
print("----------------------------------")







