# Screenshot Organizer 
# Description
The Screenshot Organizer is a Python-based automation tool designed to analyze screenshots (or any images) added to a specific folder, extract text using Optical Character Recognition (OCR), and then rename the file based on the extracted text for easy categorization and retrieval. This tool aims to simplify managing a large number of screenshots by providing meaningful filenames at a glance.

Features
OCR Analysis: Extracts text from images using PyTesseract.
Automatic Renaming: Renames images based on the first few words of the extracted text to create easily identifiable filenames.
Folder Monitoring: Automatically triggers the script to analyze and rename new images added to the monitored folder.
Prerequisites
Python 3.x
OpenCV (cv2 library)
PyTesseract
PIL (Python Imaging Library)
Installation

# Step 1: Install Dependencies
Ensure Python 3 is installed on your system. Then, install the required Python libraries using pip:

*pip install opencv-python pytesseract Pillow*

# Step 2: Tesseract OCR
Install Tesseract OCR on your system. Instructions can be found at Tesseract's GitHub page.
You can also install Tesseract OCR on your system using Homebrew:

*brew install tesseract*

# Step 3: Download the Script
Download the ssAutomation.py script from this repository and place it in a convenient location on your system.
Modify the path of *screenshot_folder* in the script to the location of your screenshot folder.

# Future Enhancements

*Automated runs*: To make the script run whenever any changes to the folder are detected.

*GUI Application*: To make this tool more accessible to non-developers, a simple graphical interface will be developed for easy setup and monitoring.

*Smarter Analysis*: Future versions will include more advanced image analysis features for better filename generation.

# Contributing
Contributions to the Screenshot Organizer are welcome! Please read the CONTRIBUTING.md file for guidelines on how to submit issues, feature requests, and pull requests.

