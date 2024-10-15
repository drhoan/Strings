# In Robert McCloskey’s book Make Way for Ducklings,
# the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
# The code below tries to output these names in order.
# Run the program and you will see that it’s not quite right because Ouack and Quack are misspelled.
# Can you fix it so that Ouack and Quack will be printed instead Oack and Qack?
# Expected output:
'''
Jack
Kack
Lack
Mack
Nack
Ouack
Pack
Quack
'''

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)