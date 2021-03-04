#! /bin/bash

git pull origin main
rm -rf _build/html/*
rm -rf _build/latex/*
sphinx-build -b html . _build/html
sphinx-build -b latex . _build/latex
zip -r _build/DataAnalyzer.zip _build/latex
