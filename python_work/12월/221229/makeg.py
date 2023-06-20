from faker import Faker
import matplotlib.pyplot as plt

fak = Faker("ko-KR")

name_age = []
for x in range(10):
    name_age.append([fak.name(),fak.pyint(min_value=10,max_value=60)])

print(name_age)

# plt.bar