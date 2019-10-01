# Concordance
This program uses hash tables to process a textual data file to generate a word concordance with line numbers for each main word.

Include these lines of code at the bottom of the concordance.py file:
con = Concordance()
con.load_stop_table('stop_words.txt')
con.load_concordance_table('in_file_name.txt')
con.write_concordance('out_file_name.txt')

```
python3 huffman.py
```

If you don't have version 3 of python, you can download it here: https://www.python.org/downloads/



