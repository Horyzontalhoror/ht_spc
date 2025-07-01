import tkinter as tk
from tkinter import messagebox
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# model lokal
model_path = "IndoBERTweet-HateSpeech"  # Ganti jika nama folder berbeda
tokenizer = AutoTokenizer.from_pretrained("indolem/indobertweet-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()


# Mapping label hasil prediksi
label_mapping = {
    0: "✅ Tidak Mengandung Hate Speech",
    1: "❌ Mengandung Hate Speech"
}

# Fungsi prediksi
def prediksi_teks():
    teks = text_input.get("1.0", tk.END).strip()
    if not teks:
        messagebox.showwarning("Peringatan", "Masukkan kalimat terlebih dahulu.")
        return

    inputs = tokenizer(teks, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()

    result_label.config(text=f"Hasil: {label_mapping[pred]}")

# Fungsi reset
def reset_input():
    text_input.delete("1.0", tk.END)
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Deteksi Hate Speech")
root.geometry("520x340")
root.resizable(False, False)

tk.Label(root, text="Masukkan Kalimat:", font=("Helvetica", 12)).pack(pady=10)

text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Prediksi", command=prediksi_teks, font=("Helvetica", 10), bg="lightgreen").pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Reset", command=reset_input, font=("Helvetica", 10), bg="lightcoral").pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()
