# AGENTS.md

This file contains conventions for agentic coding assistants working in this Astro portfolio project.

## Build Commands

### Available Scripts
- `npm run dev` - Start development server (http://localhost:4321)
- `npm run build` - Build for production (outputs to ./dist/)
- `npm run preview` - Preview production build locally
- `npm run astro ...` - Run Astro CLI commands

### Type Checking
Run `npx astro check` to validate Astro components and catch type errors.

## Project Structure

```
src/
├── components/      # Reusable Astro components
├── layouts/         # Page layouts (BaseLayout, MarkdownPostLayout)
├── pages/           # File-based routing
│   ├── posts/      # Dynamic blog post routes
│   └── tags/       # Tag filtering pages
├── blog/           # Markdown blog posts
└── styles/         # Global CSS files
```

## Code Style Guidelines

### Astro Components (.astro)

#### Frontmatter
- Use `---` fence at the top for frontmatter
- Imports first, then component logic
- Props destructured: `const { pageTitle } = Astro.props`

#### Imports
- Relative paths: `import Header from "../components/header/Header.astro"`
- CSS imports: `import "../styles/global.css"`
- Astro imports: `import { getCollection } from "astro:content"`

#### HTML/Template
- 4-space indentation
- Complex elements: attributes on new lines
- Self-closing tags for void elements: `<Logo />`
- Use `<slot />` for content injection in layouts

### CSS

#### Styling Conventions
- Use CSS variables from Gruvbox theme (var(--bg), var(--fg1), var(--orange))
- Utility classes: .paper-border, .paper-shadow, .paper-button
- Kebab-case class names
- Scoped styles in `<style>` blocks within components
- Media queries for responsiveness (breakpoints: 700px, 768px)

#### Paper Design System
```
.paper-border    - 3px solid var(--fg1)
.paper-shadow    - 4px 4px 0px 0px var(--fg1)
.paper-button    - Combines border + shadow + hover animation
```

### TypeScript

#### Types
- Project uses strict mode (extends astro/tsconfigs/strict)
- Use `@ts-check` in .ts/.mjs config files
- Content schemas defined with Zod in `src/content.config.ts`
- Prefer proper types over `any` (avoid `(post as any)`)
- Type content collection items explicitly

#### Naming Conventions
- Components: PascalCase (Header.astro, Navigation.astro)
- Variables: camelCase (currentPath, allPosts)
- CSS classes: kebab-case (nav-link, paper-card)
- File names: PascalCase for components

### Dynamic Routes

#### Static Paths
Use `getStaticPaths()` for dynamic routes:
```astro
export async function getStaticPaths() {
  const posts = await getCollection("blog");
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { post },
  }));
}
```

#### Content Collection Access
- Use `getCollection("blog")` to fetch posts
- Render markdown with `await render(post)`

### Common Patterns

#### Current Path Detection
```astro
const currentPath = Astro.url.pathname;
```

#### Conditional Classes
```astro
<a class:list={["nav-link", { active: currentPath === "/" }]}>
```

#### Content Collections
- Blog posts in `src/blog/*.md`
- Frontmatter validated by Zod schema
- Required fields: title, pubDate, description, author, image, tags

### Development Notes

- Astro version: ^5.16.4
- Iconify integration via astro-icon
- Client-side transitions with astro:transitions
- RSS feed via @astrojs/rss
- JetBrains Mono font loaded in fonts.css

### Testing

No test framework configured. When adding tests:
1. Choose appropriate framework (e.g., Vitest)
2. Add test scripts to package.json
3. Document single test run command here
