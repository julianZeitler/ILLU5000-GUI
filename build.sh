#! /bin/bash

git pull origin main
rm -rf docs/_build/html/*
rm -rf docs/_build/latex/*
sphinx-build -b html docs docs/_build/html
sphinx-build -b latex docs docs/_build/latex
zip -r docs/_build/DataAnalyzer.zip docs/_build/latex
