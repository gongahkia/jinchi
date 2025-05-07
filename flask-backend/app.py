# ----- required imports -----

import tempfile
import os
import uuid
import sys
import pygame
from flask import Flask, request, send_file, jsonify
from src.core import GarudaScene
from src.render import CodeObject, LegalObject
from src.effects import TypewriterEffect
from src.parsers import CodeParser, LegalParser

# ----- initialization code -----

app = Flask(__name__)

# ----- flask routes -----


@app.route("/animate", methods=["POST"])
def animate_text():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    uploaded_file = request.files["file"]
    if uploaded_file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_type = request.form.get("type", "code")
    language = request.form.get("language", "python")
    style = request.form.get("style", "monokai")
    run_time = float(request.form.get("run_time", "2"))

    temp_dir = tempfile.mkdtemp()
    file_id = str(uuid.uuid4())
    input_path = os.path.join(temp_dir, f"input_{file_id}.txt")
    output_path = os.path.join(temp_dir, f"output_{file_id}.mp4")

    try:
        uploaded_file.save(input_path)

        with open(input_path, "r", encoding="utf-8") as f:
            text_content = f.read()

        pygame.init()
        scene = GarudaScene()

        if file_type == "code":
            CodeParser().parse(text_content)
            text_obj = CodeObject(text_content, language=language, style=style)
        elif file_type == "legal":
            LegalParser().parse(text_content)
            text_obj = LegalObject(text_content, style=style)
        else:
            return jsonify({"error": "Invalid file type. Use 'code' or 'legal'"}), 400

        scene.add(text_obj)
        scene.play(TypewriterEffect(text_obj), run_time=run_time)
        scene.recorder.export(output_path)

        return send_file(
            output_path,
            mimetype="video/mp4",
            as_attachment=True,
            download_name=f"animation_{file_id}.mp4",
        )

    except Exception as e:
        app.logger.error(f"Animation failed: {str(e)}")
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
        pygame.quit()


# ----- execution code -----

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
