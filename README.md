
# Oppenheimer OSINT Investigation

An open-source intelligence case study investigating
the provenance of a historical photograph of
J. Robert Oppenheimer.

## Project Goals
- Investigate historical image attribution
- Extract image metadata using Python
- Generate a SHA-256 file fingerprint
- Document evidence in JSON
- Evaluate historical claims using OSINT methods

## Technologies
- Python
- Pillow
- hashlib
- JSON
- OSINT methodology

## Current Results
- Image format: JPEG
- Dimensions: 524 x 721 pixels
- SHA-256 successfully generated
- Historical attribution: under investigation

## Run

Install dependencies:

    python -m pip install Pillow

Run the analyzer:

    python main.py

Place the research image in `evidence/oppenheimer.jpg`
before running the script.

## Research Status
In progress. File metadata does not independently
verify the date, photographer, or authenticity
of the historical photograph.

## Next Steps
- Source provenance verification
- Image comparison
- Structured evidence reporting
- LLM-assisted analysis (planned)
