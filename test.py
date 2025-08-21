from pathlib import Path

txt = Path("harrypotter.txt").read_text(encoding="utf-8")
total_chars = len(txt)
Pa = txt.count("a") / total_chars
print(f"Probability of 'a': {Pa:.4f}")