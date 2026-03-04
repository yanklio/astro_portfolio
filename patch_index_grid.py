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
            grid-template-columns: repeat(2, 1fr);
            grid-auto-rows: minmax(120px, auto);
        }

        .id-item {
            grid-column: span 2;
        }

        .role-item {
            grid-column: span 2;
        }

        .bio-item {
            grid-column: span 2;
        }

        .exploring-item {
            grid-column: span 2;
        }

        .ai-item {
            grid-column: span 1;
        }

        .linux-item {
            grid-column: span 1;
        }

        .socials-item {
            grid-column: span 2;
        }

        .blog-item {
            grid-column: span 2;
        }
    }

    @media (min-width: 1024px) {
        .bento-grid {
            grid-template-columns: repeat(4, 1fr);
            grid-auto-rows: minmax(120px, auto);
            grid-auto-flow: dense;
        }

        /*
         * Row 1: [ID (2)] [Role (2)]
         * Row 2: [ID (2)] [Bio (2)]
         * Row 3: [Exploring (2)] [Bio (2)]
         * Row 4: [AI (1)] [Linux (1)] [Socials (2)]
         * Row 5: [Blog (4)]
         */

        .id-item {
            grid-column: span 2;
            grid-row: span 2;
        }

        .role-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .bio-item {
            grid-column: span 2;
            grid-row: span 2;
        }

        .exploring-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .ai-item {
            grid-column: span 1;
            grid-row: span 1;
        }

        .linux-item {
            grid-column: span 1;
            grid-row: span 1;
        }

        .socials-item {
            grid-column: span 2;
            grid-row: span 1;
        }

        .blog-item {
            grid-column: span 4;
            grid-row: span 1;
        }
    }

    /* Card Base Styles */

"""

content = re.sub(r'\.bento-grid \{.*?\/\* Card Base Styles \*\/', new_styles, content, flags=re.DOTALL)

with open("src/pages/index.astro", "w") as f:
    f.write(content)
