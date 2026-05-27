import customtkinter as ctk                          #modern styled tkinter replacement
from config import Config                            #brings in project settings                       
from core.depth_estimator import DepthEstimator      #brings in the AI class
from core.blur_engine import BlurEngine              #brings in the blur math class
from core.processor import ImageProcessor            #brings in the orchestrator class
from ui.main_window import DefocusAppUI              #brings in the actual user interface window design

def main():
    print(f"--- Starting {Config.PROJECT_NAME} ---")   #prints a welcome message in the hidden terminal, confirming the program has started
    
    ctk.set_appearance_mode("dark")                    #sets the global look to dark mode
    ctk.set_default_color_theme("blue")                #sets the accent color theme to blue
    
    root = ctk.CTk()                                   #creates the main CustomTkinter window with dark-mode support
    
    # to initialize core engines
    depth_estimator = DepthEstimator(model_type=Config.MODEL_TYPE)     #creates a live object of your AI
    blur_engine = BlurEngine()                                         #creates a live object of your blurring tool
    
    #to initialize controller (the processor)
    processor = ImageProcessor(depth_estimator, blur_engine)           #creates the processor and hands it the AI and the blur engine so it can coordinate between them
    
    # to Launch UI
    app = DefocusAppUI(root, processor) #it takes the blank root window and draws all your sliders and buttons on it 
                                        #it also gives the interface access to the processor so buttons actually do something when clicked
    
    root.mainloop()                     #infinite loop it keeps the visual window open on your screen and listens for mouse clicks

if __name__ == "__main__":    #python check (Was this file run directly by the user, or was it imported by another file?)
    main()