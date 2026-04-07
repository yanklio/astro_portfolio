# AGENTS.md

This file contains conventions for agentic coding assistants working in this Astro portfolio project.

## Build Commands

### Available Scripts
- `npm run dev` - Start development server (http://localhost:4321)
- `npm run build` - Build for production (outputs to `./dist/`)
- `npm run preview` - Preview production build locally
- `npm run astro ...` - Run Astro CLI commands

### Type Checking
Run `npx astro check` to validate Astro components and catch type errors.

## Project Structure

```text
src/
├── components/      # Reusable Astro components
├── content.config.ts # Zod schemas for content validation
├── layouts/         # Page layouts (BaseLayout, MarkdownPostLayout)
├── pages/           # File-based routing
│   ├── posts/      # Dynamic blog post routes
│   └── tags/       # Tag filtering pages
├── blog/           # Markdown blog posts
└── styles/         # Global CSS files (gruvbox.css, global.css, fonts.css)
```

## Code Style Guidelines

### Astro Components (.astro)

#### Frontmatter
- Use `---` fence at the top for frontmatter.
- Imports first, then component logic.
- Props destructured: `const { pageTitle } = Astro.props`

#### Imports
- Relative paths: `import Header from "../components/header/Header.astro"`
- CSS imports: `import "../styles/global.css"`
- Astro imports: `import { getCollection, render } from "astro:content"`

#### HTML/Template
- 4-space indentation.
- Complex elements: attributes on new lines.
- Self-closing tags for void elements: `<Logo />`
- Use `<slot />` for content injection in layouts.

### CSS and Styling Conventions

#### The "Gruvbox Paper" Aesthetic
- The website styling uses a retro, Gruvbox-themed aesthetic primarily utilizing the `gruvbox.css` stylesheet.
- Layouts favor centered containers (e.g., max-width 1000px for lists, 800px for posts) with uppercase heavy headers and orange dividers.
- **Do not** use 'Bento-box' grid layouts; they are out of style and should be avoided.
- Use Gruvbox highlight colors (orange, blue, purple, green) for alternating borders and shadows.
- Utilize CSS variables from the Gruvbox theme: `var(--bg)`, `var(--fg1)`, `var(--orange)`, etc.

#### Paper Design System
- Utility classes:
  - `.paper-border` - heavy solid borders, typically `3px solid var(--fg1)`
  - `.paper-shadow` - deep distinct shadows, typically `4px 4px 0px 0px var(--fg1)`
  - `.paper-button` - Combines border + shadow + hover animation (moves up and left slightly on active/hover, translating shadow).
- Kebab-case class names for utilities.
- Scoped styles in `<style>` blocks within `.astro` components when overriding or adding specific layout behavior.
- Media queries for responsiveness (breakpoints: 700px, 768px).

### TypeScript and Content

#### Types
- Project uses strict mode (extends `astro/tsconfigs/strict`).
- Use `@ts-check` in `.ts`/`.mjs` config files.
- Content schemas defined with Zod in `src/content.config.ts`.
- Prefer proper types over `any` (avoid `(post as any)`).
- Type content collection items explicitly where possible.

#### Content Collections (Blog)
- Blog posts are stored in `src/blog/*.md`.
- Ensure files do not start with an underscore if they are meant to be published (`**/[^_]*.md`).
- Frontmatter is validated by a Zod schema. Required fields typically include: `title`, `pubDate`, `description`, `author`, `image`, `tags`.
- Image URLs in content metadata support both absolute URLs (`http://` or `https://`) and root-relative paths (`/`).
- Use `getCollection("blog")` to fetch posts.
- Render markdown content in views using `const { Content } = await render(post)`.

### Common Patterns

#### Dynamic Routes
Use `getStaticPaths()` for dynamic routes such as blog posts or tag filtering:
```astro
import { getCollection, render } from "astro:content";

export async function getStaticPaths() {
  const posts = await getCollection("blog");
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { post },
  }));
}
```

#### Current Path Detection
```astro
const currentPath = Astro.url.pathname;
```

#### Conditional Classes
```astro
<a class:list={["nav-link", { active: currentPath === "/" }]}>
```

### Development Notes

- Astro version: `^5.16.4`
- Iconify integration via `astro-icon` (`@iconify-json/ic` and `@iconify-json/mi`).
- Client-side transitions configured with `astro:transitions` (if added).
- RSS feed via `@astrojs/rss`.
- JetBrains Mono font loaded in `fonts.css`.
- The 'about' page for the website is typically located at `src/pages/index.astro`.

### Verification & Testing

- **Frontend Verification:** Frontend UI changes must be visually verified before submission using Playwright (e.g., via a Python script capturing a screenshot of the local development or preview server, typically at http://localhost:4321 or the active local port).
- Always ensure that temporary files, test scripts, and test artifacts (like Python scripts, Playwright screenshots, or preview logs) are deleted from the repository before requesting a code review or submitting changes.
- **Deep Planning:** The user requires a strict 'deep planning mode' before making changes, meaning clarifying questions must be asked using `request_user_input` until there is zero doubt.
