# AGENTS.md

Conventions for agentic coding assistants working in this Astro portfolio project.

## Commands

### Development and validation

- `npm run dev` — start the development server at `http://localhost:4321`.
- `npm run build` — create the production build in `dist/`.
- `npm run preview` — preview the production build locally.
- `npx astro check` — validate Astro components and TypeScript.
- `git diff --check` — detect whitespace errors before handoff.

### Formatting

- `npm run format` — format Astro components and CSS.
- `npm run format:check` — verify formatting without changing files.
- Prettier is configured in `.prettierrc.json` with `prettier-plugin-astro`.
- Do not run Prettier over Markdown content or unrelated project files unless requested.

## Project Structure

```text
src/
├── blog/                 # Markdown blog posts
├── components/           # Reusable Astro components
│   ├── footer/           # Site footer
│   └── header/           # Navigation, theme, and RSS controls
├── config/site.ts        # Site copy, navigation, social links, and fallback image
├── content.config.ts     # Blog content schema
├── data/blog.ts          # Typed blog collection access
├── layouts/              # Base and Markdown post layouts
├── pages/                # About, Notes, articles, RSS, robots, and 404 routes
├── scripts/theme.ts      # Theme-control behavior
└── styles/
    ├── fonts.css         # Local font declarations
    ├── global.css        # Global primitives and reusable utilities
    ├── gruvbox.css       # Gruvbox color palette and theme switching
    └── tokens.css        # Layout, spacing, typography, and control tokens
```

## Astro and TypeScript

### Frontmatter and imports

- Use `---` fences for Astro frontmatter.
- Put imports first, followed by types, component logic, and derived values.
- Destructure component props: `const { pageTitle } = Astro.props`.
- Use relative imports for local files.
- Prefer explicit types and collection entry types over `any`.
- The project extends Astro's strict TypeScript configuration.

### Templates

- Use four-space indentation; let Prettier handle wrapping.
- Put attributes on separate lines when an element becomes difficult to scan.
- Use self-closing syntax for components and void elements where appropriate.
- Use `<slot />` for layout content.
- Preserve semantic heading order and accessible names.
- Mark decorative symbols and icons with `aria-hidden="true"`.
- Use `aria-current="page"` for current navigation destinations.

## Design System

### Gruvbox Paper aesthetic

- Preserve the retro Gruvbox paper appearance: flat backgrounds, strong outlines, offset shadows, condensed uppercase labels, and orange accents.
- Do not introduce Bento-style card grids.
- Prefer existing Gruvbox roles such as `var(--bg)`, `var(--fg1)`, `var(--accent)`, and `var(--surface)` instead of raw colors.
- Keep layouts direct and editorial. Decorative boxes should have a clear purpose.

### Token ownership

- `src/styles/gruvbox.css` owns raw theme colors and light/dark switching.
- `src/styles/tokens.css` owns semantic layout, spacing, typography, border, shadow, and control values.
- `src/styles/global.css` owns reusable primitives and global element behavior.
- Component styles should primarily describe component-specific layout.
- Before adding a hardcoded font size, padding, gap, border, shadow, or width, check for an existing semantic token.
- Add a token when a value is reused or expresses a site-wide design decision.
- Keep intentionally unique values local, such as ASCII-art scaling or the large date numeral.

### Shared primitives

- `.paper-button` provides the standard background, `2px` border, `4px` offset shadow, and pressed interaction.
- `.compact-button` provides compact uppercase controls such as RSS and source buttons.
- `.action-button` provides shared typography, spacing, and padding for prominent text actions.
- `.action-button__icon` styles the arrow or external-link symbol inside an action.
- `.page-container` provides the shared centered content width.
- `.page-top` provides standard page-top spacing.
- `.page-kicker` provides small uppercase contextual labels.
- Extend these primitives with component classes instead of reimplementing their borders, shadows, typography, or pressed states.

### Responsive tiers

- Use `700px` as the primary desktop/mobile breakpoint.
- Use `420px` only for narrow-phone adjustments that cannot be handled at `700px`.
- Do not introduce nearby one-off breakpoints such as `600px`, `760px`, or `768px` without a documented layout need.
- Mobile controls and source buttons should use the available width without causing horizontal overflow.

### Scoped CSS

- Keep component-specific styles in scoped `<style>` blocks.
- Use kebab-case class names and BEM-like element names where helpful.
- Keep one declaration per line and rely on Prettier for consistent formatting.
- Avoid repeating global typography, button, border, and shadow declarations locally.

## Content and Routes

### Blog collection

- Blog posts live in `src/blog/*.md`.
- Published files must not begin with an underscore (`**/[^_]*.md`).
- Frontmatter is validated in `src/content.config.ts`.
- Current fields are `title`, `pubDate`, `description`, `author`, optional `image`, and `tags`.
- Keep image support even when a post currently relies on the fallback social image.
- Use `getBlogPosts()` from `src/data/blog.ts` for consistently typed, date-sorted posts.
- Render Markdown with `const { Content } = await render(post)`.

### Dynamic article routes

```ts
export async function getStaticPaths() {
    const posts = await getBlogPosts();

    return posts.map((post) => ({
        params: { slug: post.id },
        props: { post },
    }));
}
```

### Current navigation state

- Use `isNavigationItemActive()` from `src/config/site.ts` instead of duplicating pathname logic.

## Metadata and Theme

- `astro.config.mjs` is the single source of truth for the canonical site URL.
- Use `Astro.site` or the route context's `site` value for canonical URLs, RSS, robots, sitemap references, and structured data.
- Do not duplicate the deployment URL in `src/config/site.ts` or static text files.
- `BaseLayout.astro` owns canonical, Open Graph, Twitter, and JSON-LD metadata.
- Article layouts must pass `pageType="article"` and forward an optional post image.
- Pages without an image use `site.defaultImage`.
- Do not advertise search structured data unless working search behavior exists.
- Apply the stored/system theme in the inline head script before rendering to prevent theme flash.
- Keep interactive theme-control logic in `src/scripts/theme.ts`.

## Preserved Product Decisions

- Keep the two disabled `???` source buttons on the Notes page until the user requests replacements.
- Keep optional blog image support and the fallback social image.
- Keep the footer version as visible text; do not derive or remove it unless requested.
- The current article's disabled “Open” control represents the already-open page and should retain its pressed state.

## Verification

- Run `npm run format:check`, `npm run build`, `npx astro check`, and `git diff --check` before handoff.
- Visually verify frontend changes in a browser at desktop and mobile widths.
- Check About, Notes, an article, and 404 when shared layout or design primitives change.
- Confirm there is no horizontal overflow at mobile widths.
- Verify current navigation states, pressed/disabled controls, theme controls, and footer spacing when relevant.
- Inspect generated `dist/robots.txt`, `dist/rss.xml`, and page metadata when URL or metadata behavior changes.
- Remove temporary screenshots, scripts, logs, and preview artifacts from the repository before handoff.

## Working Process

- Preserve unrelated user changes in a dirty worktree.
- Ask clarifying questions before changes when design intent or scope is ambiguous.
- The user expects deep planning for broad or visual work; continue clarification until the intended outcome is unambiguous.
- Keep changes on a separate `codex/` branch unless the user explicitly requests another workflow.
