# FastCut ✂️

**FastCut**, Windows kullanıcıları için geliştirilmiş, sağ tık menüsüne entegre olan pratik ve hızlı bir resim kesme (crop) aracıdır.

Karmaşık editörleri açmanıza gerek kalmadan, masaüstünde veya klasörde bir resme sağ tıklayıp anında istediğiniz alanı kesip kaydedebilirsiniz.

![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Özellikler

* **Sağ Tık Entegrasyonu:** Kurulumdan sonra herhangi bir resme (`.jpg`, `.png`) sağ tıklayıp "FastCut ile Kes" diyebilirsiniz.
* **Çerçevesiz Tasarım:** Windows kenarlıkları olmadan, temiz bir arayüz.
* **Akıllı Sabitleme (Smart Anchor):** Pencereyi hareket ettirirken resim uzayda sabit kalır, bu da kesme işlemini çok daha doğal hale getirir.
* **Resize & Stretch:** Pencerenin kenarlarından (Resize Handles) tutarak kesme alanını kolayca ayarlayabilirsiniz.
* **Otomatik İsimlendirme:** Orijinal dosyanın üzerine yazmaz. `DosyaAdi_fastcut_SAAT.jpg` formatında yeni bir kopya oluşturur.
* **Tek Dosya:** Kurulum ve kullanım tek bir `.exe` içerisindedir.

## 🚀 Kurulum (Kullanıcılar İçin)

1.  **Releases** kısmından en son `FastCut.exe` dosyasını indirin.
2.  Dosyayı bilgisayarınızda kalıcı olarak duracağı bir yere koyun (Örn: Belgelerim).
3.  `FastCut.exe` dosyasına **çift tıklayın**.
4.  *"Sağ tık menüsüne eklensin mi?"* sorusuna **Evet** deyin.
5.  Tebrikler! Artık bir resme sağ tıklayıp kullanabilirsiniz.

## 🛠️ Geliştiriciler İçin (Kaynak Koddan Çalıştırma)

Bu projeyi geliştirmek veya kodlarını incelemek isterseniz:

1.  Depoyu klonlayın:
    ```bash
    git clone [https://github.com/yuxelmurat/FastCut.git](https://github.com/yuxelmurat/FastCut.git)
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install Pillow pyinstaller
    ```

3.  Uygulamayı çalıştırın:
    ```bash
    python main.pyw
    ```

4.  EXE oluşturmak için (Build):
    ```bash
    pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --name "FastCut" "main.pyw"
    ```

## 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Herkes özgürce kullanabilir, değiştirebilir ve dağıtabilir.

