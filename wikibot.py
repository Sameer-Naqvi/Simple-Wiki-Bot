import ctypes
import wikipedia as wiki
print("Please enter the wikipedia page for which you would like a summary: ")
word = input()
info = wiki.summary(word, auto_suggest=False)
ctypes.windll.user32.MessageBoxW(
    0, info[:1000], word, 0
)