from gui_new import gui_output
from itertools import product

combinations = list(product(*gui_output))
print(combinations)