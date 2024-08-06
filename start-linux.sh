#!/bin/bash

python -m shiny run \
  --port 5000 \
  --reload \
  --reload-excludes "*.png,*.pdf" \
  --launch-browser \
  --dev-mode \
  app.py