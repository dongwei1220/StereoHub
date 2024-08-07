#!/bin/bash

python -m shiny run \
  --host 0.0.0.0 \
  --port 5000 \
  --reload \
  --reload-includes "*.py,*.css,*.js,*.html,*.md" \
  --reload-excludes "*.png,*.pdf" \
  --app-dir "." \
  --launch-browser \
  --dev-mode \
  app.py