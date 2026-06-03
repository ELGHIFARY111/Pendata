import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
data = pd.DataFrame({
    "X": [2, 4, 5, 3, 3, 4, 5],
    "Y": [2, 3, 5, 4, 3, 5, 6]
})

# Variabel X dan Y
X = data[["X"]]
Y = data["Y"]

# Membuat model regresi linier
model = LinearRegression()
model.fit(X, Y)

# Mengambil nilai intercept dan koefisien
intercept = model.intercept_
koefisien = model.coef_[0]

print("Intercept:", intercept)
print("Koefisien:", koefisien)
print(f"Persamaan garis: y = {koefisien:.5f}x + {intercept:.5f}")

# Mencari nilai prediksi Y
data["Y_prediksi"] = model.predict(X)

# Menghitung residual error
data["Residual_Error"] = data["Y"] - data["Y_prediksi"]

# Menghitung residual kuadrat
data["Residual_Kuadrat"] = data["Residual_Error"] ** 2

# Menghitung Mean Squared Error
mse = data["Residual_Kuadrat"].mean()

print("\nHasil prediksi dan residual error:")
print(data)

print("\nTotal residual error:", data["Residual_Error"].sum())
print("Mean Squared Error:", mse)

# Visualisasi dengan Matplotlib

plt.scatter(data["X"], data["Y"], label="Data Asli")
plt.plot(data["X"], data["Y_prediksi"], label="Garis Regresi")

plt.title("Regresi Linier")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.show()