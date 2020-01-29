# In python, every data type can be coerced into a string representation
age = 24
print("My age is " + str(age) + " years")  # This is tedious
# Python 3 provides an easier method as follows:
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} "
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print(
    "Jan: {2}, Feb: {0}, Mar: {1}, Apr: {2}, May: {1}, Jun: {2}, "
    "July: {1}, Aug: {2}, Sep:{1}, Oct: {2}, Nov: {1}, Dec:{2} "
    .format(28, 30, 31))
print()
# Above using triple quotes
print("""Jan: {2}
 Feb: {0}
 Mar: {1}
 Apr: {2}
 May: {1}
 Jun: {2}, 
 July: {1}
 Aug: {2}
 Sep:{1}
 Oct: {2}
 Nov: {1}
 Dec:{2} """.format(28, 30, 31))
