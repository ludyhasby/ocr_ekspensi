# ocr_ekspensi
pada repositori ini disediakan beberapa file, script yang diperlukan untuk proses OCR pada Ekspensi dan juga demonstrasi nya
- "requirements.txt" berisi library apa saja yang diperlukan pada proses running model.
  Jika package masih kurang, cobalah untuk menambahkan "pip install pillow"
- "ekspensi_ocr.py" adalah script yang digunakan untuk membangun dashboard uji coba yang dapat di lihat https://ocrekspensi.streamlit.app/
  tips : coba lakukan demo nya untuk mendapat sense processing yang dilakukan
- "ocr_default.py" adalah script baku yang digunakan untuk backend dasar pemrosesan gambar ke string, men-genarate teks seperti user lakukan, process ke NLP, dan simpan ke Cloud
  coba jalankan sekali pada lokal dan ikuti hint yang diberikan pada script. Hapus script yang tidak diperlukan. 
-  "geprek.jpeg" adalah gambar yang digunakan untuk demo "ocr_default.py".
