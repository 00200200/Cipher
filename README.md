# Cipher 

### Console Cipher Tool (ROT13 & ROT47)

Command-line application that provides encryption and decryption 
functionalities using ROT13 and ROT47 ciphers.
It allows file operations, and an in-memory buffer to manage
encrypted and decrypted data during runtime.

## **Table of Contents**  
1. [Features](#Features)  
2. [Installation](#installation)
3. [Usage](#usage)
4. [Testing](#testing) 
## **Features**  
- **Encryption and Decryption**:  
  - **ROT13**: Transforms alphabetic characters by shifting them 13 places.
  - **ROT47**: Transforms alphabetic characters by shifting them 47 places.
- **File Handling**:
  - Save encrypted/decrypted data to JSON files
  - Load encrypted/decrypted data from JSON files.
- **Buffer Management**: 
  - Storing encrypted/decrypted data during program execution.
- **Interactive Menu**:
  - Selection of encryption, decryption, load/write files and buffer management options.
- **Error Handlings**:
  - Handling Exepctions and Invalid data.  
## **Installation**
1. **Clone the repository**:  
```bash
git clone https://github.com/00200200/Cipher
cd Cipher
```
   
1. **Set up a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
1. **Install dependencies**: 
```bash
pip install -r requirements.txt
```
## **Usage**
**To start the application**
```bash
python main.py
```

## **Testing**
**Run all tests using pytest:**
```bash
pytest tests/
```