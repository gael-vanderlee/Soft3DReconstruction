from pathlib import Path

input_folder = (Path(__file__).parent / "inputs/").resolve()
image_1_path = input_folder / "teddy1.png"     # Pathlib path of the first image for manual override
image_2_path = input_folder / "teddy2.png"     # Pathlib path of the second image for manual override

output_folder = (Path(__file__).parent / "outputs/").resolve()
