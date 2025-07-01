<h1>🧠 Deteksi Hate Speech (Gabungan Model)</h1>

<p>Aplikasi GUI berbasis Python yang menggunakan <strong>dua model (Ensemble)</strong>: model hasil fine-tuning dan IndoBERTweet-HateSpeech untuk mendeteksi kalimat yang mengandung ujaran kebencian.</p>

<h2>📦 Instalasi</h2>

<p>Butuhkan venv Python? Jalankan perintah berikut:</p>
<pre><code>python -m venv venv</code></pre>

<p>Setelah itu, aktifkan venv dengan perintah:</p>
<pre><code>venv\Scripts\activate</code></pre>

<p>Install semua dependensi dengan perintah:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>📥 Download Model IndoBERTweet</h2>

<p>Clone model dari Hugging Face ke folder lokal dengan perintah:</p>
<pre><code>git clone https://huggingface.co/Exqrch/IndoBERTweet-HateSpeech</code></pre>

<h2>▶️ Menjalankan Aplikasi</h2>

<p>Jalankan program GUI dengan perintah:</p>
<pre><code>python app.py</code></pre>

<p>Atau jalankan semua otomatis menggunakan file batch:</p>
<pre><code>run_app.bat</code></pre>

<h2>🛑 Nonaktifkan venv</h2>

<p>Untuk mematikan virtual environment:</p>
<pre><code>venv\Scripts\deactivate</code></pre>

<h2>📁 Struktur Folder</h2>

<ul>
  <li><code>venv/</code> – virtual environment</li>
  <li><code>save_model/</code> – model hasil fine-tuning</li>
  <li><code>IndoBERTweet-HateSpeech/</code> – model IndoBERTweet dari Hugging Face</li>
  <li><code>app.py</code> – aplikasi GUI utama</li>
</ul>

<h2>🔄 Update Proyek</h2>

<p>Untuk memperbarui proyek dari GitHub, jalankan:</p>
<pre><code>git pull</code></pre>

<h2>📌 Catatan Penting</h2>

<ul>
  <li><strong>save_model/</strong> akan berisi model hasil pelatihan kamu sendiri.</li>
  <li><strong>IndoBERTweet-HateSpeech/</strong> berisi model pre-trained dari Hugging Face.</li>
  <li>Aplikasi bisa berjalan offline setelah semua model dan tokenizer berhasil diunduh.</li>
</ul>
