from PIL import Image, ImageFont, ImageDraw
from random import randint
import os
import glob
import cv2

files = glob.glob('Caption_Frames/*')
for f in files:
    os.remove(f)

files = glob.glob('Flashy_Frames/*')
for f in files:
    os.remove(f)

with open("Script.txt") as f:
    Master_text=f.read().split("\n")


try:
    print("How many whole seconds would you like the text to loop for? 0 will finish at the end of the center script by default.")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 0")
    Value=0
length = Value # Length in seconds

try:
    print("What fps would you like?")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 60")
    Value=60
fps=Value
font_input = 'ArchivoBlack-Regular.ttf'
try:
    print("How many pixels would you like along the x axis?")
    print("Common display aspect ratios are:")
    print("1920 x 1080 (Default)")
    print("2560 x 1440")
    print("3840 x 2160")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1920")
    Value=1920
x_length=Value
try:
    print("How many pixels would you like along the y axis?")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1080")
    Value=1080
y_length=Value
try:
    print("What is the minimal number of subliminals you want on the screen at any time? Note, this includes the center if selected.")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1")
    Value=1
Min_num_subs=Value
try:
    print("What is the maximum number of subliminals you want on the screen at any time? Note, this includes the center if selected.")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1")
    Value=1
Max_num_subs=Value
try:
    print("What is the smallest possible font size you'd like to see?")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 20")
    Value=20
Min_font_size=Value
try:
    print("What is the largest possible font size you'd like to see? The center will always be this size.")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 40")
    Value=40
Max_font_size=Value
try:
    print("What is the minimum number of frames that a sublinal should be present for?")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1")
    Value=1
Min_frames=Value
try:
    print("What is the maximum number of frames that a sublinal should be present for?")
    Value=int(input())
except:
    print("Value was not accepted as an integer. Defaulting to 1")
    Value=1
Max_frames=Value
try:
    print("Should the subliminals be in order? (Note, the wait function in the central script only works properly if yes.)")
    Value=input().capitalize()[0]
    if Value=="Y":
        Value=True
    elif Value=="N":
        Value=False
    else:
        print("Did not provide Y/N. Defaulting to yes.")
        Value=True
except:
    print("Did not provide Y/N. Defaulting to yes.")
    Value=True
Text_In_Order=Value
try:
    print("Should a flashy counterpart be made as well? Will show as Flashy video.mp4")
    Value=input().capitalize()[0]
    if Value=="Y":
        Value=True
    elif Value=="N":
        Value=False
    else:
        print("Did not provide Y/N. Defaulting to no.")
        Value=False
except:
    print("Did not provide Y/N. Defaulting to no.")
    Value=False
Flashy=Value
Probability_Blank=0
Flash_max_length=20
try:
    print("Should there be a subliminal in the center?")
    Value=input().capitalize()[0]
    if Value=="Y":
        Value=True
    elif Value=="N":
        Value=False
    else:
        print("Did not provide Y/N. Defaulting to yes.")
        Value=True
except:
    print("Did not provide Y/N. Defaulting to yes.")
    Value=True
Center=Value


if Center:
    with open("Center Script.txt") as f:
        Center_text=f.read().split("\n")
else:
    Center_text=Master_text
    

for text in Center_text:
    print(text[:text.find("{")])
temp=[]

if Center:
    for i in range(len(Center_text)):
        repeat_num=0
        middle_text=Center_text[i]
        wait_time_start=middle_text.find("{wait:")
        if wait_time_start!=-1 and Center:
            wait_time_end=middle_text.find("}")
            repeat_num=round((float(middle_text[wait_time_start+6:wait_time_end]))*fps)
            middle_text=middle_text[:wait_time_start]
        temp.append(middle_text)
        for j in range(repeat_num):
            temp.append(middle_text)
            
Center_text=temp

