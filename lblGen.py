from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageOps

font = ImageFont.truetype("./Calibri.ttf", 32)
labels = []
fileName = 'labelsList.txt'


with open(fileName, 'r') as f:
    labels = [line.rstrip() for line in f]
    
print(labels,len(labels))

for text in labels:
    lblFileName = text + ".png"
    # get text size
    txtSize = font.getsize(text)
    # set button size + 10px margins
    rectSize = (txtSize[0]+20, txtSize[1]+20)

    # create image with correct size and black background
    rectImg = Image.new('RGBA', rectSize, "white")

    # put text on button with 10px margins
    rectDraw = ImageDraw.Draw(rectImg)
    rectDraw.text((10, 10), text, font=font, fill='black', align="center")   
    # save in new file
    rectImg.save(lblFileName)
    tmpImgHolder = Image.open(lblFileName)
    ImageOps.expand(tmpImgHolder, border = 150, fill=(0,0,0))
    
    
    

