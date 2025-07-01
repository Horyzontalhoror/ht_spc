import tkinter as tk
from tkinter import messagebox
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model dan tokenizer dari folder lokal
model_path = "save_model"  # Ganti jika nama folder berbeda
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

# Mapping label ke nama kelas
label_mapping = {
    0: "✅ Tidak Mengandung Hate Speech",
    1: "❌ Mengandung Hate Speech"
}

# Fungsi prediksi
def prediksi_teks():
    teks = text_input.get("1.0", tk.END).strip()
    if not teks:
        messagebox.showwarning("Kosong", "Masukkan teks terlebih dahulu.")
        return

    inputs = tokenizer(teks, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).item()

    result_label.config(text=f"Hasil: {label_mapping[pred]}")

# Fungsi reset
def reset_input():
    text_input.delete("1.0", tk.END)
    result_label.config(text="")

# GUI Tkinter
root = tk.Tk()
root.title("Klasifikasi Hate Speech")
root.geometry("520x350")
root.resizable(False, False)

# Judul
tk.Label(root, text="Masukkan Kalimat:", font=("Helvetica", 12)).pack(pady=10)

# Input teks
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

# Tombol prediksi & reset
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Prediksi", command=prediksi_teks, font=("Helvetica", 10), bg="lightgreen").pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Reset", command=reset_input, font=("Helvetica", 10), bg="lightcoral").pack(side=tk.LEFT, padx=10)

# Label hasil prediksi
result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
