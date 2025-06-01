# Misconception Detection in Python Code using Static Analysis

This repository contains the implementations of the various programming misconceptions that I considered in my Master's thesis *"A Comparison of Program Query Languages to Detect Python Programming Misconceptions"* (Université catholique de Louvain, 2025).

## Overview

The goal of this thesis is to explore how static analysis tools can be used to detect common programming misconceptions in students' Python code, and to compare various tools available for such a task.

The tools used in this project focus on identifying **symptoms** of misconceptions, which are code patterns that often arise from misunderstandings of programming concepts, even when the output of the program appears correct.

## Content

Each programming misconception has its own repository, containing a short definition of what it consists of and the different implementations used to detect it.

Performance and Accuracy measures are also available in `results/`.

## Tools Used

- [Flake8](https://flake8.pycqa.org/)
- [Regex](https://docs.python.org/3/library/re.html)
- [CodeQL](https://codeql.github.com/)
- [Pyttern](https://github.com/JulienLie/Pyttern)

## Misconception Classification

A classification of misconceptions gathered from various sources is also present in `Misconception_Classification.xlsx`.
