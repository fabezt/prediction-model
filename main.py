# This is a simple python script that shows how a chain of events can influence predictions.
import sys
import time
from pathlib import Path

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

BOOKS = {
    "A": ("harrypotter.txt", "Harry Potter"),
    "B": ("lordoftherings.txt", "Lord of the Rings"),
    "C": ("hungergames.txt", "Hunger Games"),
}


def pause(seconds=0.5):
    time.sleep(seconds)


def resource_path(name):
    base = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return Path(base) / name


def load_text(path):
    return Path(path).read_text(encoding="utf-8")


def bigrams(txt):
    return zip(txt, txt[1:])


def letter_counts(txt):
    return {letter: txt.count(letter) for letter in ALPHABET}


def vowel_consonant_transitions(txt):
    stats = {"VV": 0, "VC": 0, "CV": 0, "CC": 0}
    for first, second in bigrams(txt):
        if first in VOWELS:
            key = "VV" if second in VOWELS else "VC" if second in CONSONANTS else None
        elif first in CONSONANTS:
            key = "CV" if second in VOWELS else "CC" if second in CONSONANTS else None
        else:
            key = None
        if key is not None:
            stats[key] += 1
    return stats


def next_letter_counts(txt, letter):
    counts = {l: 0 for l in ALPHABET}
    for first, second in bigrams(txt):
        if first == letter and second in ALPHABET:
            counts[second] += 1
    return counts


def percentage(part, whole):
    return part / whole * 100 if whole else 0.0


def main():
    print("We will start a chain with a letter x.")
    pause()
    print("Now we want to guess what you will add to the chain.")
    pause()
    print("According to the Markov chain, only present states matter, not the future.")
    pause()
    print("So we know that your last addition to the chain was x.")
    pause()
    print("This will influence the next state of the chain.")
    pause()
    print("Now the odds of us guessing the right letter is P = 1/26 = 0.03846153846 (assuming 26 letters in the alphabet).")
    pause()
    print("Now we will add events to the chain that will influence the next state.")
    pause()

    choice = input("Let me ask you a question. Do you prefer A: Harry Potter or B: Lord of the Rings? or C: Hunger Games? ").strip().upper()
    print(choice)

    if choice not in BOOKS:
        print("Choose a valid option.")
        return

    if choice != "A":
        print(f"You chose {BOOKS[choice][1]}. This option is not implemented yet.")
        return

    filename, _ = BOOKS[choice]
    try:
        txt = load_text(resource_path(filename))
    except FileNotFoundError:
        print(f"Could not find {filename}. Please make sure the file exists next to this program.")
        return

    x_count = txt.count("x")
    t_after_x = sum(1 for first, second in bigrams(txt) if first == "x" and second == "t")

    print("So I took the Harry Potter text and calculated the probability of the next letter being an x.")
    pause()
    print(f"The text has {len(txt)} characters")
    pause()
    print("Now we want to know what character is most likely to come after another.")
    pause()
    print(f"First we will count how often each letter appears. In our case x appears {x_count} times")
    pause()
    print("Now we will check what the next letter is after an x.")
    pause()
    print(f"The letter t appears {percentage(t_after_x, x_count):.2f}% of the time after an x.")
    pause()
    print("So if you add an x to the chain, the next letter will most likely be a t, if you want to build an English word.")
    pause()
    print("Let's now say that x stands for a universal undefined variable.")
    pause()
    print("We would need a matrix of all letters and their probabilities to come after each other.")
    pause()

    counts = letter_counts(txt)
    vowels_count = sum(counts[v] for v in VOWELS)
    consonants_count = sum(counts[c] for c in CONSONANTS)

    print("We will use the text as a fixed point to calculate the probabilities of the next letter.")
    pause()
    print(f"Total vowels: {vowels_count}, Total consonants: {consonants_count}")
    pause()
    print("We have 4 options: Vowels-Vowels, Vowels-Consonants, Consonants-Vowels, Consonants-Consonants.")
    pause()

    stats = vowel_consonant_transitions(txt)
    print(f"Vowels-Vowels: {stats['VV']}, Consonants-Consonants: {stats['CC']}, Vowels-Consonants: {stats['VC']}, Consonants-Vowels: {stats['CV']}")
    pause()
    print("Depending on what the letter before the x is, we can calculate the probabilities of the next letter.")
    pause()

    letter = input("What letter do you want x to represent? (a-z): ").strip().lower()
    print(letter)

    if len(letter) != 1 or letter not in ALPHABET:
        print("Please enter a valid letter from a to z.")
        return

    occurrences = txt.count(letter)
    counts = next_letter_counts(txt, letter)
    total_followers = sum(counts.values())

    if occurrences == 0 or total_followers == 0:
        print(f"The letter '{letter}' never appears in the text, so no prediction can be made.")
        return

    if letter in CONSONANTS:
        print("The letter you chose is a consonant.")
        if stats["CC"] + stats["CV"]:
            cc = percentage(stats["CC"], stats["CC"] + stats["CV"])
            cv = percentage(stats["CV"], stats["CC"] + stats["CV"])
            print(f"The chance of Consonant-Consonant is: {cc:.2f} %")
            print(f"The chance of Consonant-Vowel is: {cv:.2f} %")
            print("So most likely the next letter will be a vowel." if stats["CV"] > stats["CC"] else "So most likely the next letter will be a consonant.")
    else:
        print("The letter you chose is a vowel.")
        if stats["VV"] + stats["VC"]:
            vv = percentage(stats["VV"], stats["VV"] + stats["VC"])
            vc = percentage(stats["VC"], stats["VV"] + stats["VC"])
            print(f"The chance of Vowel-Vowel is: {vv:.2f} %")
            print(f"The chance of Vowel-Consonant is: {vc:.2f} %")
            print("So most likely the next letter will be a consonant." if stats["VC"] > stats["VV"] else "So most likely the next letter will be a vowel.")

    next_letter = max(counts, key=counts.get)
    print(f"The letter most likely to come after your letter is: {next_letter} with {percentage(counts[next_letter], occurrences):.2f}%")
    pause(2)
    print("We just predicted the next letter, now we could rerun this process and eventually build a word.")


if __name__ == "__main__":
    main()
