# PTABLE.py -- Periodic Table Explorer
# Target : TI-84 Evo (TI CircuitPython build)
# Imports: none required
# Notes  : no f-strings (TI Python builds reject them), no file I/O.
#
# Electron configurations are COMPUTED from Z using the
# Madelung (n+l) rule. No configuration is stored in this file.

WIDTH = 30
ORB = "spdfgh"

# EL[Z-1] = (symbol, name, standard atomic mass)
EL = [
    ("H", "Hydrogen", 1.008),       ("He", "Helium", 4.0026),
    ("Li", "Lithium", 6.94),        ("Be", "Beryllium", 9.0122),
    ("B", "Boron", 10.81),          ("C", "Carbon", 12.011),
    ("N", "Nitrogen", 14.007),      ("O", "Oxygen", 15.999),
    ("F", "Fluorine", 18.998),      ("Ne", "Neon", 20.180),
    ("Na", "Sodium", 22.990),       ("Mg", "Magnesium", 24.305),
    ("Al", "Aluminum", 26.982),     ("Si", "Silicon", 28.085),
    ("P", "Phosphorus", 30.974),    ("S", "Sulfur", 32.06),
    ("Cl", "Chlorine", 35.45),      ("Ar", "Argon", 39.948),
    ("K", "Potassium", 39.098),     ("Ca", "Calcium", 40.078),
    ("Sc", "Scandium", 44.956),     ("Ti", "Titanium", 47.867),
    ("V", "Vanadium", 50.942),      ("Cr", "Chromium", 51.996),
    ("Mn", "Manganese", 54.938),    ("Fe", "Iron", 55.845),
    ("Co", "Cobalt", 58.933),       ("Ni", "Nickel", 58.693),
    ("Cu", "Copper", 63.546),       ("Zn", "Zinc", 65.38),
    ("Ga", "Gallium", 69.723),      ("Ge", "Germanium", 72.630),
    ("As", "Arsenic", 74.922),      ("Se", "Selenium", 78.971),
    ("Br", "Bromine", 79.904),      ("Kr", "Krypton", 83.798),
    ("Rb", "Rubidium", 85.468),     ("Sr", "Strontium", 87.62),
    ("Y", "Yttrium", 88.906),       ("Zr", "Zirconium", 91.224),
    ("Nb", "Niobium", 92.906),      ("Mo", "Molybdenum", 95.95),
    ("Tc", "Technetium", 98.0),     ("Ru", "Ruthenium", 101.07),
    ("Rh", "Rhodium", 102.91),      ("Pd", "Palladium", 106.42),
    ("Ag", "Silver", 107.87),       ("Cd", "Cadmium", 112.41),
    ("In", "Indium", 114.82),       ("Sn", "Tin", 118.71),
    ("Sb", "Antimony", 121.76),     ("Te", "Tellurium", 127.60),
    ("I", "Iodine", 126.90),        ("Xe", "Xenon", 131.29),
    ("Cs", "Cesium", 132.91),       ("Ba", "Barium", 137.33),
    ("La", "Lanthanum", 138.91),    ("Ce", "Cerium", 140.12),
    ("Pr", "Praseodymium", 140.91), ("Nd", "Neodymium", 144.24),
    ("Pm", "Promethium", 145.0),    ("Sm", "Samarium", 150.36),
    ("Eu", "Europium", 151.96),     ("Gd", "Gadolinium", 157.25),
    ("Tb", "Terbium", 158.93),      ("Dy", "Dysprosium", 162.50),
    ("Ho", "Holmium", 164.93),      ("Er", "Erbium", 167.26),
    ("Tm", "Thulium", 168.93),      ("Yb", "Ytterbium", 173.05),
    ("Lu", "Lutetium", 174.97),     ("Hf", "Hafnium", 178.49),
    ("Ta", "Tantalum", 180.95),     ("W", "Tungsten", 183.84),
    ("Re", "Rhenium", 186.21),      ("Os", "Osmium", 190.23),
    ("Ir", "Iridium", 192.22),      ("Pt", "Platinum", 195.08),
    ("Au", "Gold", 196.97),         ("Hg", "Mercury", 200.59),
    ("Tl", "Thallium", 204.38),     ("Pb", "Lead", 207.2),
    ("Bi", "Bismuth", 208.98),      ("Po", "Polonium", 209.0),
    ("At", "Astatine", 210.0),      ("Rn", "Radon", 222.0),
    ("Fr", "Francium", 223.0),      ("Ra", "Radium", 226.0),
    ("Ac", "Actinium", 227.0),      ("Th", "Thorium", 232.04),
    ("Pa", "Protactinium", 231.04), ("U", "Uranium", 238.03),
    ("Np", "Neptunium", 237.0),     ("Pu", "Plutonium", 244.0),
    ("Am", "Americium", 243.0),     ("Cm", "Curium", 247.0),
    ("Bk", "Berkelium", 247.0),     ("Cf", "Californium", 251.0),
    ("Es", "Einsteinium", 252.0),   ("Fm", "Fermium", 257.0),
    ("Md", "Mendelevium", 258.0),   ("No", "Nobelium", 259.0),
    ("Lr", "Lawrencium", 262.0),    ("Rf", "Rutherfordium", 267.0),
    ("Db", "Dubnium", 270.0),       ("Sg", "Seaborgium", 269.0),
    ("Bh", "Bohrium", 270.0),       ("Hs", "Hassium", 270.0),
    ("Mt", "Meitnerium", 278.0),    ("Ds", "Darmstadtium", 281.0),
    ("Rg", "Roentgenium", 282.0),   ("Cn", "Copernicium", 285.0),
    ("Nh", "Nihonium", 286.0),      ("Fl", "Flerovium", 289.0),
    ("Mc", "Moscovium", 290.0),     ("Lv", "Livermorium", 293.0),
    ("Ts", "Tennessine", 294.0),    ("Og", "Oganesson", 294.0),
]