def Subliminal_Generator(length=length,fps=fps,Min_num_subs=Min_num_subs,Max_num_subs=Max_num_subs,Min_font_size=Min_font_size,Max_font_size=Max_font_size,Min_frames=Min_frames,Max_frames=Max_frames,Text_In_Order=Text_In_Order,Flashy=Flashy,Probability_Blank=Probability_Blank,Flash_max_length=Flash_max_length,Center=Center):
    Frame=0
    SubFrame=0
    SubFrameMax=0
    Middle_Text_Index=0
    Flashy_Coords=[]
    Text_Index=0
    zl=False
    
    if length==0:
        zl=True
        length=99999999999999
    while Frame<length*fps:
        im = Image.new(mode="RGB", size=(x_length,y_length))
        draw = ImageDraw.Draw(im) 
        if SubFrameMax==0:
            SubFrameMax=randint(Min_frames,Max_frames)
        
        Sub_iterator_range=randint(Min_num_subs,Max_num_subs)
        if randint(1,100)<=Probability_Blank:
            Sub_iterator_range=0
        Coords=[]
        for i in range(Sub_iterator_range):
            if Text_In_Order:
                text=Master_text[Text_Index]
                Text_Index+=1
                if i==0 and Center:
                    Middle_Text_Index+=1
                if Middle_Text_Index>=len(Center_text) and zl:
                    break
                elif Middle_Text_Index>=len(Center_text):
                    Middle_Text_Index=0
                if Center:
                    middle_text=Center_text[Middle_Text_Index]
                else:
                    middle_text=text
                if Text_Index>=len(Master_text):
                    Text_Index=0
            
                
            else:
            
                text=Master_text[randint(0,len(Master_text)-1)]
            if i!=0:
                fontsize=randint(Min_font_size,Max_font_size)
            else:
                fontsize=Max_font_size
            font = ImageFont.truetype(font_input, fontsize) 
            x_length_text=font.getbbox(text)[2]
            y_length_text=font.getbbox(text)[3]
            x_loc=-1
            if i==0 and Center:
                x_loc=(x_length-x_length_text)/2
                y_loc=(y_length-y_length_text)/2
                Coords.append([x_loc,y_loc,x_length_text,y_length_text])
            
            else: #x_loc should always be positive, not sure why this is needed
                while x_loc<0:
                    x_loc=randint(0,(x_length-x_length_text))
                    y_loc=randint(0,(y_length-y_length_text))
                    Not_In_Another=False
                    for Coord in Coords:
                        x_range=range(x_loc,x_loc+x_length_text)
                        y_range=range(y_loc,y_loc+y_length_text)
                        for x in x_range:
                            for y in y_range:
                                if (x>Coord[0]+Coord[2] or x<Coord[0]) and (y>Coord[1]+Coord[3] or y<Coord[1]):
                                    pass
                                    #print(x,y,y_range)
                                elif not(x_loc==Coord[0] and y_loc==Coord[1]):
                                    #print(text)
                                    x_loc=-1
                                    break
                            if x_loc==-1:
                                break
                        if x_loc!=-1:
                            Coords.append([x_loc,y_loc,x_length_text,y_length_text])
                            break
            if i!=0 and Center:
                while SubFrame<SubFrameMax:
                    draw.text((x_loc,y_loc), text, font = font, align ="left")
                    SubFrame+=1
            elif not(Center):
                while SubFrame<SubFrameMax:
                    draw.text((x_loc,y_loc), text, font = font, align ="left")
                    SubFrame+=1
            else:
                while SubFrame<SubFrameMax:
                    #print(middle_text)
                    draw.text(((x_length-font.getbbox(middle_text)[2])/2,(y_length-font.getbbox(middle_text)[3])/2), middle_text, font = font, align ="left")
                    SubFrame+=1
            SubFrame=0
        if Middle_Text_Index>=len(Center_text) and zl:
            break
        if Middle_Text_Index>=len(Master_text) and length==round((len(Master_text)+1)/fps):
            break
        for i in range(SubFrameMax):
            if Flashy and i==0 and Sub_iterator_range!=0:
                Flashy_Coords.append(Frame)
                Flashy_Coords.append(Frame+SubFrameMax//2)
                Flashy_Coords.append(Frame+SubFrameMax)
            Frame+=1
            if Frame>=length*fps:
                break
            im.save(f"Caption_Frames/{Frame}.jpeg")
            
        im.close()
            
        SubFrameMax=0
        
    # Function to generate video
    def generate_video(path,fps):
        image_folder = path
        video_name = f'{path[:path.find("_")]} video.mp4'

        images = [f"{img}.jpeg" for img in range(1,len(os.listdir(image_folder))+1)]
        height, width, layers = [y_length,x_length,1]

        # Video writer to create .avi file
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        # Appending images to video
        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        # Release the video file
        video.release()
        cv2.destroyAllWindows()
        
        
    generate_video("Caption_Frames", fps)
    
    Flashy_Coords=list(set(Flashy_Coords))
    
    if Flashy:
        colour="black"
        wind_up=0
        for i in range(max(Flashy_Coords)):
            if i in Flashy_Coords:
                if colour=="black":
                    colour="white"
                else:
                    colour="black"
            if colour=="white":
                wind_up+=1
            if wind_up>=Flash_max_length or colour=="black":
                colour="black"
                wind_up=0
            im = Image.new(mode="RGB", size=(x_length,y_length),color=colour)
            im.save(f"Flashy_Frames/{i}.jpeg")
    
    generate_video("Flashy_Frames",fps)
    
    files = glob.glob('Caption_Frames/*')
    for f in files:
        os.remove(f)
    
    files = glob.glob('Flashy_Frames/*')
    for f in files:
        os.remove(f)
        
Subliminal_Generator()
print("Finished")