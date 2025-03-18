""" UI's for the Killer Sudoku Helper """
import customtkinter as ctk
from logic import calculate_cage_possibilities

class KillerSudokuUI:
    """ UI class for the Killer Sudoku Helper """
    def __init__(self, root):
        self.root = root
        self.root.title("Killer Sudoku Helper")
        self.root.geometry("350x300")

        self.frame_cage_calculator = ctk.CTkFrame(self.root, border_width=5)
        self.frame_cage_calculator.pack(fill="both", expand=True)

        self.input_cage_sum = ctk.CTkEntry(
            self.frame_cage_calculator,
            width=80,
            placeholder_text="Cage Sum")
        self.input_cage_sum.pack(pady=20)

        #region Slider
        self.frame_slider = ctk.CTkFrame(self.frame_cage_calculator)
        self.frame_slider.pack()

        self.slider = ctk.CTkSlider(
            self.frame_slider,
            from_=1,
            to=9,
            number_of_steps=8,
            command=self.on_slider_change)
        self.slider.grid(row=0, column=0)
        self.slider.set(3)

        self.label_slider_value = ctk.CTkLabel(
            self.frame_slider,
            text="Cage Size: 3",
            font=("Arial", 14))
        self.label_slider_value.grid(row=0, column=1, padx=10)
        #endregion

        self.button_calculate = ctk.CTkButton(
            self.frame_cage_calculator,
            text="Calculate",
            width=80,
            command=self.on_calculate)
        self.button_calculate.pack(pady=20)

    def on_slider_change(self, value):
        """ Called when the slider value changes """
        slider_value = int(float(value))
        self.label_slider_value.configure(text=f"Cage Size: {slider_value}")

    def on_calculate(self):
        """ Calculate butonuna tıklandığında çağrılır """
        cage_sum = self.input_cage_sum.get()
        cage_size = int(float(self.slider.get()))
        calculate_cage_possibilities(cage_sum, cage_size)
