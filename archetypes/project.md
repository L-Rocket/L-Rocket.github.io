---
date: '{{ .Date }}'
draft: true
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
description: 'Short summary of the project.'
tags: ['project']
cover:
  image: '/images/project-placeholder.png'
  alt: 'Project cover image'
  caption: ''
  relative: false
---

## Overview

Write a 2-4 sentence overview of the project.

## Highlights

- Key result or feature
- Tech stack or approach
- Outcome or metric

## Links

- Demo: https://example.com
- Code: https://github.com/yourname/your-repo
