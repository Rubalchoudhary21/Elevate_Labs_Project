import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
import re
import math
import argparse
from zxcvbn import zxcvbn
import itertools

# Leetspeak map
LEET_MAP = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
}

# Entropy calculation
def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^\w\s]", password):
        charset += 32
    if charset == 0:
        return 0
    return round(len(password) * math.log2(charset), 2)

# Recommendations
def get_recommendations(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters.")
    if not re.search(r"[0-9]", password):
        suggestions.append("Include digits.")
    if not re.search(r"[^\w\s]", password):
        suggestions.append("Use special characters.")
    return suggestions

# Leet variants generator
def leet_variants(word):
    pools = [LEET_MAP.get(c.lower(), [c]) for c in word]
    return set(''.join(combo) for combo in itertools.product(*pools))

# Enhanced wordlist generator
def generate_wordlist(inputs, append_years=True):
    base_words = set()
    for i in inputs:
        base_words.update(leet_variants(i))

    combinations = set(base_words)

    # Common patterns to append/prepend
    special_patterns = ["!", "@", "#", "123", "_", "1", "12", "!@#", "321"]

    # Append years
    if append_years:
        for bw in base_words:
            for y in range(1990, 2025):
                combinations.add(f"{bw}{y}")

    # Append/prepend special characters and digits
    extended = set()
    for bw in base_words:
        for p in special_patterns:
            extended.add(f"{bw}{p}")
            extended.add(f"{p}{bw}")

    combinations.update(extended)

    return sorted(combinations)

# GUI
def launch_gui():
    def check_strength(event=None):
        pwd = entry.get()
        entropy = calculate_entropy(pwd)
        zx = zxcvbn(pwd)
        score = zx['score']
        progress['value'] = min(entropy, 100)
        if entropy < 28:
            label = "Very Weak 😟"
            style = "red.Horizontal.TProgressbar"
        elif entropy < 36:
            label = "Weak 🙁"
            style = "orange.Horizontal.TProgressbar"
        elif entropy < 60:
            label = "Moderate 😐"
            style = "yellow.Horizontal.TProgressbar"
        elif entropy < 80:
            label = "Strong 🙂"
            style = "blue.Horizontal.TProgressbar"
        else:
            label = "Very Strong 💪"
            style = "green.Horizontal.TProgressbar"
        remark.set(f"{label} (Entropy {entropy}, zxcvbn score {score}/4)")
        progress.configure(style=style)

        recs = get_recommendations(pwd)
        if pwd:
            recommend_text.set("Suggestions:\n- " + "\n- ".join(recs) if recs else "Great password!")
        else:
            recommend_text.set("")

    def toggle_visibility():
        if entry.cget('show') == '':
            entry.config(show='*')
            toggle.config(text='Show')
        else:
            entry.config(show='')
            toggle.config(text='Hide')

    def export_wordlist():
        inputs = simpledialog.askstring("Inputs", "Enter words separated by commas (name, pet, etc.):")
        if not inputs:
            return
        wordlist = generate_wordlist([i.strip() for i in inputs.split(',')])

        # Create new window to display the wordlist
        top = tk.Toplevel(root)
        top.title("Generated Wordlist")
        top.geometry("400x400")

        tk.Label(top, text="Generated Wordlist:", font=("Arial", 12, "bold")).pack(pady=5)

        # Scrollable Text widget
        text_widget = tk.Text(top, wrap="none", font=("Courier", 10))
        text_widget.pack(expand=True, fill="both")

        text_widget.insert("1.0", "\n".join(wordlist))
        text_widget.config(state="disabled")  # Make read-only

        # Scrollbar
        yscroll = tk.Scrollbar(top, command=text_widget.yview)
        yscroll.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=yscroll.set)

        # Optional save button
        def save_wordlist():
            filename = filedialog.asksaveasfilename(defaultextension=".txt")
            if filename:
                with open(filename, 'w') as f:
                    f.write("\n".join(wordlist))
                messagebox.showinfo("Saved", f"Wordlist saved to {filename}")

        tk.Button(top, text="Save to File", command=save_wordlist).pack(pady=5)

    root = tk.Tk()
    root.title("Password Strength Checker + Wordlist Generator")
    root.geometry("500x350")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("red.Horizontal.TProgressbar", background='red')
    style.configure("orange.Horizontal.TProgressbar", background='orange')
    style.configure("yellow.Horizontal.TProgressbar", background='gold')
    style.configure("blue.Horizontal.TProgressbar", background='skyblue')
    style.configure("green.Horizontal.TProgressbar", background='green')

    tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
    entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
    entry.pack()
    entry.bind("<KeyRelease>", check_strength)

    toggle = tk.Button(root, text="Show", command=toggle_visibility)
    toggle.pack(pady=5)

    progress = ttk.Progressbar(root, length=400, mode='determinate', maximum=100)
    progress.pack(pady=5)

    remark = tk.StringVar(value="Enter a password to check!")
    tk.Label(root, textvariable=remark, font=("Arial", 12)).pack()

    recommend_text = tk.StringVar()
    tk.Label(root, textvariable=recommend_text, font=("Arial", 10), fg="gray").pack(pady=5)

    tk.Button(root, text="Generate Wordlist", command=export_wordlist).pack(pady=5)

    root.mainloop()

# CLI
def cli_mode(args):
    pwd = args.password
    entropy = calculate_entropy(pwd)
    zx = zxcvbn(pwd)
    score = zx['score']

    print(f"\nAnalyzing password: {pwd}")
    print(f"Entropy: {entropy}")
    print(f"zxcvbn score: {score}/4")

    recs = get_recommendations(pwd)
    if recs:
        print("\nRecommendations:")
        for r in recs:
            print(f"- {r}")
    else:
        print("\nGreat password!")

    if args.wordlist:
        print("\nGenerating wordlist...")
        wordlist = generate_wordlist(args.wordlist.split(','))
        with open(args.output, 'w') as f:
            f.write("\n".join(wordlist))
        print(f"Wordlist saved to {args.output}")

# Main entry
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Strength Analyzer and Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--wordlist", help="Comma-separated words for custom wordlist")
    parser.add_argument("--output", help="Output file for generated wordlist")
    args = parser.parse_args()

    if args.password:
        cli_mode(args)
    else:
        launch_gui()
