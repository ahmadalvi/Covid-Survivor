"""
Ahmad Alvi
covid_project.py
2020-04-24
"""
#These are the libraries that I am importing
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#This line of code is an array of the COVID-19 cases in Ontario that are reported daily on the government website
covid_cases = np.array([1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 2, 3, 4, 3, 2, 0, 3, 5, 0, 4, 3, 1, 6, 17, 20, 24, 43, 31, 12, 25, 44, 60, 59, 48, 78, 85, 100, 170, 135, 151, 182, 380, 260, 426, 401, 462, 375, 408, 309, 379, 550, 483, 478, 411, 401, 421, 483, 494, 514, 564, 485, 568, 606, 551, 510, 634, 640, 476, 437, 424, 525, 347, 459, 421, 511, 434, 370, 387, 412, 399, 477, 346, 294, 308, 361, 329, 345, 341, 391, 340, 304, 427, 390, 413, 441, 412, 460, 404, 287, 292, 383, 344, 323, 326, 404, 446, 338, 356, 344, 455, 415, 243, 230, 251, 203, 182, 266, 197, 181, 184, 190, 173, 178, 206, 175, 161, 216, 163, 189, 111, 160, 178, 257, 157, 149, 153, 165, 121, 138, 154, 112, 118, 170, 116, 130, 129, 116, 111, 102, 111, 111, 166, 164, 135, 203, 165, 103, 195, 138, 137, 119, 111, 76, 89, 134, 124, 116, 88, 91, 86, 95, 88, 70, 79, 115, 33, 95, 78, 92, 106, 81, 99, 125, 102, 76, 131, 108, 115, 105, 100, 88, 118, 122, 148, 112, 114, 112, 133, 132, 148, 169, 158, 190, 185, 149, 170, 213, 232, 204, 313, 251, 315, 293, 401, 407, 365, 425, 478, 335, 409, 409, 435, 491, 700, 554, 625, 538, 732, 653, 566, 615, 548, 583, 797, 939, 809, 649, 807, 746, 721, 783, 712, 805, 658, 705, 821, 790, 841, 826, 978, 1042, 851, 827, 834, 934, 896, 1015, 977, 948, 1050, 987, 998, 1003, 1132, 1328, 1242, 1388, 1426, 1575, 1396, 1581, 1248, 1487, 1249, 1417, 1210, 1418, 1588, 1534, 1589, 1009, 1373, 1478, 1855, 1822, 1708, 1746, 1707, 1723, 1824, 1780, 1859, 1924, 1925, 1676, 1890, 1983, 1848, 1873, 1677, 1940, 2275, 2139, 2432, 2290, 2357, 2316, 2213, 2202, 2408, 2447, 2159, 2142, 2005, 1939, 2553, 2923, 3328, 2476, 3363, 2964, 3270, 3128, 3266, 3519, 4249, 3443, 3945, 3338, 2903, 2961, 3326, 2998, 3056, 3422, 2578, 1913, 2655, 2632, 2662, 2359, 2417, 1958, 1740, 1670, 2093, 1837, 2063, 1848, 1969, 745, 1172, 1563, 1670, 1388, 1489, 1265, 1022, 1072, 946, 1076, 1300])

#This line of code is an array of the number of COVID-19 deaths in Ontario that are reported daily on the government website
covid_deaths = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 3, 0, 2, 5, 2, 3, 0, 3, 12, 0, 4, 16, 14, 27, 25, 13, 21, 21, 26, 22, 31, 21, 17, 43, 51, 36, 55, 36, 39, 31, 38, 37, 54, 50, 48, 24, 57, 59, 45, 86, 39, 55, 40, 84, 61, 68, 48, 63, 59, 35, 35, 56, 40, 33, 27, 33, 23, 23, 15, 43, 31, 28, 27, 25, 29, 21, 32, 34, 41, 17, 19, 12, 17, 19, 45, 15, 34, 19, 24, 14, 11, 12, 11, 9, 12, 8, 11, 12, 3, 11, 31, 11, 3, 10, 12, 10, 3, 8, 6, 7, 8, 4, 4, 2, 5, 2, 0, 2, 9, 3, 7, 6, 3, 3, 1, 9, 5, 9, 2, 3, 1, 1, 2, 0, 3, 1, 4, 1, 4, 1, 3, 3, 2, 1, 0, 4, 0, 1, 0, 1, 2, 0, 0, 1, 0, 1, 1, 0, 0, 4, 1, 1, 3, 1, 0, 1, 2, 2, 1, 6, 0, 1, 1, 1, 0, 0, 1, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 4, 2, 3, 0, 1, 1, 2, 3, 3, 1, 1, 0, 2, 1, 4, 4, 3, 76, 41, 7, 5, 7, 1, 4, 5, 7, 1, 3, 9, 0, 5, 9, 10, 5, 4, 3, 9, 9, 9, 6, 7, 6, 4, 5, 10, 9, 9, 9, 7, 14, 16, 13, 14, 11, 13, 12, 15, 15, 18, 19, 20, 29, 10, 12, 32, 28, 8, 21, 14, 19, 14, 35, 21, 20, 29, 24, 8, 7, 35, 14, 25, 20, 15, 26, 10, 28, 35, 45, 17, 16, 23, 20, 43, 23, 40, 27, 25, 17, 21, 41, 49, 43, 38, 18, 37, 41, 19, 56, 51, 44, 25, 29, 51, 37, 89, 26, 40, 61, 29, 41, 74, 62, 100, 51, 69, 24, 46, 89, 46, 87, 52, 50, 43, 63, 49, 56, 58, 73, 43, 36, 14, 67, 88, 45, 45, 22, 33, 17, 41, 18, 18, 19])

#This line of code is an array of the day number. Day 1 is January 25th 2020, thte day the first COVID-19 case was recorded in Ontario
day_number = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 342, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386])
print(np.sum(covid_cases))
print(np.sum(covid_deaths))

fig, ax = plt.subplots()

ax.plot(day_number, covid_cases, color='blue')
ax.set_xlabel('Day Number')
ax.set_ylabel('Number of COVID-19 Cases', color='blue')
ax.tick_params('y', colors='blue')
ax.annotate("Jan 25, 2020 (first case)", xy=(day_number[0], 1), xytext=(day_number[0], 300), arrowprops={"arrowstyle":"->", "color":"gray"})

ax2 = ax.twinx()

ax2.plot(day_number, covid_deaths, color='red')
ax2.set_ylabel('Number of COVID-19 Deaths', color='red')
ax2.tick_params('y', colors='red')

plt.title('COVID-19 in Ontario')
plt.show()
