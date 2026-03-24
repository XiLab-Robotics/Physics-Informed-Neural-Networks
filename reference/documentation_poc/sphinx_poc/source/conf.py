from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

project = 'Physics-Informed Neural Networks Docs POC'
author = 'Isolated Documentation Evaluation'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns: list[str] = []

html_theme = 'sphinx_rtd_theme'
html_static_path: list[str] = []
html_title = 'Physics-Informed Neural Networks Docs POC'

autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_class_signature = 'mixed'
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_examples = False
