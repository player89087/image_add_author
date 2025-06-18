from PIL import Image, ImageDraw, ImageFont, ExifTags
import os , glob

# pip install pillow 
# exif data (exchangeable image file fomrat) standart for saving metadata 
directory = r"C:\Users\sven-\Desktop\coding_projects\photo_stuff\photo"
directory_no_exif = r"C:\Users\sven-\Desktop\coding_projects\photo_stuff\photo\no_exif"

my_files = glob.glob(os.path.join(directory,"*.JPG")) # list of all jpg files

for index,file_path in enumerate(my_files): 
    new_name = f"new_photo_{str(index + 1).zfill(2)}.JPG"
    new_file_path = os.path.join(directory, new_name)
    os.rename(file_path, new_file_path)
    with Image.open(new_file_path) as image:
        img = Image.open(new_file_path) 
    
    
       
        
        x_width, y_width = image.size
        place_y = (y_width // 100)
        place_x = (x_width // 2) - 50
        
        pixelRGB = img.getpixel((place_x, place_y))
        brightness = int(sum(pixelRGB)**(1/3))
        print(brightness)
        color = 0
        if brightness <= 6: 
            color = 255, 255, 255
        elif brightness >= 7:
            color = 0, 0, 0
        
        I1 = ImageDraw.Draw(img) # call method to add 2d to pic
        font = ImageFont.truetype("arial.ttf",65)
        I1.text((place_x,place_y),"© Sven Künne", font=font, fill=(color))
        img.save(f"edited_photo_{str(index + 1).zfill(2)}.JPG")

        print(x_width)
        print(y_width)
     
        

