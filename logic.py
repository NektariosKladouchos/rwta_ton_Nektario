import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime, timedelta
import random

# Χρώματα GEYER
GREEN = '#27ae60'
BLUE = '#2980b9'
DARK = '#2c3e50'

def geyer_ceo_final_stable():
    root = tk.Tk()
    root.title("GEYER SMART HOME - Live Pricing Dashboard")
    root.state('zoomed')
    root.configure(bg="#f0f2f5")

    PRICES = {
        "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
        "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
        "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
        "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
        "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
    }
    
    brands = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]

    def update_live(*args):
        try:
            def get_v(v): return int(v.get() or 0)
            
            if not var_name.get() or not var_job.get() or not var_addr.get():
                txt_display.config(state="normal"); txt_display.delete("1.0", tk.END)
                txt_display.insert("1.0", "⚠️ LIVE PRICING: ΣΥΜΠΛΗΡΩΣΤΕ ΟΝΟΜΑ, ΙΔΙΟΤΗΤΑ & ΔΙΕΥΘΥΝΣΗ")
                txt_display.config(state="disabled"); return

            int_l = get_v(var_int_l); ext_l = get_v(var_ext_l)
            d220 = get_v(var_dim220); d110 = get_v(var_dim110); led = get_v(var_led); dali = get_v(var_dali); double = get_v(var_double)
            on_off_lines = (int_l + ext_l) - (d220 + d110 + led + dali + (double * 2))

            h_idx = combo_heat.current(); h_qty = get_v(var_h_qty)
            c_idx = combo_cool.current(); c_qty = get_v(var_c_qty)
            
            h_label_map = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. σωμάτων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
            c_label_map = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
            lbl_h_qty_txt.config(text=h_label_map[h_idx] if h_idx < len(h_label_map) else "Ποσότητα:")
            lbl_c_qty_txt.config(text=c_label_map[c_idx] if c_idx < len(c_label_map) else "Ποσότητα:")

            if h_idx == 6: h_brand_frame.grid()
            else: h_brand_frame.grid_remove()
            if c_idx == 4: c_brand_frame.grid()
            else: c_brand_frame.grid_remove()

            txt_display.config(state="normal"); txt_display.delete("1.0", tk.END)
            
            if (h_idx == 6 and combo_h_brand.get() == "Άλλη") or (c_idx == 4 and combo_c_brand.get() == "Άλλη"):
                txt_display.insert("1.0", "❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ (ΕΠΙΛΕΞΤΕ ΥΠΟΣΤΗΡΙΖΟΜΕΝΗ ΜΑΡΚΑ)"); txt_display.config(state="disabled"); return

            if h_idx == 6 and c_idx == 4 and combo_h_brand.get() != combo_c_brand.get():
                txt_display.insert("1.0", "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV ΣΕ ΘΕΡΜΑΝΣΗ/ΨΥΞΗ"); txt_display.config(state="disabled"); return

            is_common_type = (h_idx == 7 and c_idx == 5) or (h_idx == 3 and c_idx == 2) or (h_idx == 4 and c_idx == 3) or (h_idx == 6 and c_idx == 4)
            if is_common_type and h_qty != c_qty:
                txt_display.insert("1.0", "❌ ΛΑΘΟΣ: Ο ΑΡΙΘΜΟΣ ΜΟΝΑΔΩΝ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΙΔΙΟΣ ΣΕ ΘΕΡΜΑΝΣΗ ΚΑΙ ΨΥΞΗ"); txt_display.config(state="disabled"); return

            hvac_cost = 0; hvac_details = []
            if h_idx == 2 and c_idx == 1:
                cost = h_qty * PRICES["fancoil_ctrl"]; hvac_cost += cost
                hvac_details.append({"name": "Ενδοδαπέδια με Δροσισμό", "qty": h_qty, "price": cost})
            else:
                if h_idx > 0 and h_qty > 0:
                    p_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    cost = h_qty * PRICES[p_keys[h_idx]]; hvac_cost += cost
                    name = f"Interface VRV ({combo_h_brand.get()})" if h_idx == 6 else combo_heat.get()
                    hvac_details.append({"name": name, "qty": h_qty, "price": cost})
                
                is_common = (c_idx == 2 and h_idx == 3) or (c_idx == 3 and h_idx == 4) or (c_idx == 4 and h_idx == 6) or (c_idx == 5 and h_idx == 7)
                if c_idx > 0 and c_qty > 0 and not is_common:
                    p_keys_c = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    cost = c_qty * PRICES[p_keys_c[c_idx]]; hvac_cost += cost
                    name = f"Interface VRV ({combo_c_brand.get()}) - Ψ" if c_idx == 4 else combo_cool.get()
                    hvac_details.append({"name": name, "qty": c_qty, "price": cost})

            shutt = get_v(var_shutt)
            e_idx = var_energy.get()
            e_cost = 110 if e_idx == "1" else 160 if e_idx == "3" else 0
            h_cost = 95 if var_heater.get() else 0
            
            hvac_total_qty = sum(d['qty'] for d in hvac_details)
            base_dev_count = max(0, on_off_lines) + double + d220 + d110 + led + dali + shutt + hvac_total_qty + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
            
            if base_dev_count > 230:
                txt_display.insert("1.0", "❌ ΣΦΑΛΜΑ: ΤΟ ΣΥΣΤΗΜΑ ΥΠΟΣΤΗΡΙΖΕΙ ΜΕΧΡΙ 230 ΣΥΣΚΕΥΕΣ"); txt_display.config(state="disabled"); return

            hub_rows = []; hubs_cost = 0; hub_qty_total = 0
            if base_dev_count <= 37:
                hubs_cost = PRICES["hub_small"]; hub_qty_total = 1
                hub_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
            elif base_dev_count <= 97:
                hubs_cost = PRICES["hub_large"]; hub_qty_total = 1
                hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
            elif 97 < base_dev_count <= 130:
                hubs_cost = PRICES["hub_large"] + PRICES["hub_small"]; hub_qty_total = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
                hub_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
            else:
                hubs_cost = PRICES["hub_large"] * 2; hub_qty_total = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<35} | 2       | {PRICES['hub_large']*2:9.2f}€")

            total_dev = base_dev_count + hub_qty_total
            mat_sum = (max(0, on_off_lines)*63.92) + (double*63.92) + (d220*63.92) + (d110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + h_cost
            mat_fpa = mat_sum * 1.24
            prog_fee = mat_sum * 0.20

            if on_off_lines < 0:
                txt_display.insert("1.0", "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ: DIMMING > ΣΥΝΟΛΟ"); txt_display.config(state="disabled"); return

            res = f"{'='*70}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*70}\n"
            res += f"ΠΕΛΑΤΗΣ: {var_name.get().upper()} ({var_job.get()})\nΔΙΕΥΘΥΝΣΗ: {var_addr.get()}\n{'-'*70}\n"
            res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<35} | {'ΤΕΜΑΧΙΑ':<7} | {'ΤΙΜΗ':<10}\n{'-'*70}\n"
            for hr in hub_rows: res += f"{hr}\n"
            if on_off_lines > 0: res += f"{'Γραμμές Φωτισμού On/Off':<35} | {on_off_lines:<7} | {on_off_lines*63.92:9.2f}€\n"
            if double > 0:       res += f"{'Διπλές Γραμμές (Κομιτατέρ)':<35} | {double:<7} | {double*63.92:9.2f}€\n"
            if d220 > 0:         res += f"{'Dimming 220V':<35} | {d220:<7} | {d220*63.92:9.2f}€\n"
            if d110 > 0:         res += f"{'Dimming 1-10V':<35} | {d110:<7} | {d110*52.00:9.2f}€\n"
            if led > 0:          res += f"{'Ταινίες LED Dimming':<35} | {led:<7} | {led*63.92:9.2f}€\n"
            if dali > 0:         res += f"{'Γραμμές DALI':<35} | {dali:<7} | {dali*160.00:9.2f}€\n"
            if shutt > 0:        res += f"{'Ρολά / Τέντες / Κουρτίνες':<35} | {shutt:<7} | {shutt*63.92:9.2f}€\n"
            for d in hvac_details: res += f"{d['name']:<35} | {d['qty']:<7} | {d['price']:9.2f}€\n"
            if e_cost > 0:       res += f"{('Μονοφασικός μετρητής' if e_idx=='1' else 'Τριφασικός μετρητής'):<35} | 1       | {e_cost:9.2f}€\n"
            if h_cost > 0:       res += f"{'Έλεγχος Θερμοσίφωνα':<35} | 1       | {h_cost:9.2f}€\n"
            res += f"{'-'*70}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\nΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ: {mat_sum:27.2f}€\n"
            res += f"ΑΞΙΑ ΥΛΙΚΩΝ ΜΕ ΦΠΑ 24%: {mat_fpa:23.2f}€\n{'-'*70}\n"
            res += f"ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ: {prog_fee:23.2f}€\n(Προαιρετική υπηρεσία)\n{'='*70}\n"
            txt_display.insert("1.0", res); txt_display.config(state="disabled")
        except: pass

    def save_file():
        content = txt_display.get("1.0", tk.END)
        path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=f"GEYER_PROSFORA_{var_name.get()}")
        if path:
            with open(path, "w", encoding="utf-8") as f: f.write(content)
            messagebox.showinfo("Επιτυχία", "Η προσφορά αποθηκεύτηκε!")

    # UI LAYOUT
    header = tk.Frame(root, bg=GREEN, height=80); header.pack(fill="x")
    tk.Label(header, text="GEYER SMART HOME", font=("Arial", 24, "bold"), fg="white", bg=GREEN).pack(pady=(10,0))
    tk.Label(header, text="LIVE PRICING SYSTEM", font=("Arial", 12, "bold"), fg="#e0e0e0", bg=GREEN).pack(pady=(0,10))

    main = tk.Frame(root, bg="#f0f2f5"); main.pack(fill="both", expand=True)
    left = tk.Frame(main, bg="white", padx=15, pady=15, highlightthickness=1, highlightbackground="#d1d1d1")
    left.pack(side="left", fill="both", padx=20, pady=20, expand=True)

    canvas = tk.Canvas(left, bg="white", highlightthickness=0); scroll = ttk.Scrollbar(left, orient="vertical", command=canvas.yview)
    sf = tk.Frame(canvas, bg="white"); sf.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=sf, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True); scroll.pack(side="right", fill="y"); canvas.configure(yscrollcommand=scroll.set)

    # 1. ΣΤΟΙΧΕΙΑ
    tk.Label(sf, text="1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    tk.Label(sf, text="Ονοματεπώνυμο / Επωνυμία:", bg="white").pack(anchor="w")
    var_name = tk.StringVar(); var_name.trace_add("write", update_live); tk.Entry(sf, textvariable=var_name, width=40).pack(anchor="w")
    tk.Label(sf, text="Ιδιότητα (Υποχρεωτικό):", bg="white").pack(anchor="w")
    var_job = tk.StringVar(); var_job.trace_add("write", update_live); ttk.OptionMenu(sf, var_job, "", "Κατασκευαστής", "Μηχανικός", "Αρχιτέκτονας", "Ηλεκτρολόγος", "Κατάστημα", "Ιδιώτης").pack(anchor="w")
    tk.Label(sf, text="Διεύθυνση έργου:", bg="white").pack(anchor="w")
    var_addr = tk.StringVar(); var_addr.trace_add("write", update_live); tk.Entry(sf, textvariable=var_addr, width=40).pack(anchor="w")

    # 2. ΦΩΤΙΣΜΟΣ
    tk.Label(sf, text="\n2. ΣΥΝΟΛΙΚΕΣ ΓΡΑΜΜΕΣ ΦΩΤΙΣΜΟΥ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    var_int_l = tk.StringVar(value="0"); var_ext_l = tk.StringVar(value="0")
    tk.Label(sf, text="Εσωτερικές:", bg="white").pack(anchor="w"); tk.Entry(sf, textvariable=var_int_l, width=10).pack(anchor="w")
    tk.Label(sf, text="Εξωτερικές:", bg="white").pack(anchor="w"); tk.Entry(sf, textvariable=var_ext_l, width=10).pack(anchor="w")
    var_int_l.trace_add("write", update_live); var_ext_l.trace_add("write", update_live)

    tk.Label(sf, text="\n2α. ΕΙΔΗ ΓΡΑΜΜΩΝ ΠΟΥ ΘΕΛΟΥΜΕ DIMMING", font=("Arial", 9, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    f_g2 = tk.Frame(sf, bg="white"); f_g2.pack(fill="x")
    var_dim220 = tk.StringVar(value="0"); var_dim110 = tk.StringVar(value="0"); var_led = tk.StringVar(value="0"); var_dali = tk.StringVar(value="0"); var_double = tk.StringVar(value="0")
    for i, (t, v) in enumerate([("Dimming 220V:", var_dim220), ("Dimming 1-10V:", var_dim110), ("Ταινίες LED Dim:", var_led), ("DALI:", var_dali), ("Κομιτατέρ (Διπλές):", var_double)]):
        tk.Label(f_g2, text=t, bg="white").grid(row=i, column=0, sticky="w"); tk.Entry(f_g2, textvariable=v, width=8).grid(row=i, column=1, padx=5); v.trace_add("write", update_live)

    # 3 & 4 HVAC
    tk.Label(sf, text="\n3. ΘΕΡΜΑΝΣΗ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    h_f = tk.Frame(sf, bg="white"); h_f.pack(fill="x")
    combo_heat = ttk.Combobox(h_f, values=["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Κλιματιστικά split"], width=15)
    combo_heat.grid(row=0, column=0); combo_heat.current(0); combo_heat.bind("<<ComboboxSelected>>", update_live)
    h_brand_frame = tk.Frame(h_f, bg="white"); combo_h_brand = ttk.Combobox(h_brand_frame, values=brands, width=10); combo_h_brand.current(0); combo_h_brand.pack(side="left"); h_brand_frame.grid(row=0, column=1, padx=5); h_brand_frame.grid_remove(); combo_h_brand.bind("<<ComboboxSelected>>", update_live)
    lbl_h_qty_txt = tk.Label(h_f, text="Ποσότητα:", bg="white", font=("Arial", 9)); lbl_h_qty_txt.grid(row=1, column=0, sticky="w")
    var_h_qty = tk.StringVar(value="0"); tk.Entry(h_f, textvariable=var_h_qty, width=5).grid(row=1, column=1, sticky="w"); var_h_qty.trace_add("write", update_live)

    tk.Label(sf, text="\n4. ΨΥΞΗ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    c_f = tk.Frame(sf, bg="white"); c_f.pack(fill="x")
    combo_cool = ttk.Combobox(c_f, values=["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "VRV/VRF", "Κλιματιστικά split"], width=15)
    combo_cool.grid(row=0, column=0); combo_cool.current(0); combo_cool.bind("<<ComboboxSelected>>", update_live)
    c_brand_frame = tk.Frame(c_f, bg="white"); combo_c_brand = ttk.Combobox(c_brand_frame, values=brands, width=10); combo_c_brand.current(0); combo_c_brand.pack(side="left"); c_brand_frame.grid(row=0, column=1, padx=5); c_brand_frame.grid_remove(); combo_c_brand.bind("<<ComboboxSelected>>", update_live)
    lbl_c_qty_txt = tk.Label(c_f, text="Ποσότητα:", bg="white", font=("Arial", 9)); lbl_c_qty_txt.grid(row=1, column=0, sticky="w")
    var_c_qty = tk.StringVar(value="0"); tk.Entry(c_f, textvariable=var_c_qty, width=5).grid(row=1, column=1, sticky="w"); var_c_qty.trace_add("write", update_live)

    # 5 & 6
    tk.Label(sf, text="\n5. ΡΟΛΑ / ΤΕΝΤΕΣ / ΚΟΥΡΤΙΝΕΣ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    var_shutt = tk.StringVar(value="0"); tk.Entry(sf, textvariable=var_shutt, width=10).pack(anchor="w"); var_shutt.trace_add("write", update_live)
    tk.Label(sf, text="\n6. ΠΙΝΑΚΑΣ", font=("Arial", 10, "bold"), fg=BLUE, bg="white").pack(anchor="w")
    var_energy = tk.StringVar(value="0"); var_energy.trace_add("write", update_live)
    for t,v in [("Όχι","0"), ("Μονοφασικός μετρητής","1"), ("Τριφασικός μετρητής","3")]: tk.Radiobutton(sf, text=t, variable=var_energy, value=v, bg="white").pack(anchor="w")
    var_heater = tk.BooleanVar(); var_heater.trace_add("write", update_live); tk.Checkbutton(sf, text="Έλεγχος Θερμοσίφωνα", variable=var_heater, bg="white").pack(anchor="w")

    right = tk.Frame(main, bg=DARK, padx=20, pady=20); right.pack(side="right", fill="both", expand=True, padx=20, pady=20)
    txt_display = tk.Text(right, font=("Consolas", 11), bg="#ecf0f1", padx=15, pady=15); txt_display.pack(fill="both", expand=True)
    tk.Button(right, text="💾 ΑΠΟΘΗΚΕΥΣΗ ΠΡΟΣΦΟΡΑΣ", font=("Arial", 12, "bold"), bg=GREEN, fg="white", pady=12, command=save_file).pack(fill="x", pady=10)
    
    update_live(); root.mainloop()

if __name__ == "__main__":
    geyer_ceo_final_stable()
