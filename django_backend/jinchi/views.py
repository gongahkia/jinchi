from django.shortcuts import render
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from src.core import GarudaScene
from src.render import CodeObject, LegalObject
from src.effects import TypewriterEffect
import tempfile, os, uuid


class AnimationAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        uploaded_file = request.FILES["file"]
        file_type = request.data.get("type", "code")
        style = request.data.get("style", "monokai")

        temp_dir = tempfile.mkdtemp()
        file_id = str(uuid.uuid4())
        output_path = os.path.join(temp_dir, f"output_{file_id}.mp4")

        try:
            text_content = uploaded_file.read().decode("utf-8")

            scene = GarudaScene()
            if file_type == "code":
                obj = CodeObject(text_content, style=style)
            else:
                obj = LegalObject(text_content, style=style)

            scene.add(obj)
            scene.play(TypewriterEffect(obj), run_time=2)
            scene.recorder.export(output_path)

            return FileResponse(
                open(output_path, "rb"),
                content_type="video/mp4",
                as_attachment=True,
                filename=f"animation_{file_id}.mp4",
            )

        finally:
            if os.path.exists(output_path):
                os.remove(output_path)
