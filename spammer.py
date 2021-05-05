import csv, pyautogui, time
time.sleep(5)
with open("pokemon.txt", "r") as file:
    csv_reader = csv.reader(file, delimiter = ",")
    for line in csv_reader:
        pyautogui.typewrite(line[1])
        pyautogui.press("enter")
