import matplotlib.pyplot as plt

x = []
with open('C:/Users/Саня/Python_Algoritms_Chirkin_Autumn/seminars/seminar 25.09/data_x.txt', encoding='utf-8') as f:
    for line in f:
        n = line.strip()
        x.append(int(n))
y = []
with open('C:/Users/Саня/Python_Algoritms_Chirkin_Autumn/seminars/seminar 25.09/data_y.txt', encoding='utf-8') as f:
    for line in f:
        n = line.strip()
        y.append(int(n))
plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y, 'b^--', label='3x')
