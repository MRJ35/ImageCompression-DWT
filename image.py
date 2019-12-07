from PIL import Image, ImageDraw, ImageFont


def show_output(filename1,filename2):
    im1 = Image.open(filename1)
    im2 = Image.open(filename2)
    a,b = im1.size
    print(a,b)
    # im1 = im1.resize((a//2,b))
    # im2 = im2.resize((a//2,b))
    newI = Image.new('RGBA',(2*a+5,100+b+100),'white')
    newI.paste(im1,(0,100,a,b+100))
    newI.paste(im2,(a+5,100,2*a+5,b+100))
    #newI.show()

    draw = ImageDraw.Draw(newI)
    font = ImageFont.truetype('Lato-Black.ttf', 75) # write the path of the font which you want to select
    draw.text((a//2 - 150, b+102), "226 Kb", (0, 0, 0), font=font)
    draw.text(((a+a//2) - 150, b+102), "4.5 Mb", (0, 0, 0), font=font)
    draw.text((a//2+150,5),"Image Compression",(0,0,0),font=font)
    #newI.show()
    newI.save("abc.png")

#show_output("MERGED.png","NEE.png")