import random

# =============================================================================
# 1: generate a floating point number
print(random.random())          # generates a random float in range [0.0, 1.0)
print(random.uniform(5, 7))     # generates a random float in range [5.0, 7.0)


# 2: generate random integers
print(random.randrange(10))         # generates a random Integer: "0 <= x < 9"
print(random.randrange(5, 10))      # Integer from 5 to 9 inclusive
print(random.randrange(5, 10, 2))   # random integer in [5, 10) with step=2
print(random.randint(5, 10))        # Integer from 5 to 9 inclusive

# =============================================================================
# 2: generate random integers -----  ساخت عدد صحیح رندم

# Integers in: 5 <= Number <= 10 ------------------ randrange -----------------
# generates a random Integer: "0 <= NUMBER < 10"
print(random.randrange(10))

# Integer from 5 to 9 inclusive
print(random.randrange(5, 10))

# random integer in range [5, 10) with step = 2
# در این تابع، علاوه بر نقطه شروع و پایان،
# گام حرکت نیز میتوان مشخص کرد
print(random.randrange(5, 10, 2))

# Integers in: 5 <= Number <= 10 ------------------ randint -------------------
print(random.randint(5, 10))

# Return a random integer Number such that a <= Number <= b.
# A randint(a,b) works only for integers.
# The randint(a,b) function accepts two parameters,
# and both are required. The resultant random number
# is greater than or equal to a and less than or equal to b.

# =============================================================================
# 3: pick a random element from the sequence
# انتخاب تصادفی از داخل یک مجموعه

my_list = ['Phika', 'Py', 'js', 'Java']

# Random element --------------------------------------------------------------
print(random.choice(my_list))

# Random k elements from seq with replacement ---------------------------------
print(random.choices(my_list, k=2))

# 4: rearranges the items of a list in (in a random order) --------------------
# بر زدن یا چینش تصادفی اعضا
random.shuffle(my_list)
print(my_list)

# 5: sample, randomly choose 2 item from my_list ------------------------------
samples = random.sample(my_list, 2)
print(samples)

