import os
import utils

DISPLAY_RIGHT_TOP = (35, 455)
DISPLAY_LEFT_BOTTOM = (660, 1200)
SPLIT_LEVEL = 2

def cli_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def config_split_level():
    global SPLIT_LEVEL
    try:
        SPLIT_LEVEL = int(input("Enter SPLIT_LEVEL: "))
    except:
        pass

def main():
    while True:
        cli_clear()
        
        print("TOSS Hangul day Event")
        print(f"SPLIT_LEVEL: {SPLIT_LEVEL}")
        print("")
        print("1. Config SPLITE_LEVEL")
        print("2. Capture test")
        print("3. Run")
        print("4. Exit")
        print("")
        
        SEL_MENU = input("Select Menu: ")
        
        # Config SPLITE_LEVEL
        if SEL_MENU == '1':
            config_split_level()
            
        # Capture test
        if SEL_MENU == '2':
            utils.capture_screen_region(DISPLAY_RIGHT_TOP, DISPLAY_LEFT_BOTTOM, 'region_capture.png')
        
        # Run
        elif SEL_MENU == '3':
            utils.capture_screen_region(DISPLAY_RIGHT_TOP, DISPLAY_LEFT_BOTTOM, 'region_capture.png')
            utils.split_image('region_capture.png', SPLIT_LEVEL, 'splited')
            
            image_texts = []
            for image in os.listdir('splited'):
                image_text = utils.extract_text_from_image(os.path.join('splited', image))
                cleaned_text = image_text.replace(" ", "").replace("\n", "")
                info_dict = {
                    "name": image,
                    "text": cleaned_text
                }
                image_texts.append(info_dict)
                
            text_list = [info["text"] for info in image_texts]

            unique_text = utils.find_unique_item(text_list)

            for info in image_texts:
                if info["text"] == unique_text:
                    print(os.path.splitext((info["name"]))[0])
            
            input("Enter to continue . . .")
            
        # Exit
        elif SEL_MENU == '4':
            exit(0)
    
if __name__ == '__main__':        
    try:
        main()
    except KeyboardInterrupt:
        exit(0)