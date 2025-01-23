import imghdr
import cv2

# Membaca gambar dari file
image = cv2.imread("1.jpg")

# Menampilkan gambar ke layar
cv2.imshow("Gambar", imghdr)

# Menunggu hingga pengguna menekan tombol apa pun
cv2.waitKey(0)

# Menutup jendela tampilan
cv2.destroyAllWindows()
