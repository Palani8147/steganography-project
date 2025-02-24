# Secure Data Hiding in Image Using Steganography

## Project Overview

This is a modern steganography application that allows users to hide secret messages within images using a graphical user interface (GUI). The tool uses OpenCV for image processing and Tkinter for the GUI interface.

## Features

- User-friendly GUI interface
- Image preview functionality
- Secure message encoding with password protection
- Message decoding with password verification
- Support for saving encoded images
- Error handling for invalid inputs

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- NumPy
- Pillow (PIL)
- Tkinter (usually comes with Python)

## Installation

1. Clone the repository:
   git clone [repository-url]
   cd steganography-project

2. Install required packages:
   pip install opencv-python numpy pillow

## Usage

1. Run the application:

2. Using the GUI:

- Click "Select Image" to choose an image
- Enter your secret message in the text box
- Enter a password
- Click "Encode" to hide the message
- Use "Decode" with the correct password to retrieve the message
- Click "Save Encoded Image" to save the result

## Security Notes

- The current implementation uses a basic pixel modification technique
- For production use, consider adding:
  - Stronger encryption
  - Better message length handling
  - Image format validation

## Limitations

- Message length is limited by image dimensions
- Supports JPG and PNG files only
- Basic steganography that might be detectable by advanced analysis

## Future Improvements

- Add encryption layer (e.g., AES)
- Implement capacity checking
- Support more image formats
- Add compression for larger messages

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with your changes

## License

This project is licensed under the MIT License.
