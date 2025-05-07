from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.custom import Custom
from diagrams.generic.device import Mobile
from diagrams.programming.language import Python
from diagrams.onprem.client import User

MP4_ICON = "mp4.png"

with Diagram("Jinchi Architecture", show=False, direction="LR"):
    user = User("User\n(provides input file)")
    with Cluster("Jinchi Engine Core"):
        main_script = Python("main.py\nCLI Entry Point")
        parsers = Python("parsers.py\nCode/Legal Text Parser")
        core = Python("core.py\nScene Manager")
        effects = Python("effects.py\nAnimation Effects")
        render = Python("render.py\nSyntax Highlighting\n& Text Rendering")
        exporter = Python("exporter.py\nVideo Encoding")
        mp4_output = Custom("demo.mp4", MP4_ICON)
    (
        user
        >> Edge(label="1. Runs script\nwith input file", color="darkgreen")
        >> main_script
    )
    main_script >> Edge(label="2. Calls parser", style="dashed") >> parsers
    parsers >> Edge(label="3. Returns\nstructured data") >> core
    core >> Edge(label="4. Applies\nanimation effects") >> effects
    core >> Edge(label="5. Renders\nframe content") >> render
    core >> Edge(label="6. Exports\nfinal video") >> exporter
    exporter >> Edge(label="7. Generates", color="firebrick") >> mp4_output
    effects - Edge(style="invis") - render
    render - Edge(style="invis") - exporter
