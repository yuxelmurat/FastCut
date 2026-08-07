import sys
import os
import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def install_context_menu():
    exe_path = sys.executable
    icon_path = exe_path 
    
    key_path = r"SystemFileAssociations\image\shell\FastCut"
    
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValue(key, "", winreg.REG_SZ, "FastCut ile Kes")
        winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, icon_path)
        winreg.CloseKey(key)
        
        cmd_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path + r"\command")
        winreg.SetValue(cmd_key, "", winreg.REG_SZ, f'"{exe_path}" "%1"')
        winreg.CloseKey(cmd_key)
        
        messagebox.showinfo("Başarılı", "FastCut sağ tık menüsüne başarıyla eklendi!\nArtık resimlere sağ tıklayabilirsiniz.")
    except Exception as e:
        messagebox.showerror("Hata", f"Kayıt defterine erişilemedi:\n{e}")

class FastCutApp:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path
        
        # --- AYARLAR ---
        self.root.overrideredirect(True) 
        self.root.configure(bg='black')
        self.grip_size = 15 
        
        # --- RESİM YÜKLEME ---
        try:
            self.original_image = Image.open(self.image_path)
        except Exception as e:
            # Eğer yanlışlıkla exe dosyası gönderildiyse sessizce çık veya uyar
            if str(e).strip() == "":
                sys.exit()
            messagebox.showerror("Hata", f"Resim açılamadı:\n{e}")
            sys.exit()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        target_w = int(screen_width * 0.8)
        target_h = int(screen_height * 0.8)

        img_w, img_h = self.original_image.size
        ratio = min(target_w / img_w, target_h / img_h)
        
        self.display_w = int(img_w * ratio)
        self.display_h = int(img_h * ratio)
        
        self.resized_image = self.original_image.resize((self.display_w, self.display_h), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.resized_image)

        self.win_x = (screen_width - self.display_w) // 2
        self.win_y = (screen_height - self.display_h) // 2
        self.win_w = self.display_w
        self.win_h = self.display_h
        
        self.root.geometry(f"{self.win_w}x{self.win_h}+{self.win_x}+{self.win_y}")

        self.abs_img_x = self.win_x
        self.abs_img_y = self.win_y

        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        self.root.bind("<Motion>", self.check_cursor)
        self.root.bind("<ButtonPress-1>", self.start_action)
        self.root.bind("<B1-Motion>", self.do_action)
        
        self.action_mode = None
        self.add_buttons()

    def check_cursor(self, event):
        x, y = event.x, event.y
        w, h = self.root.winfo_width(), self.root.winfo_height()
        g = self.grip_size
        mode = ""
        if y < g: mode += "n"
        elif y > h - g: mode += "s"
        if x < g: mode += "w"
        elif x > w - g: mode += "e"

        if mode == "": self.root.config(cursor="fleur")
        elif mode == "n" or mode == "s": self.root.config(cursor="sb_v_double_arrow")
        elif mode == "e" or mode == "w": self.root.config(cursor="sb_h_double_arrow")
        elif "n" in mode and "e" in mode: self.root.config(cursor="top_right_corner")
        elif "n" in mode and "w" in mode: self.root.config(cursor="top_left_corner")
        elif "s" in mode and "e" in mode: self.root.config(cursor="bottom_right_corner")
        elif "s" in mode and "w" in mode: self.root.config(cursor="bottom_left_corner")
        self.current_cursor_mode = mode

    def start_action(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.start_win_x = self.root.winfo_x()
        self.start_win_y = self.root.winfo_y()
        self.start_win_w = self.root.winfo_width()
        self.start_win_h = self.root.winfo_height()
        if self.current_cursor_mode == "": self.action_mode = "move"
        else: self.action_mode = self.current_cursor_mode

    def do_action(self, event):
        if not self.action_mode: return
        dx = event.x_root - self.start_x
        dy = event.y_root - self.start_y
        new_x, new_y = self.start_win_x, self.start_win_y
        new_w, new_h = self.start_win_w, self.start_win_h
        mode = self.action_mode

        if mode == "move":
            new_x += dx
            new_y += dy
        else:
            if "e" in mode: new_w += dx
            if "w" in mode: new_w -= dx; new_x += dx
            if "s" in mode: new_h += dy
            if "n" in mode: new_h -= dy; new_y += dy

        if new_w < 50: new_w = 50
        if new_h < 50: new_h = 50

        self.root.geometry(f"{new_w}x{new_h}+{new_x}+{new_y}")
        
        current_win_x = self.root.winfo_x()
        current_win_y = self.root.winfo_y()
        offset_x = self.abs_img_x - current_win_x
        offset_y = self.abs_img_y - current_win_y
        self.canvas.coords(self.image_on_canvas, offset_x, offset_y)

    def add_buttons(self):
        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        btn_cancel = tk.Button(btn_frame, text="X", bg="red", fg="white", font=("Arial", 12, "bold"), command=self.close_app, width=3, bd=0)
        btn_cancel.pack(side="right", padx=5)
        btn_save = tk.Button(btn_frame, text="✓", bg="green", fg="white", font=("Arial", 12, "bold"), command=self.save_image, width=3, bd=0)
        btn_save.pack(side="right", padx=5)

    def save_image(self):
        win_x = self.root.winfo_x()
        win_y = self.root.winfo_y()
        win_w = self.root.winfo_width()
        win_h = self.root.winfo_height()
        img_rel_x = self.abs_img_x - win_x
        img_rel_y = self.abs_img_y - win_y
        crop_x1 = -img_rel_x
        crop_y1 = -img_rel_y
        crop_x2 = crop_x1 + win_w
        crop_y2 = crop_y1 + win_h
        
        try:
            scale_x = self.original_image.width / self.display_w
            scale_y = self.original_image.height / self.display_h
            orig_crop = (
                crop_x1 * scale_x,
                crop_y1 * scale_y,
                crop_x2 * scale_x,
                crop_y2 * scale_y,
            )
            cropped = self.original_image.crop(orig_crop)
            dir_name, file_name = os.path.split(self.image_path)
            name, ext = os.path.splitext(file_name)
            timestamp = datetime.datetime.now().strftime("%H_%M_%S")
            new_filename = f"{name}_fastcut_{timestamp}{ext}"
            save_path = os.path.join(dir_name, new_filename)
            cropped.save(save_path)
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Hata", f"Hata:\n{e}")

    def close_app(self):
        self.root.destroy()

if __name__ == "__main__":
    # Eğer programa resim ile tıklanmadıysa (Çift Tıklama Modu - Kurulum)
    if len(sys.argv) < 2:
        if is_admin():
            # Yönetici isek kurulumu yap
            root = tk.Tk()
            root.withdraw()
            ans = messagebox.askyesno("Kurulum", "FastCut sağ tık menüsüne eklensin mi?")
            if ans:
                install_context_menu()
            sys.exit()
        else:
            # Yönetici değilsek, yönetici olarak YENİDEN BAŞLAT
            # DÜZELTME BURADA: Parametre kısmını boş ("") gönderiyoruz.
            # Böylece yeniden başladığında sys.argv yine tek elemanlı (exe) olacak.
            params = ""
            if not getattr(sys, 'frozen', False):
                 # Eğer script olarak çalışıyorsa argümanları koru (test amaçlı)
                 params = " ".join(sys.argv)
            
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
            sys.exit()

    # Eğer resim gönderildiyse (Sağ Tık Modu - Çalışma)
    image_arg = sys.argv[1]
    root = tk.Tk()
    app = FastCutApp(root, image_arg)
    root.mainloop()