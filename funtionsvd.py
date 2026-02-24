from matplotlib.image import imread
import matplotlib.pyplot as plot
import numpy as np

# function to set the global value 'v' based on user input
def value(scale_choice):
    global v
    v = scale_choice

# function to compress an image using singular value decomposition (SVD)
def compress_image(image):
    # set default size for the figure
    plot.rcParams['figure.figsize'] = [19.2, 10.08]

    # inner function to handle grayscale image compression
    def grayscale():
        # read the image from the provided path
        x = imread(image)
        # convert the image to grayscale by averaging the RGB channels
        grayx = np.mean(x, -1)
        # display the grayscale image
        pic = plot.imshow(grayx)
        pic.set_cmap('gray')
        plot.title('Gray-scaled image')
        plot.axis('off')
        plot.show()
        
        # perform singular value decomposition on the grayscale image
        U, Σ, VT = np.linalg.svd(grayx, full_matrices=False)
        Σ = np.diag(Σ)  # convert singular values to a diagonal matrix
        z = 0
        # loop through specified ranks and approximate the grayscale image
        for n in (5, 20, 100, 200, 500, 750, 1000):
            grayxapprox = U[:, :n] @ Σ[0:n, :n] @ VT[:n, :]
            plot.figure(z + 1)
            z += 1
            # display the approximated image
            pic = plot.imshow(grayxapprox)
            pic.set_cmap('gray')
            plot.axis('off')
            plot.title('rank = ' + str(n))
            plot.show()
        # plot the cumulative percentage of variance explained by singular values
        plot.figure(2)
        plot.plot(np.cumsum(np.diag(Σ)) / np.sum(np.diag(Σ)))
        plot.title('Rank - Approximation Percentage relation')
        plot.show()
    
    # inner function to handle RGB image compression
    def rgb():
        # read the image from the provided path
        x = imread(image)
        # display the original image
        plot.imshow(x)
        plot.title('Original Image')
        plot.axis('off')
        plot.show()

        # perform SVD on each color channel (red, green, blue)
        red_U, red_Σ, red_VT = np.linalg.svd(x[:, :, 0], full_matrices=False)
        green_U, green_Σ, green_VT = np.linalg.svd(x[:, :, 1], full_matrices=False)
        blue_U, blue_Σ, blue_VT = np.linalg.svd(x[:, :, 2], full_matrices=False)

        # convert singular values to diagonal matrices for each channel
        red_Σ = np.diag(red_Σ)
        green_Σ = np.diag(green_Σ)
        blue_Σ = np.diag(blue_Σ)
        z = 0

        # loop through specified ranks and approximate the RGB image
        for n in (5, 20, 100, 200, 500, 750, 1000):
            # reconstruct approximated images for each color channel
            redapprox = red_U[:, :n] @ red_Σ[0:n, :n] @ red_VT[:n, :]
            greenapprox = green_U[:, :n] @ green_Σ[0:n, :n] @ green_VT[:n, :]
            blueapprox = blue_U[:, :n] @ blue_Σ[0:n, :n] @ blue_VT[:n, :]
            # combine the three channels into a single RGB image
            final = np.stack([redapprox, greenapprox, blueapprox], axis=-1)
            final = np.clip(final, 0, 255)  # ensure values are within valid range
            plot.figure(z + 1)
            z += 1
            # display the approximated RGB image
            plot.imshow(final.astype(np.uint8))
            plot.axis('off')
            plot.title('rank = ' + str(n))
            # save the image to a file
            plot.savefig(f'plot_rank_{n}.jpg', format='jpg')
            plot.show()

    # call the appropriate function based on the value of 'v'
    if v == 1:
        grayscale()
    elif v == 2:
        rgb()
    else:
        # print an error message for invalid input
        print("Invalid input, please try again")
