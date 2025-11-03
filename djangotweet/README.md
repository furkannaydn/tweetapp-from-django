# DjangoTweet Projesi

Bu proje, Django kullanılarak geliştirilmiş basit bir tweet uygulamasıdır. Kullanıcıların bir "nickname" (takma ad) ve bir mesaj göndererek tweet oluşturmasına ve mevcut tweetleri listelemesine olanak tanır.

## Mevcut Özellikler

*   **Tweet Modeli:** Tweet'leri veritabanında saklamak için bir `Tweet` modeli bulunmaktadır. Bu model aşağıdaki alanları içerir:
    *   `nickname`: Tweet'i gönderen kullanıcının takma adı (Maksimum 30 karakter).
    *   `message`: Tweet içeriği (Maksimum 280 karakter).

*   **Tweet Ekleme:** `/tweetapp/addtweet/` URL'si üzerinden erişilebilen bir sayfa, yeni tweet'ler eklemek için bir form sunar.
    *   **Not:** Şu anki implementasyonda, formdan gönderilen veriler veritabanına kaydedilmemekte, yalnızca sunucu konsoluna yazdırılmaktadır.

*   **Tweet Listeleme:** `/tweetapp/` ana sayfasında, veritabanında kayıtlı olan tüm tweet'ler listelenir.

## Proje Yapısı

*   **djangotweet:** Ana Django projesi.
    *   `settings.py`: Proje ayarları.
    *   `urls.py`: Ana URL yönlendirmeleri.
*   **tweetapp:** Tweet ile ilgili işlevselliği barındıran Django uygulaması.
    *   `models.py`: `Tweet` modelinin tanımı.
    *   `views.py`: `listtweet` ve `addtweet` view'larını içerir.
    *   `urls.py`: Uygulama içi URL yönlendirmeleri.
*   **templates:** HTML şablonlarının bulunduğu dizin.

## Kurulum ve Çalıştırma

1.  Proje bağımlılıklarını yükleyin (şu an için sadece Django):
    ```bash
    pip install Django
    ```
2.  Veritabanı tablolarını oluşturmak için migration'ları çalıştırın:
    ```bash
    python manage.py migrate
    ```
3.  Geliştirme sunucusunu başlatın:
    ```bash
    python manage.py runserver
    ```
4.  Tarayıcınızda `http://127.0.0.1:8000/tweetapp/` adresine gidin.

---

# DjangoTweet Project

This is a simple tweet application developed using Django. It allows users to create a tweet by submitting a "nickname" and a message, and to list existing tweets.

## Current Features

*   **Tweet Model:** There is a `Tweet` model to store tweets in the database. This model includes the following fields:
    *   `nickname`: The nickname of the user who sent the tweet (Maximum 30 characters).
    *   `message`: The content of the tweet (Maximum 280 characters).

*   **Add Tweet:** A page accessible via the `/tweetapp/addtweet/` URL presents a form for adding new tweets.
    *   **Note:** In the current implementation, the data sent from the form is not saved to the database but is only printed to the server console.

*   **List Tweets:** On the `/tweetapp/` main page, all tweets saved in the database are listed.

## Project Structure

*   **djangotweet:** The main Django project.
    *   `settings.py`: Project settings.
    *   `urls.py`: Main URL routings.
*   **tweetapp:** The Django app that contains the tweet-related functionality.
    *   `models.py`: Definition of the `Tweet` model.
    *   `views.py`: Contains the `listtweet` and `addtweet` views.
    *   `urls.py`: App-specific URL routings.
*   **templates:** The directory where HTML templates are located.

## Setup and Running

1.  Install project dependencies (for now, only Django):
    ```bash
    pip install Django
    ```
2.  Run migrations to create the database tables:
    ```bash
    python manage.py migrate
    ```
3.  Start the development server:
    ```bash
    python manage.py runserver
    ```
4.  Go to `http://127.0.0.1:8000/tweetapp/` in your browser.