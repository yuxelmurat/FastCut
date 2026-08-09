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
    git clone https://github.com/yuxelmurat/FastCut.git
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

## 🏪 Microsoft Store'a Yayınlama

Bu depoda yayın için gerekli tüm dosyalar hazır: `build/build_exe.bat` (derleme), `installer/installer.iss` (yükleyici), `PRIVACY_POLICY.md` (gizlilik politikası) ve `store/STORE_LISTING.md` (Store listeleme metinleri).

> **Not:** FastCut sağ tık menüsü için sistem geneli registry (`HKEY_CLASSES_ROOT`) değiştirdiğinden ve bunun için yönetici izni istediğinden, **MSIX yerine "paketlenmemiş EXE/MSI" (unpackaged Win32 installer)** seçeneğiyle göndermeniz önerilir. MSIX sandbox'ı bu tür kalıcı sistem değişikliklerini varsayılan olarak kısıtlar.

1.  **EXE derle** *(Windows makinede)*:
    ```bash
    build\build_exe.bat
    ```
    Çıktı: `dist\FastCut.exe`

2.  **Yükleyici oluştur** *(Windows'ta, [Inno Setup](https://jrsoftware.org/isinfo.php) kurulu olmalı)*:
    ```bash
    iscc installer\installer.iss
    ```
    Çıktı: `installer\Output\FastCut-Setup-1.0.0.exe`

3.  **Gizlilik politikasını yayınla:** `PRIVACY_POLICY.md` içeriğini kendi web sitenize veya GitHub Pages'e koyup URL'sini not edin (Store gönderiminde zorunlu).

4.  **Partner Center hesabı açın:** [partner.microsoft.com/dashboard](https://partner.microsoft.com/dashboard) üzerinden (bireysel geliştirici kaydı, tek seferlik ücret + kimlik doğrulama gerektirir — bu adım geliştiricinin kendisi tarafından yapılmalıdır).

5.  **Yeni gönderim oluşturun**, paket türü olarak **"MSI or EXE (unpackaged)"** seçin, 2. adımdaki yükleyiciyi yükleyin.

6.  `store/STORE_LISTING.md` içindeki başlık, açıklama, anahtar kelime ve destek bilgilerini ilgili alanlara kopyalayın; ekran görüntülerini ekleyin.

7.  Gönderimi inceleme için yollayın. Sertifikasyon sırasında "neden yönetici izni istiyor" sorulursa, gizlilik politikasındaki açıklamayı referans gösterin (sağ tık menü entegrasyonu için).

## 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Herkes özgürce kullanabilir, değiştirebilir ve dağıtabilir.

## 📧 İletişim

**Design4D — Dijital Tasarım Ajansı**  
📍 Kocaeli — Türkiye  
✉️ murat@yukselmurat.com  
🌐 [yukselmurat.com](https://www.yukselmurat.com)
🌐 [design4d.com.tr](https://www.design4d.com.tr)

