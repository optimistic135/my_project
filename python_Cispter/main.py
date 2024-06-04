import tkinter as tk

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        char_up = char.upper()
        if char_up.isalpha():
            ascii_offset = ord(char_up) - ord('A')
            new_ascii_offset = (ascii_offset + shift) % 26
            new_char = chr(new_ascii_offset + ord('A'))
            if char.islower():
                new_char = new_char.lower()
        else:
            new_char = char
        result += new_char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def encrypt():
    shift = int(shift_entry.get())
    text = input_text.get("1.0", tk.END)
    encrypted_text = caesar_encrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)


def decrypt():
    shift = int(shift_entry.get())
    text = input_text.get("1.0", tk.END)
    decrypted_text = caesar_decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

root = tk.Tk()
root.title("凯撒密码")

tk.Label(root, text="输入:").grid(row=0, column=0)
input_text = tk.Text(root, height=10, width=30)
input_text.grid(row=0, column=1)

tk.Label(root, text="密钥:").grid(row=1, column=0)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1)

encrypt_button = tk.Button(root, text="加密", command=encrypt)
encrypt_button.grid(row=2, column=1, columnspan=2)

decrypt_button = tk.Button(root, text="解密", command=decrypt)
decrypt_button.grid(row=3, column=1, columnspan=3)

tk.Label(root, text="输出:").grid(row=4, column=0)
output_text = tk.Text(root, height=10, width=30)
output_text.grid(row=4, column=1)

root.mainloop()