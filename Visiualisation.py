import matplotlib.pyplot as plt
import pandas as pd

# read result
result = pd.read_csv(r"C:\Users\khale\OneDrive\Desktop\SW exercise\transformed dataset\transformed.csv",usecols=["Year","Count","count"])
# draw chart
plt.title("Relationsip between liverCancer incidance and tobacco smoker in alabama")
plt.plot(result["Year"],result["Count"], label = "Liver Cancer Incidance")
plt.plot(result["Year"],result["count"], label = "Tobacco smoker")
plt.legend()
plt.show()