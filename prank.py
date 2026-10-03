import tkinter as tk
import random


root = tk.Tk()
root.title("System Diagnostic")


root.attributes("-fullscreen", True)


root.configure(bg="black")

# boton para cortar de raiz el archivo
root.bind("/", lambda event: root.destroy())


# recordatorio propio:
# No usé grab_set(), bloqueo de teclado, mouse,
# taskkill, registry, os.system, subprocess, etc.

# ------------------------------------------------------------
# UTIL
# ------------------------------------------------------------

jobs = []


def later(ms, function):
    
    job = root.after(ms, function)
    jobs.append(job)
    return job


def clear():
    
    for widget in root.winfo_children():
        widget.destroy()


def label(text="", size=18, color="white",
          bg="black", font="Consolas", bold=False):

    weight = "bold" if bold else "normal"

    lbl = tk.Label(
        root,
        text=text,
        fg=color,
        bg=bg,
        font=(font, size, weight)
    )

    return lbl


# ============================================================
# FASE 1 - TERMINAL FEKA
# 
# ============================================================

def phase_terminal():

    clear()
    root.configure(bg="black")

    terminal = tk.Text(
        root,
        bg="black",
        fg="#00ff41",
        insertbackground="#00ff41",
        font=("Consolas", 13),
        borderwidth=0,
        highlightthickness=0
    )

    terminal.pack(fill="both", expand=True, padx=25, pady=20)

    fake_lines = [
        "[SYSTEM] Initializing diagnostic environment...",
        "[SYSTEM] Loading kernel modules...",
        "[OK] Memory verification complete",
        "[OK] Network interface detected",
        "[SCAN] Searching active processes...",
        "[SCAN] C:\\Users\\TARGET\\Documents\\archivo_001.dat",
        "[SCAN] C:\\Users\\TARGET\\Desktop\\backup_003.bin",
        "[SCAN] C:\\Users\\TARGET\\Pictures\\cache_481.tmp",
        "[WARNING] Unknown executable signature detected",
        "[WARNING] Unauthorized process detected",
        "[SYSTEM] Attempting process termination...",
        "[ERROR] TERMINATION FAILED",
        "[ERROR] ACCESS CONTROL OVERRIDE",
        "[SYSTEM] Retrying...",
        "[ERROR] FAILED",
    ]

    index = 0

    def add_line():
        nonlocal index

        if index >= len(fake_lines):
            return

        terminal.insert("end", fake_lines[index] + "\n")
        terminal.see("end")

        index += 1

        # Velocidad ligeramente variable
        later(random.randint(250, 500), add_line)

    add_line()

    later(8000, phase_warning)


# ============================================================
# FASE 2 - WARNING
# 
# ============================================================

def phase_warning():

    clear()
    root.configure(bg="black")

    label(
        "⚠  WARNING  ⚠",
        38,
        "#ff2020",
        bold=True
    ).pack(pady=(100, 30))

    label(
        "UNAUTHORIZED SYSTEM CONTROL DETECTED",
        22,
        "#ff4040",
        bold=True
    ).pack(pady=10)

    status = label(
        "Attempting recovery...",
        17,
        "#cccccc"
    )

    status.pack(pady=40)

    later(
        1800,
        lambda: status.config(
            text="RECOVERY FAILED",
            fg="#ff0000"
        )
    )

    later(3500, phase_charras)


# ============================================================
# FASE 3 - EL CHARRAS
# 
# ============================================================

def phase_charras():

    clear()
    root.configure(bg="#160000")

    label(
        "PC CHARREADA POR EL CHARRAS",
        42,
        "red",
        "#160000",
        bold=True
    ).pack(pady=(120, 25))

    label(
        "WARNING",
        30,
        "#ff4444",
        "#160000",
        bold=True
    ).pack(pady=10)

    error = label(
        "6767 ERROR",
        34,
        "white",
        "#160000",
        bold=True
    )

    error.pack(pady=35)

    # Parpadeo
    def blink(count=0):

        if count >= 8:
            return

        error.config(
            fg="red" if count % 2 == 0 else "white"
        )

        later(300, lambda: blink(count + 1))

    blink()

    later(6000, phase_fake_encryption)


# ============================================================
# FASE 4 - "CIFRADO" feka
# 20 - 29 segundos
# ============================================================

