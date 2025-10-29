from PIL import Image
from colorthief import ColorThief

def detect_mood(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    avg_brightness = sum(sum(pix) / 3 for pix in pixels) / len(pixels)

    thief = ColorThief(image_path)
    r, g, b = thief.get_color(quality=1)

    if avg_brightness > 170 and r > 180:
        return "energetic"
    elif b > 150:
        return "calm"
    elif avg_brightness < 80:
        return "sad"
    else:
        return "neutral"

#print(detect_mood("./static/uploads/j.jpg"))
