# 🏢 Corporate – Django Web Project

Bu proje, Django framework kullanılarak geliştirilmiş, kullanıcıların kayıt olabildiği, giriş yapabildiği ve yönetici paneli üzerinden içeriklerin düzenlenebildiği kurumsal bir web sitesi altyapısı sunmaktadır.

## 🚀 Özellikler

- Kullanıcı kayıt / giriş / çıkış işlemleri
- Admin paneli üzerinden içerik yönetimi
- Bootstrap ile responsive (mobil uyumlu) tasarım
- ModelTranslation ile çoklu dil desteği
- SQLite veritabanı desteği
- Temiz ve modüler yapı

## 🔧 Kullanılan Teknolojiler ve Kütüphaneler

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap 4/5
- **Veritabanı:** SQLite
- **Kütüphaneler:**
  - `django-modeltranslation`
  - `django-crispy-forms` *(isteğe bağlı)*
  - `python-decouple` *(ortam değişkenleri için)*

## 🧩 Proje Yapısı

```
corporate/
├── accounts/           # Kullanıcı yönetimi (login, register)
├── core/               # Ana sayfa, hakkımızda, iletişim vb.
├── static/             # CSS, JS, görseller
├── templates/          # HTML şablonları
├── corporate/          # Ayarlar ve URL yönlendirmeleri
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ⚙️ Kurulum

Aşağıdaki adımları izleyerek projeyi kendi bilgisayarınızda çalıştırabilirsiniz:

```bash
# 1. Repoyu klonla
git clone https://github.com/tugraozdemir/django_web_project.git
cd django_web_project

# 2. Sanal ortam oluştur ve etkinleştir
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Gereksinimleri yükle
pip install -r requirements.txt

# 4. Veritabanını oluştur
python manage.py makemigrations
python manage.py migrate

# 5. Süper kullanıcı oluştur
python manage.py createsuperuser

# 6. Sunucuyu başlat
python manage.py runserver
```

## 🔐 Admin Panel Girişi

- **URL:** http://127.0.0.1:8000/admin
- **Kullanıcı Adı / Şifre:** Kurulum sırasında belirlenir.


## 🤝 Katkı

Proje açık kaynaklıdır. Her türlü katkı, öneri ve geri bildirim memnuniyetle karşılanır. PR (Pull Request) veya Issue açabilirsiniz.

---

© 2025 Tuğra Özdemir – [GitHub](https://github.com/tugraozdemir)
