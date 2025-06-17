from PIL import Image, ImageDraw, ImageFont
import os , glob

# pip install pillow 
# exif data (exchangeable image file fomrat) standart for saving metadata 
directory = r"C:\Users\sven-\Desktop\coding_projects\photo_stuff\photo"

my_files = glob.glob(os.path.join(directory,"*.JPG")) # list of all jpg files

for index,file_path in enumerate(my_files): 
    new_name = f"new_photo_{str(index + 1).zfill(2)}.JPG"
    new_file_path = os.path.join(directory, new_name)
    os.rename(file_path, new_file_path)
    with Image.open(new_file_path) as image:
        img = Image.open(new_file_path) 
        exif = img.getexif()
        if 274 in exif: # 274 for orientation 
            del exif[274] # deletes the orientation
            img.save(new_file_path)
        img = Image.open(new_file_path)
        x_width, y_width = image.size
        place_y = y_width - 100
        place_x = x_width // 2
        
         
        
        
        I1 = ImageDraw.Draw(img) # call method to add 2d to pic
        font = ImageFont.truetype("arial.ttf",65)
        I1.text((place_x,place_y),"Hello Test 1283213", font=font, fill=(255, 0, 0))
        img.save(f"edited_photo_{str(index + 1).zfill(2)}.JPG")

        print(new_file_path)
        print(x_width)
        print(y_width)
        
        

