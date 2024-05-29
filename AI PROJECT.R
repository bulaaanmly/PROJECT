# Memuat library yang diperlukan
library(readxl)

# Membaca data dari file Excel
COBA_AI <- read_excel("Downloads/COBA AI.xlsx")

# Menampilkan data untuk memastikan data sudah benar
View(COBA_AI)

# Membuat model regresi linear sederhana
ModelRegSederhana <- lm(Pupuk_Kandang ~ Jumlah_Pohon, data = COBA_AI)

# Menampilkan ringkasan model
summary(ModelRegSederhana)

# Menghitung residual
residuals <- resid(ModelRegSederhana)

# Melakukan uji normalitas menggunakan uji Shapiro-Wilk
shapiro.test(residuals)

# Membuat plot Q-Q untuk memvisualisasikan residual
qqnorm(residuals)
qqline(residuals)

#Melakukan Uji Multikolineritas
#Anda tidak perlu dan tidak bisa menghitung VIF karena hanya ada satu variabel independen. Multikolinearitas adalah konsep yang relevan hanya dalam model dengan beberapa variabel independen.

# Melakukan uji Durbin-Watson untuk autokorelasi
durbinWatsonTest(ModelRegSederhana)

# Melakukan uji Breusch-Pagan untuk heteroskedastisitas
library(lmtest)
bptest(ModelRegSederhana)

#Melakukan uji linearitas 
library(car)
avPlots(ModelRegSederhana)

#Melakukan uji simultan (uji f) Uji Parsial (Uji T) 
anova(ModelRegSederhana)
summary(ModelRegSederhana)

# Menghitung koefisien korelasi antara variabel independen dan dependen
cor.test
cor(COBA_AI[,c("Pupuk_Kandang","Jumlah_Pohon")])
