import qrcode

def qrcode_generator(link):
    #img = qrcode.make('https://github.com/rahul1990bhatia/Algorithms')
    img = qrcode.make(link)
    img.save('qrcode.jpg')