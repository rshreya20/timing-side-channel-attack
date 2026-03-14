import matplotlib.pyplot as plt

characters = ["a","b","c","d","e","f","g","h","i","j"]
times = [0.02,0.03,0.05,0.02,0.08,0.01,0.03,0.02,0.01,0.02]

plt.bar(characters, times)
plt.xlabel("Characters Tested")
plt.ylabel("Response Time")
plt.title("Timing Side Channel Attack")
plt.show()