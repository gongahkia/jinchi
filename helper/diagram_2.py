from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.programming.language import Python
from diagrams.onprem.client import User

FLASK_ICON = "flask.png"
MP4_ICON = "mp4.png"

with Diagram("Jinchi Flask API Architecture", show=False, direction="LR"):
    user = User("User")
    api = Custom("\n\nFlask API\n(POST /animate)", FLASK_ICON)
    with Cluster("Jinchi Engine Core"):
        with Cluster("Processing Pipeline"):
            parsers = Python("parsers.py\n(Code/Legal Analysis)")
            core = Python("core.py\nScene Management")
            effects = Python("effects.py\nAnimation Logic")
            render = Python("render.py\nText Rendering")
        with Cluster("Export System"):
            exporter = Python("exporter.py\nFrame Capture")
            mp4_output = Custom("demo.mp4", MP4_ICON)
    user >> Edge(label="1. POST file & metadata", color="darkgreen") << api
    api >> Edge(label="2. Process request") >> parsers
    parsers >> Edge(label="3. Structured data") >> core
    core >> Edge(label="4. Apply effects") >> effects
    effects >> Edge(label="5. Render frames") >> render
    render >> Edge(label="6. Capture frames") >> exporter
    exporter >> Edge(label="7. Encode video", color="firebrick") >> mp4_output
    mp4_output >> Edge(label="8. Return MP4", color="blue") >> user
    parsers - Edge(style="invis") - effects
    core - Edge(style="invis") - exporter
