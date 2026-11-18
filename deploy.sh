#!/bin/zsh
# Rigenera la pagina e la pubblica su https://alessiogranella.github.io/studio/
set -e
cd "$(dirname "$0")"
python3 build.py
git add -A
git commit -m "Aggiorna lo studio ($(date +%d/%m/%Y))" || echo "Niente da aggiornare"
git push
