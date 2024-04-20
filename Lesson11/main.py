from recogniser import Recognizer
imgPath = 'imgs/cat.jpg'
glassesPath = 'imgs/glasses.png'
newPath = 'imgs/newcat.png'
wndwName = 'Cat'
filePath = 'xmls/haarcascade_frontalcatface_extended.xml'
pict = Recognizer(imgPath)
pict.MultiScale = pict.GetCoordinates(filePath, pict.Image)
pict.HighLight(pict.Image)
pict.Image = pict.PasteImg(glassesPath, imgPath, newPath)
pict.ShowImg(wndwName)