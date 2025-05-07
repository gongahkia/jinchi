import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", required=True)
    args = parser.parse_args()
    
    scene = GarudaScene()
    # Load input file and build scene
    renderer = PygameRenderer(scene)
    renderer.export_video(args.output)

if __name__ == "__main__":
    main()