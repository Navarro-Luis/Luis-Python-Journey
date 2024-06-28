from PIL import Image, ImageFilter

img = Image.open('./pokedex_pics/pikachu.jpg')

img.thumbnail((200,200))

img.save('thumbnail.jpg')

print(img.size)

