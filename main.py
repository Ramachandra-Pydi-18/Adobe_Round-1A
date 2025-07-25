import fitz  # PyMuPDF
import os
import json

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []
    for i, page in enumerate(doc):
        blocks_on_page = page.get_text("dict")["blocks"]
        for block in blocks_on_page:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text:
                            blocks.append({
                                "text": text,
                                "size": span["size"],
                                "font": span["font"],
                                "page": i + 1
                            })
    return blocks

def assign_heading_levels(blocks):
    sizes = sorted(list(set(round(b["size"], 1) for b in blocks)), reverse=True)
    level_map = {}
    if len(sizes) >= 4:
        level_map = {sizes[0]: "title", sizes[1]: "H1", sizes[2]: "H2", sizes[3]: "H3"}
    elif len(sizes) == 3:
        level_map = {sizes[0]: "title", sizes[1]: "H1", sizes[2]: "H2"}
    elif len(sizes) == 2:
        level_map = {sizes[0]: "title", sizes[1]: "H1"}
    else:
        level_map = {sizes[0]: "title"}

    output = {"title": "", "outline": []}
    for b in blocks:
        level = level_map.get(round(b["size"], 1))
        if level == "title" and output["title"] == "":
            output["title"] = b["text"]
        elif level in {"H1", "H2", "H3"}:
            output["outline"].append({
                "level": level,
                "text": b["text"],
                "page": b["page"]
            })
    return output

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            blocks = extract_text_blocks(os.path.join(input_dir, filename))
            result = assign_heading_levels(blocks)
            out_file = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(out_file, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
