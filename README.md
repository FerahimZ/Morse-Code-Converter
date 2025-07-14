# Morse Code Converter (Flask + Bootstrap)

A simple web application to convert between English text and Morse code, built with Python Flask and styled with modern Bootstrap.

---

## Features

- **Text to Morse:** Convert any English text into Morse code.
- **Morse to Text:** Decode Morse code back into English text.
- **Modern UI:** Clean, responsive interface using Bootstrap 5.
- **Web-based:** No installation required for users—just run and open in your browser.

---

## Requirements

- Python 3.7+
- Flask

## Optional (for development)
- Any modern web browser

---

## Installation

1. **Clone the repository or copy the code:**
    ```bash
    git clone https://github.com/yourusername/morse-code-flask.git
    cd morse-code-flask
    ```

2. **Install dependencies:**
    ```bash
    pip install flask
    ```

---

## Usage

1. **Run the Flask app:**
    ```bash
    python app.py
    ```
    (Replace `app.py` with your filename if different.)

2. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Use the interface to:**
    - Enter text and convert to Morse code.
    - Enter Morse code (use spaces between letters) and convert to text.

---

## Example

- **Text to Morse:**  
  Input: `HELLO`  
  Output: `.... . .-.. .-.. ---`

- **Morse to Text:**  
  Input: `.... . .-.. .-.. ---`  
  Output: `HELLO`

---

## Customization

- To change the style, edit the Bootstrap classes in the HTML template.
- To add more symbols, update the `MORSE_CODE_DICT` in the Python code.

---

## License

MIT License

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- Morse code reference: [Wikipedia](https://en.wikipedia.org/wiki/Morse_code)