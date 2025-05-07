from core import GarudaScene
from render import CodeObject
from effects import TypewriterEffect

def main():
    scene = GarudaScene()
    code = CodeObject("def hello():\n    print('Garuda!')", "python", style="monokai")
    scene.add(code)
    scene.play(TypewriterEffect(code), run_time=2)
    scene.recorder.export("demo.mp4")

if __name__ == "__main__":
    main()