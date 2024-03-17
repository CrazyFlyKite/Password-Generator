from tkinter import PhotoImage

from customtkinter import CTk, CTkLabel, CTkButton, CTkCheckBox, CTkFrame, BooleanVar, StringVar, CTkFont, CENTER, LEFT

from utilities import *


class App:
	def __init__(self) -> None:
		self.root = CTk()

		# Variables
		self.length_variable = StringVar(value=str(DEFAULT_LENGTH))
		self.checkbox_variables: List[BooleanVar] = []
		self.output_variable = StringVar(value=self.generate_password())

		self.current_password = self.output_variable.get()

	def setup_window(self) -> None:
		self.root.wm_title(WINDOW_TITLE)
		self.root.wm_geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
		self.root.wm_resizable(WINDOW_RESIZABLE, WINDOW_RESIZABLE)
		self.root.wm_iconphoto(True, PhotoImage(file=WINDOW_ICON))

	def setup_ui(self) -> None:
		# Font
		title_font: CTkFont = CTkFont(size=17, weight='bold')
		password_font: CTkFont = CTkFont(family=PASSWORD_FONT, size=22, weight='bold')

		# Length
		CTkLabel(self.root, text='Length', font=title_font).pack(pady=5)

		length_frame: CTkFrame = CTkFrame(self.root)
		length_frame.pack()

		CTkButton(length_frame, text='-', width=30, command=self.decrease_length).pack(side=LEFT, padx=5)
		CTkNumberEntry(length_frame, width=60, justify=CENTER, textvariable=self.length_variable).pack(side=LEFT)
		CTkButton(length_frame, text='+', width=30, command=self.increase_length).pack(side=LEFT, padx=5, pady=5)

		# Include
		CTkLabel(self.root, text='Include', font=title_font).pack(pady=(10, 0))

		include_frame: CTkFrame = CTkFrame(self.root)
		include_frame.pack()

		for text in INCLUDE_CATEGORIES:
			variable: BooleanVar = BooleanVar(value=True)
			CTkCheckBox(
				include_frame,
				text=text.title(),
				variable=variable,
				checkbox_width=20,
				checkbox_height=20,
			).pack(padx=4, pady=5, side='top')
			self.checkbox_variables.append(variable)

		# Generate button
		CTkButton(
			self.root, text='Generate',
			command=lambda: self.change_password(self.generate_password())
		).pack(pady=15)

		# Output
		output_frame: CTkFrame = CTkFrame(self.root)
		output_frame.pack(pady=10)

		CTkLabel(output_frame, textvariable=self.output_variable, font=password_font).pack(padx=10, side=LEFT)
		CTkButton(output_frame, text='Copy', width=20, command=self.copy_password).pack(side=LEFT, padx=5, pady=5)

	def increase_length(self) -> None:
		try:
			self.length_variable.set(str(int(self.length_variable.get()) + 1))
		except ValueError:
			self.length_variable.set('1')

	def decrease_length(self) -> None:
		try:
			self.length_variable.set(str(int(self.length_variable.get()) - 1))
		except ValueError:
			self.length_variable.set('0')

	def generate_password(self) -> Optional[str]:
		try:
			length: int = int(self.length_variable.get())
		except ValueError:
			self.output_variable.set(INVALID_INPUT_MESSAGE)
			return

		includes: List[bool] = [variable.get() for variable in self.checkbox_variables]

		return generate_password(length, *includes)

	def change_password(self, password: str) -> None:
		self.current_password = password

		if not password:
			self.output_variable.set(INVALID_INPUT_MESSAGE)
		elif len(password) >= 30:
			self.output_variable.set(f'{password[:4]}...{password[-4:]}')
		else:
			self.output_variable.set(password)

		logging.info(f'Generated new password: {password}')

	def copy_password(self) -> None:
		if self.current_password:
			copy_to_clipboard(self.current_password)
			logging.info(f'Copied password: {self.current_password}')
		else:
			logging.info('No password to copy!')

	def run(self) -> None:
		self.setup_window()
		self.setup_ui()
		self.root.mainloop()