def phase_fake_encryption():

    clear()
    root.configure(bg="black")

    label(
        "CRITICAL SECURITY FAILURE",
        30,
        "red",
        bold=True
    ).pack(pady=(80, 30))

    encrypted = label(
        "FILES ENCRYPTED: 0",
        22,
        "#ff3030",
        bold=True
    )

    encrypted.pack(pady=15)

    
    
    fake_count = 0

    def increase():

        nonlocal fake_count

        fake_count += random.randint(40, 130)

        if fake_count > 1847:
            fake_count = 1847

        encrypted.config(
            text=f"FILES ENCRYPTED: {fake_count}"
        )

        if fake_count < 1847:
            later(180, increase)

    increase()

    label(
        "Recovery environment: DISABLED",
        18,
        "orange"
    ).pack(pady=20)

    label(
        "System integrity: COMPROMISED",
        18,
        "orange"
    ).pack(pady=10)

    progress = tk.Label(
        root,
        text="[□□□□□□□□□□□□□□] 0%",
        fg="white",
        bg="black",
        font=("Consolas", 18)
    )

    progress.pack(pady=40)

    percent = 0

    def progress_animation():

        nonlocal percent

        percent += random.randint(4, 11)

        if percent > 100:
            percent = 100

        blocks = int(percent / 7)

        bar = "■" * blocks + "□" * (14 - blocks)

        progress.config(
            text=f"[{bar}] {percent}%"
        )

        if percent < 100:
            later(300, progress_animation)

    progress_animation()

    later(9000, phase_critical)


# ============================================================
# FASE 5 - FALLO CRÍTICO
# AURA
# ============================================================

def phase_critical():

    clear()
    root.configure(bg="#250000")

    label(
        "CRITICAL SYSTEM FAILURE",
        42,
        "white",
        "#250000",
        bold=True
    ).pack(pady=(130, 30))

    label(
        "SYSTEM RECOVERY FAILED",
        24,
        "#ff4444",
        "#250000"
    ).pack(pady=20)

    countdown = label(
        "Restarting in 5...",
        25,
        "white",
        "#250000"
    )

    countdown.pack(pady=50)

    def fake_restart(n):

        if n <= 0:
            phase_bsod()
            return

        countdown.config(
            text=f"Restarting in {n}..."
        )

        later(900, lambda: fake_restart(n - 1))

    fake_restart(5)


# ============================================================
# FASE 6 - BSOD FALSO
# 36 - 45 segundos masomenos
# ============================================================

def phase_bsod():

    clear()

    bsod_blue = "#0078d7"
    root.configure(bg=bsod_blue)

    container = tk.Frame(
        root,
        bg=bsod_blue
    )

    container.pack(
        fill="both",
        expand=True,
        padx=150,
        pady=80
    )

    tk.Label(
        container,
        text=":(",
        fg="white",
        bg=bsod_blue,
        font=("Segoe UI", 75)
    ).pack(anchor="w")

    tk.Label(
        container,
        text=(
            "Your PC ran into a problem and needs to restart.\n"
            "We're just collecting some error info."
        ),
        justify="left",
        fg="white",
        bg=bsod_blue,
        font=("Segoe UI", 22)
    ).pack(anchor="w", pady=25)

    percent_label = tk.Label(
        container,
        text="0% complete",
        fg="white",
        bg=bsod_blue,
        font=("Segoe UI", 18)
    )

    percent_label.pack(anchor="w", pady=20)

    p = 0

    def bsod_progress():

        nonlocal p

        p += random.randint(8, 19)

        if p > 100:
            p = 100

        percent_label.config(
            text=f"{p}% complete"
        )

        if p < 100:
            later(500, bsod_progress)

    bsod_progress()

    later(8500, phase_black)


# ============================================================
# pantalla negra jkdjadkasj
# ============================================================

def phase_black():

    clear()
    root.configure(bg="black")

    # Solo 2 segundos.
    later(2000, phase_final)


# ============================================================
# FASE FINAL - tiene que durar maso 30 segundos
# ============================================================

def phase_final():

    clear()
    root.configure(bg="black")

    title = label(
        "CHECK YOUR SECURITY NEXT TIME",
        38,
        "red",
        bold=True
    )

    title.pack(pady=(110, 20))

    label(
        "agus - alan",
        24,
        "#aaaaaa"
    ).pack(pady=10)

    timer = label(
        "30",
        70,
        "#ff3030",
        bold=True
    )

    timer.pack(pady=45)

    message = label(
        "",
        28,
        "#00ff41",
        bold=True
    )

    message.pack(pady=20)

    # ========================================================
    # PARPADEO DEL "CHECK YOUR SECURITY NEXT TIME"
    # ========================================================

    blinking = True

    def blink_title():

        if not blinking:
            return

        
        if title.cget("fg") == "red":
            title.config(fg="black")
        else:
            title.config(fg="red")

        
        root.after(300, blink_title)

    blink_title()

    # ========================================================
    # CONTADOR
    # ========================================================

    seconds = 30

    def countdown():

        nonlocal seconds, blinking

        timer.config(text=str(seconds))

        
        if seconds == 10:

           
            blinking = False

            title.config(
                text="PISCUÍ",
                fg="white"
            )

            message.config(
                text="na mentira te cagaste todo"
            )

        
        if seconds <= 0:

            root.after(700, root.destroy)
            return

        seconds -= 1

        later(1000, countdown)

    countdown()


# ============================================================
# ARRANQUE
# ============================================================

phase_terminal()

root.mainloop()
