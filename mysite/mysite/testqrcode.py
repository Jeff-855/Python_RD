import qrcode

img = qrcode.make('https://jefftestapp.herokuapp.com/index1/')
img.save("qrcode.png")
img.show()