import re

with open("src/pages/index.astro", "r") as f:
    content = f.read()

new_styles = """
    .bento-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 1.5rem;
        width: 100%;
        max-width: 1000px;
    }

    @media (min-width: 768px) {
        .bento-grid {
            grid-template-columns: repeat(4, 1fr);
            grid-auto-rows: minmax(120px, auto);
        }

        .id-item {
            grid-column: span 2;
            grid-row: span 2;
        }

        .role-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .bio-item {
            grid-column: span 4;
            grid-row: span 1;
        }

        .exploring-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .ai-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .linux-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .socials-item {
            grid-column: span 1;
            grid-row: span 1;
        }

        .blog-item {
            grid-column: span 1;
            grid-row: span 1;
        }
    }

    @media (min-width: 1024px) {
        .bento-grid {
            grid-template-columns: repeat(6, 1fr);
            grid-auto-rows: minmax(120px, auto);
        }

        .id-item {
            grid-column: span 3;
            grid-row: span 2;
        }

        .role-item {
            grid-column: span 3;
            grid-row: span 1;
        }

        .bio-item {
            grid-column: span 3;
            grid-row: span 2;
        }

        .exploring-item {
            grid-column: span 3;
            grid-row: span 1;
        }

        .ai-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .linux-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .socials-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .blog-item {
            grid-column: span 6;
            grid-row: span 1;
        }
    }

    /* Card Base Styles */

    .bio-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--fg);
        margin: 0;
    }

    .small-text {
        font-size: 1rem;
        line-height: 1.5;
        color: var(--fg2);
        margin: 0;
    }

    .exploring-item {
        background-color: var(--bg2);
    }

    .ai-item {
        background-color: var(--bg);
        border-color: var(--purple);
    }

    .linux-item {
        background-color: var(--bg);
        border-color: var(--blue);
    }

    .bio-item {
        background-color: var(--bg);
        border-color: var(--green);
    }

"""

content = re.sub(r'\.bento-grid \{.*?\/\* Card Base Styles \*\/', new_styles, content, flags=re.DOTALL)

with open("src/pages/index.astro", "w") as f:
    f.write(content)
