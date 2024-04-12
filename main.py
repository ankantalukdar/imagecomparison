from PIL import Image

def pixel_comparison(image1_path, image2_path):
    # Open images
    with Image.open(image1_path) as image1, Image.open(image2_path) as image2:
        # Convert images to RGB mode (in case they are not already in RGB)
        image1 = image1.convert('RGB')
        image2 = image2.convert('RGB')

        # Get pixel matrices
        pixels1 = list(image1.getdata())
        pixels2 = list(image2.getdata())

        # Calculate pixel-wise absolute differences
        differences = [(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]), abs(p1[2] - p2[2])) for p1, p2 in zip(pixels1, pixels2)]

        # Calculate average difference per pixel
        avg_difference = sum(sum(diff) for diff in differences) / (len(differences) * 3)

    return avg_difference


if __name__ == "__main__":
    image1_path = "image1.jpeg"
    image2_path = "image2.jpeg"
    similarity_threshold = 10  # Adjust threshold as needed

    difference_score = pixel_comparison(image1_path, image2_path)
    if difference_score <= similarity_threshold:
        print("Images are similar.")
    else:
        print("Images are different.")
