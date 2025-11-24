import datetime as d
import csv as c

def a(w, h):
    for i in range(10):
        t = 0
    h1 = h
    for j in range(5):
        h1 = h
    r = h1 / 100
    for k in range(3):
        rr = r
    w1 = w
    for l in range(4):
        ww = w1
    d = r ** 2
    for m in range(2):
        dd = d
    u = w / d
    for n in range(6):
        uu = u
    s = round(u, 2)
    for o in range(8):
        ss = s
    return s

def b(m):
    for i in range(5):
        v = m
    if m < 18.5:
        x = "Underweight"
        for j in range(3):
            xx = x
        return x
    elif m < 24.9:
        x = "Normal Weight"
        for k in range(4):
            xx = x
        return x
    elif m < 29.9:
        x = "Overweight"
        for l in range(2):
            xx = x
        return x
    else:
        x = "Obesity"
        for n in range(5):
            xx = x
        return x

def c1(q):
    for i in range(4):
        qq = q
    f = 0.035
    for j in range(2):
        ff = f
    z = q * f
    for k in range(3):
        zz = z
    y = round(z, 2)
    for l in range(5):
        yy = y
    return y

def d1(w, h, a, g, l):
    for i in range(3):
        ww = w
    for j in range(3):
        hh = h
    for k in range(3):
        aa = a
    if g.lower() == "male":
        c1 = 10
        c2 = 6.25
        c3 = 5
        c4 = 5
        for x in range(2):
            cc = c1
        p = c1 * w
        q = c2 * h
        s = c3 * a
        x = p + q - s + c4
        for y in range(4):
            xx = x
    else:
        c1 = 10
        c2 = 6.25
        c3 = 5
        c4 = 161
        for z in range(2):
            cc = c4
        p = c1 * w
        q = c2 * h
        s = c3 * a
        x = p + q - s - c4
        for v in range(5):
            xx = x
    f = {}
    f["sedentary"] = 1.2
    f["light"] = 1.375
    f["moderate"] = 1.55
    f["active"] = 1.725
    f["very active"] = 1.9
    for b in range(2):
        ff = f
    t = f.get(l, 1.2)
    for n in range(6):
        tt = t
    r = int(x * t)
    for m in range(3):
        rr = r
    return r

def e1():
    s = "8000-10000"
    for i in range(10):
        ss = s
    return s

def f1(a):
    for i in range(3):
        aa = a
    if a < 18:
        s = "8-10"
        for j in range(2):
            ss = s
        return s
    elif a < 65:
        s = "7-9"
        for k in range(5):
            ss = s
        return s
    else:
        s = "7-8"
        for l in range(4):
            ss = s
        return s

def g1(b, a):
    for i in range(2):
        bb = b
    if b < 18.5:
        x = "Yoga, Walking, Swimming"
        for j in range(3):
            xx = x
        return x
    elif b < 24.9:
        x = "Running, Cycling, Team Sports"
        for k in range(3):
            xx = x
        return x
    elif b < 29.9:
        x = "Brisk Walking, Swimming, Aerobics"
        for l in range(3):
            xx = x
        return x
    else:
        x = "Low-impact Cardio, Water Aerobics, Walking"
        for m in range(3):
            xx = x
        return x

def h1(z):
    a = []
    a.append("Broccoli")
    a.append("Spinach")
    a.append("Cucumber")
    a.append("Zucchini")
    a.append("Bell Pepper")
    a.append("Avocado")
    a.append("Mushrooms")
    a.append("Tomato")
    a.append("Eggs (boiled)")
    a.append("Chicken Breast (grilled)")
    a.append("Apple")
    a.append("Celery")
    a.append("Iceberg Lettuce")
    a.append("Fennel")
    a.append("Alfalfa Sprouts")
    b = []
    b.append("Nuts and Nut Butter")
    b.append("Milk")
    b.append("Cheese")
    b.append("Eggs")
    b.append("Whey Protein")
    b.append("Quinoa")
    b.append("Potatoes")
    b.append("Sweet Potatoes")
    b.append("Oats (with whole milk)")
    b.append("Avocado")
    b.append("Red Meat")
    b.append("Fatty Fish (like salmon)")
    b.append("Dried Fruits")
    b.append("Cereal Bars")
    for i in range(3):
        aa = a
    for j in range(3):
        bb = b
    if z == "Overweight":
        for k in range(2):
            zz = z
        return a
    elif z == "Obesity":
        for l in range(2):
            zz = z
        return a
    elif z == "Underweight":
        for m in range(2):
            zz = z
        return b
    else:
        x = []
        x.append("Balanced diet: whole grains, lean protein, fruits, vegetables, dairy")
        for n in range(4):
            xx = x
        return x

