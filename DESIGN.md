---
version: alpha
name: Number Sequence Play
description: Warm, playful, and highly tactile UI for 3-7 year old children learning number sequences. Designed for large touch targets, immediate visual feedback, and zero frustration.
colors:
  primary: "#f472b6"          # Warm pink
  secondary: "#fbbf24"        # Sunny yellow
  accent: "#34d399"           # Fresh green
  warm-bg: "#fff7ed"          # Cream
  card-bg: "#fefce8"          # Soft yellow
  text-strong: "#9f1239"      # Deep rose
  text-muted: "#854d0e"       # Warm brown
typography:
  display:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "3rem"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 800
    lineHeight: 1.1
  body:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
    lineHeight: 1.3
rounded:
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "9999px"   # full pill for special elements
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  xxl: "32px"
components:
  level-card:
    backgroundColor: "{colors.card-bg}"
    borderColor: "#fde047"
    borderWidth: "4px"
    borderRadius: "{rounded.lg}"
    padding: "16px"
    minHeight: "128px"
    boxShadow: "0 8px 0 #e2e8f0"
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    borderRadius: "{rounded.md}"
    padding: "16px 24px"
    fontWeight: 800
  success-state:
    backgroundColor: "#dcfce7"
    textColor: "#166534"
    borderColor: "#4ade80"
  error-state:
    backgroundColor: "#fef3c7"
    textColor: "#854d0e"
    borderColor: "#fbbf24"
---

# Number Sequence Play — Design System

Warm, joyful, and extremely forgiving UI language for young children (3~7세) who are just beginning to understand number sequences.

## Overview

This design prioritizes **emotional safety** and **motor accessibility** above everything else. Every element must feel like a friendly toy — large, soft, colorful, and impossible to "get wrong" in a scary way. The visual language draws from:

- Lovable's warm cream parchment aesthetic (approachable, non-clinical)
- Figma's generous pill/rounded geometry and tactile depth
- Classic children's educational apps (Duolingo Kids, Khan Kids, ABCmouse) — big friendly shapes, immediate positive feedback, minimal text density

Core principles:
- Touch target minimum 64px (ideally 80px+)
- Zero sharp edges or hard contrasts
- Every action produces delightful, immediate feedback
- Text is short, warm, and action-oriented in Korean

## Colors

The palette is intentionally warm and pastel. High saturation is avoided in backgrounds to prevent overstimulation.

- **Warm Background** (`#fff7ed`): Primary page and screen background. Creamy and inviting.
- **Soft Yellow Cards** (`#fefce8`): Level cards and content surfaces.
- **Primary Accent** (`#f472b6`): Pink — used for CTAs and important highlights.
- **Sunny Yellow** (`#fbbf24`): Secondary highlight, borders, success states.
- **Fresh Green** (`#34d399`): Used for positive progress and "correct" states.
- **Deep Rose** (`#9f1239`): Strong text and headings.
- **Warm Brown** (`#854d0e`): Supporting text.

Error states deliberately use warm yellow/orange instead of red to avoid scaring children.

## Typography

- **Font stack**: System UI (San Francisco / Segoe UI / Roboto)
- Heavy use of **font-bold (700-900)** for everything children need to read.
- Extremely short Korean copy only.
- No dense paragraphs — maximum 2 short lines per label.

## Layout & Spacing

- Generous outer padding (`px-6` or more).
- Container max-width: `max-w-lg` (good balance between mobile and tablet).
- Consistent 12-16px gaps between interactive elements.
- Large section breathing room (space-y-6 or higher).

## Components

### Level Cards (Core Interaction)
- Large rounded-3xl (28-32px radius)
- 4px bright border + soft drop shadow
- Minimum height 128px (h-32)
- Two-line structure: bold title + friendly subtitle
- No long number sequences — pure conceptual language
- Active state: scale 0.94 + reduced shadow (tactile "press" feeling)

### Game Grid Cells
- Even larger rounded corners
- Thick borders
- Very large numbers (clamp 3.5rem ~ 7rem)
- Strong but friendly correct/wrong states (green glow vs warm yellow)

### Celebration Modal
- Extra large rounded corners (36px+)
- Confetti + big encouraging Korean text
- Single clear "다시 할래요" button

## Do's and Don'ts

**Do**
- Use warm cream backgrounds everywhere
- Make every button at least 64px tall with generous padding
- Use 4px+ colored borders on cards
- Write extremely short, cheerful Korean copy
- Give instant visual + audio feedback on every tap
- Use soft shadows and scale transforms for tactile feedback

**Don't**
- Use red for wrong answers (use warm orange/yellow instead)
- Show long number sequences like "1420 → 1520" in level selection
- Use small text or dense labels
- Use sharp 4px or 8px corners on main interactive elements
- Create narrow containers that cause text overflow
- Use clinical white or gray backgrounds

## Current Implementation Notes (2026-05-30)

- Single-file HTML + Tailwind CDN
- Heavy use of pastel Tailwind colors (emerald, amber, sky, violet, rose)
- Recent improvements: removed number examples from level buttons, increased card height, added overflow-hidden
- Next focus areas: tighter control over text overflow, more consistent card internal layout, stronger visual hierarchy between categories

This DESIGN.md should be the single source of truth for all future visual changes.