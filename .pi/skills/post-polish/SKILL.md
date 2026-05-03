---
name: post-polish
description: Polishes blog post drafts for rbucks.com. Completes all frontmatter fields, checks for typos and omissions, suggests corrections in a table, and provides a quick critique. Use after writing a draft or when asked to review a post.
---

# Post Polish

Validates and polishes a blog post for [rbucks.com](https://rbucks.com). Run this after writing a draft or when asked to review an existing post.

## How It Works

Read the post file, then work through each section below. **Do not edit the file** — only suggest corrections in the table format specified.

## 1. Frontmatter Audit

Check the post's frontmatter against the table below. For each field, note whether it's **present**, **missing**, or **needs correction**. If missing or incorrect, suggest a value.

### Required Fields

| Field | Rules |
|-------|-------|
| `Title` | Sentence case. Capitalize first word and proper nouns only (e.g. "Why I run", not "Why I Run"). |
| `Date` | `YYYY-MM-DD HH:MM` format. Should be the current or intended publish date. |
| `Slug` | Lowercase, hyphens between words. Must be unique. |
| `Category` | One of: `business`, `family`, `food`, `health`, `lifestyle`, `personal`, `politics`, `technology` (lowercase). |
| `Tags` | Comma-separated, lowercase. 2-6 relevant tags. |

### Recommended Fields

| Field | Rules |
|-------|-------|
| `Summary` | One sentence, ~20-30 words. Describes what the post is about. Used on homepage listings. |
| `Subtitle` | Short phrase (3-8 words). Appears in the article kicker next to the category. |
| `Deck` | 1-2 sentences. A compelling blurb that appears below the title as a lead-in. Longer than Subtitle, shorter than a full paragraph. |
| `Description` | ~160 chars, plain text. Used for SEO and search results. Auto-generated from first paragraph if missing. |

### Conditional Fields

| Field | Rules |
|-------|-------|
| `Status` | Include `Status: draft` if the post is not ready to publish. Omit entirely when ready to publish (removing the line publishes it). |

### Valid Categories

Only use these exact categories (lowercase): `business`, `family`, `food`, `health`, `lifestyle`, `personal`, `politics`, `technology`.

### URL Convention

Slug determines the URL: `/{year}/{month}/{day}/{slug}/`. Ensure the slug is unique and descriptive.

## 2. Typos & Omissions Check

Scan the post body for:

- **Spelling errors** — misspelled words, especially proper names and domain-specific terms
- **Grammar issues** — subject-verb agreement, tense consistency, run-on sentences
- **Punctuation** — missing periods, mismatched quotes, missing em-dashes or en-dashes
- **Missing cross-references** — references to other posts that should use `{filename}slug.md` syntax
- **Broken `{static}` references** — image paths that might not exist
- **Repeated words** — e.g. "the the", "is is"
- **Inconsistent capitalization** — e.g. mixing "Scripted" and "scripted"

## 3. Correction Table

Present all suggested corrections in this exact table format:

| # | Location | Issue | Suggestion |
|---|----------|-------|------------|
| 1 | Line 12 | Missing `Summary:` field | Add `Summary: Reflections on attending a political fundraiser...` |
| 2 | Line 14 | "recieved" → "received" | Fix spelling error |
| 3 | Line 24 | References "earlier post" without link | Add `{filename}my-thyroid-got-cancer.md` link |

Number each row. Keep suggestions concise and actionable.

## 4. Quick Critique

After the table, provide a brief critique (2-4 sentences) covering:

- **Tone & voice** — Does it sound like the author? Is the voice consistent?
- **Structure** — Does the post flow well? Are there logical breaks?
- **Clarity** — Is the main point clear? Any confusing sections?
- **Cuts** — Any sentences or paragraphs that drag?

Be direct and honest. This is a writing workout, not a compliment sandwich.

## Example Output

For a post about finding one's political voice:

| # | Location | Issue | Suggestion |
|---|----------|-------|------------|
| 1 | Frontmatter | Missing `Subtitle:` field | Add `Subtitle: Searching for the progressive middle` |
| 2 | Frontmatter | Missing `Deck:` field | Add a 1-2 sentence blurb about attending the fundraiser |
| 3 | Line 20 | "Scott Weiner" → "Scott Wiener" | Fix spelling of the state senator's name |
| 4 | Line 32 | Mentions "my cancer saga" without link | Add `{filename}my-thyroid-got-cancer.md` for readers new to the story |

**Critique:** The post has a strong conversational voice and the anecdote about speaking at the fundraiser is compelling. The middle section listing policy critiques feels a bit list-like — consider weaving them into the narrative instead of enumerating. The ending lands well but could use one more sentence tying back to the opening.
