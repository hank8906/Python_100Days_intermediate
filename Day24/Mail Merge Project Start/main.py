
import os

output_folder = "./Output/ReadyToSend/"

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            content = letter.read()
            invite_name = name.strip()
            output_file_path = os.path.join(output_folder, f"{invite_name}.txt")
            with open(output_file_path, mode="w") as name_letter:
                final_letter = content.replace("[name]", f"{invite_name}")
                name_letter.write(f"{final_letter}")
