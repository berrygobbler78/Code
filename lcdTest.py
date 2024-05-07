import board
import digitalio
lcd_rs = digitalio.DigitalInOut(board.D11)
lcd_en = digitalio.DigitalInOut(board.D12)
lcd_d7 = digitalio.DigitalInOut(board.D35)
lcd_d6 = digitalio.DigitalInOut(board.D33)
lcd_d5 = digitalio.DigitalInOut(board.D31)
lcd_d4 = digitalio.DigitalInOut(board.D29)

lcd_columns = 16
lcd_rows = 2

import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

lcd.message = "I love\n balls"