from pathlib import Path
from PIL import Image
import hashlib
import json

BASE_DIR = Path(__file__).resolve().parent
image_path = BASE_DIR / "evidence" / "oppenheimer.jpg"
report_path = BASE_DIR / "reports" / "evidence.json"

with Image.open(image_path) as image:
    image_format = image.format
    width, height = image.size

    sha256 = hashlib.sha256(
    image_path.read_bytes()
    ).hexdigest()

    evidence = {
    "subject": "J. Robert Oppenheimer",
    "file_name": image_path.name,
    "format": image_format,
    "dimensions": [width, height],
    "sha256": sha256,
    "source_url": "https://commons.wikimedia.org/wiki/File:JROppenheimer-LosAlamos.jpg",
    "claimed_date": "circa 1944",
    "photographer": None,
    "verification_status": "unverified"
    }

    report_path.parent.mkdir(exist_ok=True)

    report_path.write_text(
    json.dumps(evidence, indent=4),
    encoding="utf-8"
    )

    print("Evidence report created:", report_path)
