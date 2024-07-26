# Spell Checker

## 📋 Overview
The **Spell Checker** is a Python-based application that provides an intuitive interface for real-time spell checking and correction. Developed using Tkinter, it features interactive elements that highlight misspelled words and offer correction suggestions, enhancing user experience and accessibility.

## 🚀 Features
- **User-Friendly Interface:** Built with Tkinter, providing a clean and simple GUI.
- **Real-Time Spell Checking:** Highlights errors instantly as users type.
- **Correction Suggestions:** Utilizes advanced algorithms to suggest corrections.
- **Interactive Feedback:** Click on highlighted words to view suggestions.

## 🛠️ Technologies Used
- **Python:** The core programming language.
- **Tkinter:** Standard GUI toolkit for Python.
- **Levenshtein Distance & Wagner-Fischer Algorithm:** Employed for calculating the similarity between words and generating suggestions.

## 📊 Algorithms
### Levenshtein Distance
A dynamic programming approach to measure the edit distance between two strings. It calculates the minimum number of single-character edits required to change one word into another.

### Wagner-Fischer Algorithm
An efficient dynamic programming algorithm to compute the edit distance between two strings, widely used for applications in spell checking, DNA sequence analysis, and more.
[code](https://github.com/Aniruddh-482/spell_checker/blob/main/wagner_fischer.py)

## 🎥 Demo
>Watch the [demo video](https://github.com/Aniruddh-482/spell_checker/blob/main/demo_video.mp4) to see the application in action.

https://github.com/user-attachments/assets/ffe61ef4-e624-498b-96da-ca2457876cc7


## 📦 Installation and Usage
1. **Clone the Repository:**
  ```bash
   git clone https://github.com/Aniruddh-482/spellChecker.git
   cd spellChecker
  ```
2. **Install Dependencies:**
The project primarily uses standard Python libraries. Ensure your Python environment is properly set up.
3. **Run the Application:**
  ```bash
   python spell_checker.py
  ```
    
## 📝 How It Works
The application reads a list of correctly spelled words from a text file (words.txt). It uses the Levenshtein Distance and Wagner-Fischer algorithms to suggest the most similar correct words for any misspelled input. The user interface, built with Tkinter, provides real-time feedback and interactive suggestions.

## 🔧 Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<br>
<hr>
Made with ❤️ using Python
