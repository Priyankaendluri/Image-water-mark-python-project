from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the original image
    image = Image.open(input_image_path).convert("RGBA")

    # Create a transparent layer for the watermark
    watermark_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark_layer)

    # Load a font or use default
    try:
        font = ImageFont.truetype("arial.ttf", 36)  # You can change font & size
    except:
        font = ImageFont.load_default()

    # Position: bottom right corner
    text_width, text_height = draw.textsize(watermark_text, font)
    position = (image.width - text_width - 20, image.height - text_height - 20)

    # Draw the watermark text with semi-transparency
    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

    # Combine original image with watermark layer
    watermarked_image = Image.alpha_composite(image, watermark_layer)

    # Save the result
    watermarked_image.convert("RGB").save(output_image_path, "JPEG")
    print(f"✅ Watermark added. Saved to {output_image_path}")

# Example usage
if __name__ == "__main__":
    add_watermark("input.jpg", "output_watermarked.jpg", "© YourBrand 2025")

