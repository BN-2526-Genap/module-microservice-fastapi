## Modul Microservice - FastAPI

Repository ini akan berisi **beberapa module** praktikum untuk mata kuliah Microservice berbasis **FastAPI**.

- Setiap module diletakkan dalam folder terpisah di root, misalnya:
  - `Module_1-Alembic_FastAPI_SQL_Lite`
  - `Module_2-...` (dan seterusnya, bisa ditambahkan nanti)
- Masing-masing module punya `README.MD` sendiri yang berisi materi & langkah praktikum.

---

### Daftar Module

- **Module 1 – Alembic, FastAPI, SQLModel, SQLite**
  - Folder: `Module_1-Alembic_FastAPI_SQL_Lite`
  - Topik:
    - Setup FastAPI
    - SQLModel + SQLite
    - Pydantic schema
    - Alembic migration
    - (opsional) Docker untuk FastAPI + SQLite
  - Dokumentasi lengkap: lihat `Module_1-Alembic_FastAPI_SQL_Lite/README.MD`

> Ke depan, jika ada module baru (Module 2, 3, dst), cukup buat folder baru dan tambahkan poin baru di bagian ini.

---

### Cara Menggunakan Repository Ini

1. **Clone repo**

   ```bash
   git clone <url-repo-anda>.git
   cd module-fast-api
   ```

2. **Masuk ke module yang ingin dipelajari**, contoh Module 1:

   ```bash
   cd Module_1-Alembic_FastAPI_SQL_Lite
   ```

3. Ikuti langkah-langkah yang sudah dijelaskan di `README.MD` di dalam module tersebut.

---

### Catatan untuk Pengembangan ke Depan

- Jika nanti Anda membuat:
  - `Module_2-Auth_JWT_PostgreSQL`
  - `Module_3-Message_Broker_RabbitMQ`
  - dan lain-lain…
- Cukup:
  1. Buat folder baru dengan nama yang konsisten (`Module_2-...`).
  2. Tambahkan `README.MD` di dalamnya.
  3. Update daftar module di `README.MD` root ini.

Dengan pola seperti ini, dosen/mahasiswa bisa langsung melihat **overview semua module** dari README root, dan detail teknisnya tetap rapi di dalam masing-masing submodule.

