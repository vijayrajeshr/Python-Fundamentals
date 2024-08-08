import sys

def word_count(text):
  words = text.split()
  return len(words)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python script.py <text>")
    sys.exit(1)
  
  text = sys.argv[1]
  word_count = word_count(text)
  print("Word count:", word_count)
