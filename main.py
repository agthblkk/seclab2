import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Функції для шифрування і дешифрування методом Тритеміуса
def Trithemius_encrypt(text, key, key_type, alphabet):
    """Шифрування методом Тритеміуса з логуванням."""
    result = ""
    n = len(alphabet)
    print(f"Encrypting: {text} with key {key} as {key_type}")
    if key_type == "2D-вектор":
        a, b = key
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                new_idx = (idx + a * i + b) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Shifted: {new_idx}, New Char: {new_char}")
            else:
                result += char
    elif key_type == "3D-вектор":
        a, b, c = key
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                new_idx = (idx + a * i**2 + b * i + c) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Shifted: {new_idx}, New Char: {new_char}")
            else:
                result += char
    elif key_type == "Гасло":
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                offset = alphabet.index(key[i % len(key)].upper())
                new_idx = (idx + offset) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Offset: {offset}, New Index: {new_idx}, New Char: {new_char}")
            else:
                result += char
    print(f"Encrypted Text: {result}")
    return result

def Trithemius_decrypt(text, key, key_type, alphabet):
    """Дешифрування методом Тритеміуса з логуванням."""
    result = ""
    n = len(alphabet)
    print(f"Decrypting: {text} with key {key} as {key_type}")
    if key_type == "2D-вектор":
        a, b = key
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                new_idx = (idx - (a * i + b)) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Shifted: {new_idx}, New Char: {new_char}")
            else:
                result += char
    elif key_type == "3D-вектор":
        a, b, c = key
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                new_idx = (idx - (a * i**2 + b * i + c)) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Shifted: {new_idx}, New Char: {new_char}")
            else:
                result += char
    elif key_type == "Гасло":
        for i, char in enumerate(text):
            if char.upper() in alphabet:
                idx = alphabet.index(char.upper())
                offset = alphabet.index(key[i % len(key)].upper())
                new_idx = (idx - offset) % n
                new_char = alphabet[new_idx]
                result += new_char if char.isupper() else new_char.lower()
                print(f"Char: {char}, Index: {idx}, Offset: {offset}, New Index: {new_idx}, New Char: {new_char}")
            else:
                result += char
    print(f"Decrypted Text: {result}")
    return result

# Функції для роботи з інтерфейсом
def validate_key(key, key_type):
    """Перевірка валідності ключа залежно від його типу."""
    if key_type == "2D-вектор":
        try:
            key = list(map(int, key.split(',')))
            if len(key) != 2:
                raise ValueError("Ключ повинен містити рівно 2 числа.")
            return key
        except ValueError:
            raise ValueError("Ключ має бути у форматі 'a,b', де a і b - цілі числа.")
    elif key_type == "3D-вектор":
        try:
            key = list(map(int, key.split(',')))
            if len(key) != 3:
                raise ValueError("Ключ повинен містити рівно 3 числа.")
            return key
        except ValueError:
            raise ValueError("Ключ має бути у форматі 'a,b,c', де a, b і c - цілі числа.")
    elif key_type == "Гасло":
        if not key.strip():
            raise ValueError("Гасло не може бути порожнім.")
        return key
    else:
        raise ValueError("Невідомий тип ключа.")

def get_selected_alphabet():
    """Отримує обраний алфавіт для шифрування/дешифрування."""
    selected_alphabet = alphabet_choice.get()
    if selected_alphabet == "Англійський":
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif selected_alphabet == "Український":
        return "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

def encrypt_text():
    try:
        key = validate_key(entry_key.get(), key_choice.get())
        text = text_area.get("1.0", tk.END).strip()
        alphabet = get_selected_alphabet()
        encrypted_text = Trithemius_encrypt(text, key, key_choice.get(), alphabet)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, encrypted_text)
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

def decrypt_text():
    try:
        key = validate_key(entry_key.get(), key_choice.get())
        text = text_area.get("1.0", tk.END).strip()
        alphabet = get_selected_alphabet()
        decrypted_text = Trithemius_decrypt(text, key, key_choice.get(), alphabet)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, decrypted_text)
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text_area.get("1.0", tk.END).strip())

# Графічний інтерфейс
root = tk.Tk()
root.title("Шифрування методом Тритеміуса")

# Вибір типу ключа
frame_key_type = tk.Frame(root)
frame_key_type.pack(pady=10)

tk.Label(frame_key_type, text="Тип ключа:", font=("Arial", 14)).pack(side=tk.LEFT)
key_choice = tk.StringVar(value="2D-вектор")
tk.OptionMenu(frame_key_type, key_choice, "2D-вектор", "3D-вектор", "Гасло").pack(side=tk.LEFT, padx=5)

# Вибір алфавіту
frame_alphabet = tk.Frame(root)
frame_alphabet.pack(pady=10)

tk.Label(frame_alphabet, text="Алфавіт:", font=("Arial", 14)).pack(side=tk.LEFT)
alphabet_choice = tk.StringVar(value="Український")
tk.OptionMenu(frame_alphabet, alphabet_choice, "Український", "Англійський").pack(side=tk.LEFT, padx=5)

# Введення ключа
frame_key = tk.Frame(root)
frame_key.pack(pady=10)

tk.Label(frame_key, text="Ключ:", font=("Arial", 14)).pack(side=tk.LEFT)
entry_key = tk.Entry(frame_key, width=30, font=("Arial", 14))
entry_key.pack(side=tk.LEFT, padx=5)

# Панель кнопок
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Шифрувати", command=encrypt_text, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Дешифрувати", command=decrypt_text, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Відкрити файл", command=open_file, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Зберегти файл", command=save_file, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)

# Текстова область
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 14))
text_area.pack(padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()
