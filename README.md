# FastCut ✂️

🇬🇧 [English](#english) | 🇹🇷 [Türkçe](#türkçe)

![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## English

**FastCut** is a lightweight, right-click image cropping tool for Windows.

No need to open a full photo editor — just right-click any image on your desktop or in a folder, drag out the area you want, and save.

### 🌟 Features

* **Right-Click Integration:** After installation, right-click any image (`.jpg`, `.png`) and select "FastCut ile Kes" ("Crop with FastCut").
* **Borderless Design:** A clean interface with no Windows window chrome.
* **Smart Anchor:** The image stays fixed in space while you move the crop window, making cropping feel natural.
* **Resize & Stretch:** Drag the window's edges (resize handles) to adjust the crop area.
* **Dimmed Overlay:** The area outside the crop stays visibly dimmed so you always see exactly what will be kept.
* **Live Size Indicator:** The current crop dimensions are shown in real time as you resize.
* **Keyboard Shortcuts:** `Enter` to save, `Esc` to cancel.
* **Automatic Naming:** Never overwrites the original file — creates a new copy named `FileName_fastcut_HH_MM_SS.jpg`.
* **Full Resolution:** Crops are taken from the original image, not a downscaled preview, so there's no quality loss.
* **Single File:** Installation and usage are both handled by one `.exe`.

### 🚀 Installation (for users)

1. Download the latest `FastCut.exe` from the **Releases** page.
2. Place the file somewhere permanent on your computer (e.g. Documents).
3. **Double-click** `FastCut.exe`.
4. Answer **Yes** to *"Add to right-click menu?"*.
5. Done! Right-click any image to use it.

### 🛠️ For Developers (running from source)

1. Clone the repository:
   ```bash
   git clone https://github.com/yuxelmurat/FastCut.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.pyw
   ```

4. Build the `.exe` (on Windows):
   ```bash
   build\build_exe.bat
   ```
   Output: `dist\FastCut.exe`

### 🏪 Publishing to the Microsoft Store

Everything needed is already in this repo: `build/build_exe.bat` (build script), `installer/installer.iss` (Inno Setup installer), `PRIVACY_POLICY.md`, and `store/STORE_LISTING.md` (store listing copy).

> **Note:** Because FastCut modifies the system-wide registry (`HKEY_CLASSES_ROOT`) for its right-click integration and requests administrator elevation to do so, submit it as an **unpackaged EXE/MSI installer** rather than MSIX — the MSIX sandbox restricts this kind of persistent system change by default.

1. **Build the exe** *(on Windows)*: `build\build_exe.bat` → produces `dist\FastCut.exe`
2. **Build the installer** *(on Windows, with [Inno Setup](https://jrsoftware.org/isinfo.php) installed)*: `iscc installer\installer.iss` → produces `installer\Output\FastCut-Setup-1.0.0.exe`
3. **Publish the privacy policy**: host `PRIVACY_POLICY.md`'s content on your own site or GitHub Pages and note the URL (required for submission).
4. **Create a Partner Center account**: [partner.microsoft.com/dashboard](https://partner.microsoft.com/dashboard) (one-time fee + identity verification, done by you personally).
5. **Create a new submission**, choose **"MSI or EXE (unpackaged)"** as the package type, upload the installer from step 2.
6. Copy the title, description, keywords, and support info from `store/STORE_LISTING.md` into the submission form; add screenshots.
7. Submit for certification. If asked why the app requests admin rights, point to the privacy policy's explanation (needed for right-click menu integration).

### 📝 License

This project is licensed under the MIT License. Anyone is free to use, modify, and distribute it.

### 📧 Contact

**Design4D — Digital Design Agency**
📍 Kocaeli — Turkey
✉️ murat@yukselmurat.com
🌐 [yukselmurat.com](https://www.yukselmurat.com)
🌐 [design4d.com.tr](https://www.design4d.com.tr)

---

## Türkçe

**FastCut**, Windows kullanıcıları için geliştirilmiş, sağ tık menüsüne entegre olan pratik ve hızlı bir resim kesme (crop) aracıdır.

Karmaşık editörleri açmanıza gerek kalmadan, masaüstünde veya klasörde bir resme sağ tıklayıp anında istediğiniz alanı kesip kaydedebilirsiniz.

### 🌟 Özellikler

* **Sağ Tık Entegrasyonu:** Kurulumdan sonra herhangi bir resme (`.jpg`, `.png`) sağ tıklayıp "FastCut ile Kes" diyebilirsiniz.
* **Çerçevesiz Tasarım:** Windows kenarlıkları olmadan, temiz bir arayüz.
* **Akıllı Sabitleme (Smart Anchor):** Pencereyi hareket ettirirken resim uzayda sabit kalır, bu da kesme işlemini çok daha doğal hale getirir.
* **Resize & Stretch:** Pencerenin kenarlarından (Resize Handles) tutarak kesme alanını kolayca ayarlayabilirsiniz.
* **Karartma Overlay:** Kesim alanı dışında kalan kısım karartılır, böylece neyin kaydedileceğini her zaman net görürsünüz.
* **Canlı Boyut Göstergesi:** Yeniden boyutlandırırken kesim alanının boyutu anlık olarak gösterilir.
* **Klavye Kısayolları:** Kaydetmek için `Enter`, iptal için `Esc`.
* **Otomatik İsimlendirme:** Orijinal dosyanın üzerine yazmaz. `DosyaAdi_fastcut_SAAT.jpg` formatında yeni bir kopya oluşturur.
* **Tam Çözünürlük:** Kesim, küçültülmüş önizleme yerine orijinal görselden yapılır, kalite kaybı olmaz.
* **Tek Dosya:** Kurulum ve kullanım tek bir `.exe` içerisindedir.

### 🚀 Kurulum (Kullanıcılar İçin)

1. **Releases** kısmından en son `FastCut.exe` dosyasını indirin.
2. Dosyayı bilgisayarınızda kalıcı olarak duracağı bir yere koyun (Örn: Belgelerim).
3. `FastCut.exe` dosyasına **çift tıklayın**.
4. *"Sağ tık menüsüne eklensin mi?"* sorusuna **Evet** deyin.
5. Tebrikler! Artık bir resme sağ tıklayıp kullanabilirsiniz.

### 🛠️ Geliştiriciler İçin (Kaynak Koddan Çalıştırma)

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/yuxelmurat/FastCut.git
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Uygulamayı çalıştırın:
   ```bash
   python main.pyw
   ```

4. EXE oluşturmak için (Windows'ta):
   ```bash
   build\build_exe.bat
   ```
   Çıktı: `dist\FastCut.exe`

### 🏪 Microsoft Store'a Yayınlama

Bu depoda yayın için gerekli tüm dosyalar hazır: `build/build_exe.bat` (derleme), `installer/installer.iss` (yükleyici), `PRIVACY_POLICY.md` (gizlilik politikası) ve `store/STORE_LISTING.md` (Store listeleme metinleri).

> **Not:** FastCut sağ tık menüsü için sistem geneli registry (`HKEY_CLASSES_ROOT`) değiştirdiğinden ve bunun için yönetici izni istediğinden, **MSIX yerine "paketlenmemiş EXE/MSI" (unpackaged Win32 installer)** seçeneğiyle göndermeniz önerilir. MSIX sandbox'ı bu tür kalıcı sistem değişikliklerini varsayılan olarak kısıtlar.

1. **EXE derle** *(Windows makinede)*:
   ```bash
   build\build_exe.bat
   ```
   Çıktı: `dist\FastCut.exe`

2. **Yükleyici oluştur** *(Windows'ta, [Inno Setup](https://jrsoftware.org/isinfo.php) kurulu olmalı)*:
   ```bash
   iscc installer\installer.iss
   ```
   Çıktı: `installer\Output\FastCut-Setup-1.0.0.exe`

3. **Gizlilik politikasını yayınla:** `PRIVACY_POLICY.md` içeriğini kendi web sitenize veya GitHub Pages'e koyup URL'sini not edin (Store gönderiminde zorunlu).

4. **Partner Center hesabı açın:** [partner.microsoft.com/dashboard](https://partner.microsoft.com/dashboard) üzerinden (bireysel geliştirici kaydı, tek seferlik ücret + kimlik doğrulama gerektirir — bu adım geliştiricinin kendisi tarafından yapılmalıdır).

5. **Yeni gönderim oluşturun**, paket türü olarak **"MSI or EXE (unpackaged)"** seçin, 2. adımdaki yükleyiciyi yükleyin.

6. `store/STORE_LISTING.md` içindeki başlık, açıklama, anahtar kelime ve destek bilgilerini ilgili alanlara kopyalayın; ekran görüntülerini ekleyin.

7. Gönderimi inceleme için yollayın. Sertifikasyon sırasında "neden yönetici izni istiyor" sorulursa, gizlilik politikasındaki açıklamayı referans gösterin (sağ tık menü entegrasyonu için).

### 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Herkes özgürce kullanabilir, değiştirebilir ve dağıtabilir.

### 📧 İletişim

**Design4D — Dijital Tasarım Ajansı**
📍 Kocaeli — Türkiye
✉️ murat@yukselmurat.com
🌐 [yukselmurat.com](https://www.yukselmurat.com)
🌐 [design4d.com.tr](https://www.design4d.com.tr)