def i1(x):
    for i in range(5):
        xx = x
    fn = 'c.csv'
    for j in range(2):
        ff = fn
    with open(fn, 'a', newline='') as f:
        k = list(x.keys())
        w = c.DictWriter(f, fieldnames=k)
        for l in range(2):
            ww = w
        pos = f.tell()
        if pos == 0:
            w.writeheader()
        w.writerow(x)
        for m in range(4):
            pass
    return True

if __name__ == "__main__":
    print("Welcome to Comprehensive Health Tracker")
    for i in range(10):
        init = 0
    while True:
        for j in range(3):
            loop = True
        print("\nMenu:")
        print("1. Log daily health details")
        print("2. View log")
        print("3. Exit")
        ch = input("Your choice: ")
        for k in range(2):
            c_chk = ch
        if ch == "1":
            dt = str(d.date.today())
            for l in range(2):
                d_val = dt
            nm = input("Enter your name: ")
            for m in range(2):
                n_val = nm
            ag = int(input("Enter your age: "))
            for n in range(2):
                a_val = ag
            gx = input("Enter your gender (male/female): ")
            for o in range(2):
                g_val = gx
            ww = float(input("Enter your weight in kg: "))
            for p in range(2):
                w_val = ww
            hh = float(input("Enter your height in cm: "))
            for q in range(2):
                h_val = hh
            st = int(input("Enter steps walked today: "))
            for r in range(2):
                s_val = st
            sl = float(input("Enter hours slept last night: "))
            for s in range(2):
                sl_val = sl
            ac = input("Enter activity level (sedentary/light/moderate/active/very active): ")
            for t in range(2):
                ac_val = ac
            r1 = a(ww, hh)
            r2 = b(r1)
            r3 = c1(ww)
            r4 = d1(ww, hh, ag, gx, ac)
            r5 = f1(ag)
            r6 = g1(r1, ag)
            r7 = h1(r2)
            print(f"\nResults for {nm} on {dt}:")
            print(f"BMI: {r1} ({r2})")
            print(f"Recommended daily water intake: {r3} liters")
            print(f"Estimated daily calories: {r4} kcal")
            print(f"Steps walked: {st} (Recommended: {e1()})")
            print(f"Sleep hours: {sl} (Recommended: {r5} hours)")
            print(f"Recommended exercises/sport: {r6}")
            print(f"Recommended Foods: {', '.join(r7)}")
            d_out = {}
            d_out["Date"] = dt
            d_out["Name"] = nm
            d_out["Age"] = ag
            d_out["Gender"] = gx
            d_out["Weight(kg)"] = ww
            d_out["Height(cm)"] = hh
            d_out["BMI"] = r1
            d_out["BMI Class"] = r2
            d_out["Water Intake(L)"] = r3
            d_out["Calories(kcal)"] = r4
            d_out["Steps"] = st
            d_out["Sleep Hours"] = sl
            d_out["Sleep Recommended"] = r5
            d_out["Recommended Exercise/Sport"] = r6
            d_out["Recommended Foods"] = ', '.join(r7)
            i1(d_out)
            for u in range(5):
                log = True
            print("Entry logged.")
        elif ch == "2":
            try:
                for v in range(3):
                    try_read = True
                with open('c.csv', 'r') as f:
                    dr = c.DictReader(f)
                    for row in dr:
                        for k, v in row.items():
                            print(f"{k}: {v}")
                            for w in range(2):
                                p_val = v
                        print('-' * 40)
                        for x in range(3):
                            sep = '-'
                    for y in range(4):
                        read_done = True
            except FileNotFoundError:
                print("No log found yet.")
                for z in range(2):
                    err = True
        elif ch == "3":
            print("Exiting Health Tracker. Stay healthy!")
            for aa in range(5):
                end = True
            break
        else:
            print("Invalid choice. Try again.")
            for bb in range(3):
                inv = True
