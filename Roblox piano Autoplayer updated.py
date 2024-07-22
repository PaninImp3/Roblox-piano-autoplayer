import keyboard
import time

# Define the melody and cooldown
melody = '[tf][ua][of][ua][of][ua][tf][ua][of][ua][of][ua][ep][To][ua]T[uo][Tp][ed][TS][ud][Tf][uS][Tp][qf][ep][tf][ep][tf][ep][qf][WO][tf][WO][tg][W][tf][us][of][us][od][uf][rd][y][os][y][oa][y][tf][ua][of][ua][of][ua][tf][ua][of][ua][of][ua][ep][To][ua][T][uo][Tp][ed][TS][ud][Tf][uS][Tp][qf][ep][tf][ep][tf][ep][qf][WO][tf][WO][tg][W][tf][us][of][us][od][uf][ra][u][of][u][oa][y][is][t][i][to][ip][ua][ys][r][ua][w][es][r][yo][u][r][up][ro][qi][wu][r][uf][t][id][u][es][t][u][to][up][ea][ws][r][ya][r][us][O][pf][u][y][eg][tf][id][os][u][yd][t][ya][u][is][t][i][to][ip][ua][ys][r][ua][w][es][r][yo][u][r][up][ro][qi][wu][r][uf][t][id][u][es][t][u][to][up][ea][ws][r][ya][r][us][O][pf][us][pf][us][pd][uf][od][y][os][y][oa][y][to][uo][uo][th][uo][uo][rd][yo][yo][r][yo][yo][es][tu][tu][eh][tu][tu][wo][ry][ry][w][ry][ry][qo][et][et][qs][et][et][0h][wt][wt][0][wt][wtj][9h][qe][qe][9d][qe][qe][ws][ry][ry][w][ry][ry][to][uo][uo][th][uo][uo][rd][yo][yo][r][yo][yo][es][tu][tu][eh][tu][tu][wo][ry][ry][w][ry][ry][qo][et][et][qs][et][et][0h][wt][wt][0][wt][wtj][9h][qe][qe][9d][qe][qe][ws][ry][ry][w][ry][ry][qo][et][et][qh][et][etf][qd][et][ets][qa][et][ets][0d][wr][wr][0k][wrJ][wrj][0h][wr][wr][0][wr][wr][9p][qe][qe][9h][qe][qef][wd][ry][rys][wd][ry][ryf][Wa][ry][ry][Wd][ry][ry][ed][tu][uos][wa][ry][yos][qo][et][et][qh][et][etf][qd][et][ets][qa][et][ets][0d][wr][wr][0k][wrJ][wrj][0h][wr][wr][0][wr][wr][9p][qe][qe][9h][qe][qef][wd][ry][rys][wd][ry][ryf][Wa][ry][ry][Wd][ry][ry][ed][tu][uos][wa][ry][yos][8o][t][y][t][Q][t][y][t][q][t][y][i][8u][y][t][w][8o][t][y][t][Q][t][y][t][q][t][y][i][8u][y][t][w][qo][t][y][t][w][t][y][u][y][wt]'
cooldown = 0.005 # DONT CHANGE

# Function to play the melody
def play_melody(melody, cooldown):
    for note in melody:
        if note == '[':
            note = next(melody, None)
            chord = ''
            while note != ']':
                chord += note
                note = next(melody, None)
            # Play chord
            for char in chord:
                if char.isupper():
                    keyboard.press('shift')
                keyboard.press(char.lower())
                if char.isupper():
                    keyboard.release('shift')
            time.sleep(cooldown)
            for char in chord:
                keyboard.release(char.lower())
            print(f"Played chord: {chord}")
        elif note.isupper():
            # Play capital letter note with shift
            keyboard.press('shift')
            keyboard.press_and_release(note.lower())
            keyboard.release('shift')
            print(f"Played note with shift: {note}") # Debug
        else:
            # Play single note
            keyboard.press_and_release(note)
            print(f"Played note: {note}") # Debug
        # Wait for ';' key press to play the next note
        keyboard.wait(';')
        time.sleep(cooldown)

# Wait for user to press the play button (space bar)
print("Press the enter to start playing the melody...")
keyboard.wait('Enter')

# Play the melody
play_melody(iter(melody), cooldown)
