from typing import Dict, Any, Tuple
import re
from pathlib import Path
from nbconvert.exporters import HTMLExporter
import nbformat
from bs4 import BeautifulSoup


def _export(json: Dict[str, Any]) -> Tuple[Dict[str, Any], str]:
    config = {"TemplateExporter": {"template_file": "basic.tpl"}}
    html, _ = HTMLExporter(config).from_notebook_node(json)

    metadata = {"type": "article"}
    metadata.update(json.get("metadata", {}).get("miyadaiku", {}))

    if "title" not in metadata:
        soup = BeautifulSoup(html, "html.parser")
        for elem in soup(re.compile(r"h\d")):
            text = elem.text.strip()
            text = text.strip("\xb6")  # remove 'PILCROW SIGN'
            metadata["title"] = text
            break

    return metadata, "<div>" + html + "</div>"


def load(path: Path) -> Tuple[Dict[str, Any], str]:
    json = nbformat.read(str(path), nbformat.current_nbformat)
    return _export(json)


def load_string(s: str) -> Tuple[Dict[str, Any], str]:
    json = nbformat.reads(s, nbformat.current_nbformat)
    return _export(json)
