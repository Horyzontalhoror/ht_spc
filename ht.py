import tkinter as tk
from tkinter import messagebox
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ========== MODEL A: IndoBERTweet ==========
model_path_A = "IndoBERTweet-HateSpeech"
tokenizer_A = AutoTokenizer.from_pretrained("indolem/indobertweet-base-uncased")
model_A = AutoModelForSequenceClassification.from_pretrained(model_path_A)
model_A.eval()

# ========== MODEL B: Fine-tuned Model ==========
model_path_B = "save_model"
tokenizer_B = AutoTokenizer.from_pretrained(model_path_B)
model_B = AutoModelForSequenceClassification.from_pretrained(model_path_B)
model_B.eval()

# ========== LABEL MAPPING ==========
label_mapping = {
    0: "✅ Tidak Mengandung Hate Speech",
    1: "❌ Mengandung Hate Speech"
}

# ========== FUNGSI PREDIKSI ==========
def prediksi_teks():
    teks = text_input.get("1.0", tk.END).strip()
    if not teks:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu.")
        return

    try:
        # Tokenisasi dan prediksi
        inputs_A = tokenizer_A(teks, return_tensors="pt", truncation=True, padding=True, max_length=512)
        inputs_B = tokenizer_B(teks, return_tensors="pt", truncation=True, padding=True, max_length=512)

        with torch.no_grad():
            probs_A = torch.nn.functional.softmax(model_A(**inputs_A).logits, dim=1)
            probs_B = torch.nn.functional.softmax(model_B(**inputs_B).logits, dim=1)

        # Ensemble (soft voting)
        probs_avg = (probs_A + probs_B) / 2
        final_pred = torch.argmax(probs_avg, dim=1).item()

        # Tampilkan hasil ke UI
        result_label.config(text=f"Hasil: {label_mapping[final_pred]}")
        status_label.config(text="✓ Prediksi dihitung dari dua model")

        # Debug log ke terminal
        print("=== Probabilitas Model A (IndoBERTweet) ===", probs_A)
        print("=== Probabilitas Model B (Fine-tuned) ===", probs_B)
        print("=== Probabilitas Gabungan (Rata-rata) ===", probs_avg)
        print("Prediksi akhir:", final_pred, "-", label_mapping[final_pred])

    except Exception as e:
        messagebox.showerror("Error", f"Gagal memproses input:\n{str(e)}")
        status_label.config(text="❌ Terjadi kesalahan saat prediksi")

# ========== FUNGSI RESET ==========
def reset_input():
    text_input.delete("1.0", tk.END)
    result_label.config(text="")
    status_label.config(text="")

# ========== UI SETUP ==========
root = tk.Tk()
root.title("Deteksi Hate Speech (Gabungan Model)")
root.geometry("550x360")
root.resizable(False, False)

tk.Label(root, text="Masukkan Kalimat:", font=("Helvetica", 12)).pack(pady=10)

text_input = tk.Text(root, height=5, width=65)
text_input.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Prediksi", command=prediksi_teks, font=("Helvetica", 10), bg="lightgreen").pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Reset", command=reset_input, font=("Helvetica", 10), bg="lightcoral").pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 13, "bold"))
result_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 9), fg="gray")
status_label.pack()

tk.Label(root, text="Model A: IndoBERTweet | Model B: Fine-tuned", font=("Helvetica", 9), fg="gray").pack(side=tk.BOTTOM, pady=5)

# ========== JALANKAN UI ==========
root.mainloop()
