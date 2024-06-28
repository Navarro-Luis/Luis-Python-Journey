from PIL import Image, ImageFilter

img = Image.open('./pokedex_pics/pikachu.jpg') #./ means current directory. could be something like ./pokedex(next fokder)/pikachu.jpg

filtered_img = img.convert('L')

crooked = filtered_img.rotate(90)

crooked.save('crooked2.png','png')

# filtered_img.show()

