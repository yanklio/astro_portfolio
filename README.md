# Astro Portfolio

A minimal, retro Gruvbox-themed personal portfolio and blog built with [Astro](https://astro.build).

## Features

- **Framework:** Astro ^5.16.4
- **Language:** TypeScript
- **Styling:** Custom retro, Gruvbox-themed CSS with a "Paper" design system (heavy borders, deep shadows).
- **Icons:** `astro-icon` integration for inline SVGs.
- **Blog:** Markdown-based blog using Astro Content Collections with Zod validation.
- **RSS Feed:** Built-in RSS feed generation using `@astrojs/rss`.

## Getting Started

### Prerequisites

- Node.js (v18 or higher recommended)
- npm (or yarn, pnpm, bun)

### Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```sh
   npm install
   ```

### Development

Start the local development server:

```sh
npm run dev
```

This will start the server at `http://localhost:4321`.

### Building for Production

To build the static site:

```sh
npm run build
```

The generated files will be placed in the `dist/` directory.

### Previewing Production Build

To preview the built site locally before deploying:

```sh
npm run preview
```

### Type Checking

To validate Astro components and catch type errors:

```sh
npx astro check
```

## Project Structure

```text
src/
├── blog/           # Markdown blog posts
├── components/     # Reusable Astro components (e.g., Header, Footer)
├── content.config.ts # Zod schemas for content collections
├── layouts/        # Page layouts (BaseLayout, MarkdownPostLayout)
├── pages/          # File-based routing (pages and dynamic routes)
└── styles/         # Global CSS files (including Gruvbox theme)
```
