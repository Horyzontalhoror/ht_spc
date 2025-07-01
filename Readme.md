<h1>Installasi</h1>

<p>Butuhkan venv Python? Cukup jalankan perintah berikut:</p>

<pre><code>python -m venv venv</code></pre>

<p>Setelah itu, aktifkan venv dengan perintah:</p>

<pre><code>venv\Scripts\activate</code></pre>

<p>Install semua kebutuhan dengan perintah:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>Kemudian, clone model IndoBERTweet-HateSpeech dengan perintah:</p>

<pre><code>git clone https://huggingface.co/Exqrch/IndoBERTweet-HateSpeech</code></pre>

<p>Jalankan program dengan perintah:</p>

<pre><code>app.py</code></pre>

<p>Atau, jalankan semua file <code>.bat</code></p>

<p>Untuk mematikan venv, jalankan perintah:</p>

<pre><code>venv\Scripts\deactivate</code></pre>

<p><strong>Penting!</strong> Folder <code>save_model</code> akan diisi dengan model yang telah di training. Folder <code>IndoBERTweet-HateSpeech</code> akan diisi dengan model IndoBERTweet-HateSpeech.</p>

<p>Untuk update model IndoBERTweet-HateSpeech, jalankan perintah:</p>

<pre><code>git pull</code></pre>
