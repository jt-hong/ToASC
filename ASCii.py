from PIL import Image

Handle = Image.open('NiceOne.jpg')
Handle = Handle.resize((80,80),Image.NEAREST)
Handle = Handle.transpose(Image.FLIP_LEFT_RIGHT)
Handle = Handle.rotate(90)
Text = ""

def CoverChar(R,G,B,gray = 256):
    AsciiC = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    #AsciiC = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
    Gray = int(0.2126 * R + 0.7152 * G + 0.0722 * B)
    ASCPercent = Gray/255
    Length = len(AsciiC)
    Unit = (257)/Length
    return AsciiC[int(Gray/Unit)]

for Width in range(80):
    for Heigh in range(80):
        Text+=CoverChar(*Handle.getpixel((Width,Heigh)))
        Text+=' '
    Text+='\n'

print(Text)
# with open("output.txt",'w') as f: #文件输出
#     f.write(txt)