# Z of elements whose MEASURED ground-state configuration departs
# from strict Aufbau filling. Only the Z values live here -- the
# real configurations are deliberately not hardcoded, so this is
# only ever shown as a caution flag, never as an answer.
EXCEPTIONS = (24, 29, 41, 42, 44, 45, 46, 47, 57, 58, 64,
              78, 79, 89, 90, 91, 92, 93, 96, 103)


def aufbau_order(smax=12):
    """Subshells as (n, l) tuples in Madelung filling order.

    Ordered by increasing n+l, ties broken by increasing n.
    That rule reproduces exactly:
    1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p
    """
    out = []
    for s in range(1, smax + 1):        # s = n + l
        for n in range(1, s + 1):       # n ascending -> l descending
            l = s - n
            if 0 <= l < n:              # l must satisfy 0 <= l <= n-1
                out.append((n, l))
    return out


ORDER = aufbau_order()


def configure(z):
    """Drop z electrons into ORDER. -> [(n, l, count), ...]"""
    shells = []
    left = z
    for (n, l) in ORDER:
        if left <= 0:
            break
        cap = 4 * l + 2                 # 2(2l+1)
        put = cap
        if left < cap:
            put = left
        shells.append((n, l, put))
        left -= put
    return shells


def config_text(shells):
    parts = []
    for (n, l, c) in shells:
        parts.append("{}{}{}".format(n, ORB[l], c))
    return " ".join(parts)


def valence(shells):
    """Electrons in the outermost shell, plus any partly filled
    inner d/f subshell (the usual transition-metal convention).
    Reproduces the group number for the main group and d block."""
    nmax = 0
    for (n, l, c) in shells:
        if n > nmax:
            nmax = n
    v = 0
    for (n, l, c) in shells:
        if n == nmax:
            v += c
        elif l >= 2 and c < 4 * l + 2:
            v += c
    return v


def open_f_block(shells):
    for (n, l, c) in shells:
        if l == 3 and c < 14:
            return True
    return False


def wrap(text, width=WIDTH):
    """Break a space-separated string into screen-width lines."""
    lines = []
    cur = ""
    for w in text.split(" "):
        if cur == "":
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur = cur + " " + w
        else:
            lines.append(cur)
            cur = w
    if cur != "":
        lines.append(cur)
    return lines


def find(query):
    """Accept an atomic number, a symbol, or a full name.
    Returns Z, or None if nothing matches."""
    q = query.strip()
    if q == "":
        return None
    try:
        z = int(q)
        if 1 <= z <= len(EL):
            return z
        return None
    except ValueError:
        pass
    q = q.lower()
    for i in range(len(EL)):
        if EL[i][0].lower() == q:
            return i + 1
    for i in range(len(EL)):
        if EL[i][1].lower() == q:
            return i + 1
    return None


def show(z):
    sym, name, mass = EL[z - 1]
    shells = configure(z)
    print("-" * WIDTH)
    print("Sym   : " + sym)
    print("Name  : " + name)
    print("Z     : {}".format(z))
    print("Mass  : {} amu".format(mass))
    print("Val e-: {}".format(valence(shells)))
    print("Config (Aufbau fill order):")
    for line in wrap(config_text(shells)):
        print("  " + line)
    if z in EXCEPTIONS:
        print("! Z={} is a known Aufbau".format(z))
        print("  exception - the measured")
        print("  config differs. Check text.")
    if open_f_block(shells):
        print("! f-block: valence count is")
        print("  convention-dependent.")
    print("-" * WIDTH)


def show_order():
    """Print the filling order as far as the known elements go,
    i.e. until the running capacity covers the whole table."""
    print("-" * WIDTH)
    print("Aufbau filling order:")
    row = ""
    total = 0
    for (n, l) in ORDER:
        item = "{}{}".format(n, ORB[l])
        if len(row) + len(item) + 1 > WIDTH:
            print(row)
            row = ""
        if row == "":
            row = item
        else:
            row = row + " " + item
        total += 4 * l + 2
        if total >= len(EL):
            break
    if row != "":
        print(row)
    print("(fills through Z={})".format(total))
    print("-" * WIDTH)


def main():
    print("PERIODIC TABLE EXPLORER")
    print("Elements 1-{}".format(len(EL)))
    while True:
        print("")
        print("1) Look up element")
        print("2) Show Aufbau order")
        print("3) Quit")
        choice = input("Choice: ").strip()
        if choice == "1":
            z = find(input("Z, symbol or name: "))
            if z is None:
                print("! Not found. Try 26, Fe or Iron.")
            else:
                show(z)
        elif choice == "2":
            show_order()
        elif choice == "3":
            print("Bye.")
            return
        else:
            print("! Pick 1, 2 or 3.")


main()
