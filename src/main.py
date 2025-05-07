# ----- required imports -----

from core import GarudaScene
from render import CodeObject
from effects import TypewriterEffect
import pygame
import sys
import argparse

# ----- function definition -----


def main():
    parser = argparse.ArgumentParser(
        description="Garuda: Animated code/text visualizer"
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="input.txt",
        help="Input text file to visualize (default: input.txt)",
    )
    args = parser.parse_args()

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            code_text = f.read()
    except FileNotFoundError:
        print(f"File '{args.input_file}' not found.")
        return

    scene = GarudaScene()
    code = CodeObject(code_text, "python", style="monokai")
    scene.add(code)
    scene.play(TypewriterEffect(code), run_time=2)
    scene.recorder.export("demo.mp4")
    pygame.quit()
    sys.exit()


# ----- execution code -----

if __name__ == "__main__":
    main()
