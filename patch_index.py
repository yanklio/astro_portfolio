import re

with open("src/pages/index.astro", "r") as f:
    content = f.read()

new_bento_grid = """
        <div class="bento-grid">
            <div class="paper-card paper-border paper-shadow id-card bento-item id-item">
                <div class="card-content">
                    <span class="label">USER_ID</span>
                    <h1 class="giant-text">YAROSLAV</h1>
                    <div class="deco-line"></div>
                    <span class="id-number">#001</span>
                </div>
            </div>

            <div class="paper-card paper-border paper-shadow role-card bento-item role-item">
                <span class="label">CURRENT_ROLE</span>
                <span class="value">Full-Stack Dev</span>
                <span class="sub-value">@ Viseven</span>
            </div>

            <div class="paper-card paper-border paper-shadow bio-card bento-item bio-item">
                <span class="label">ABOUT_ME</span>
                <p class="bio-text">Welcome! 👋 And also hi! I'm Yaroslav, a Full-Stack Dev and interesting mostly in web technologies. During my journey I used a lot of interesting technologies including TypeScript, React (with recently popular Next.js), NodeJs, Python and that's not all of them. But main focus as should be - always on product 🏆</p>
            </div>

            <div class="paper-card paper-border paper-shadow exploring-card bento-item exploring-item">
                <span class="label">EXPLORING</span>
                <p class="small-text">🌍 Evolving in web sphere using different technologies (Typescript, React, React Native, Angular, NodeJs, Python, ...)</p>
            </div>

            <div class="paper-card paper-border paper-shadow ai-card bento-item ai-item">
                <span class="label">AI_&_AGENTS</span>
                <p class="small-text">🪄 Playing with LLM, Agents and AI (Github Copilot, Gemini CLI, Firebase Studio, ...)</p>
            </div>

            <div class="paper-card paper-border paper-shadow linux-card bento-item linux-item">
                <span class="label">OS_&_TOOLS</span>
                <p class="small-text">🐧 And continue to bless Linux as OS (Currently on Fedora + Cosmic❤️, in future strong Vim user💪)</p>
            </div>

            <!-- Socials Card -->
            <div class="paper-card paper-border paper-shadow socials-card bento-item socials-item">
                <div class="social-row">
                    <a href="https://github.com/yanklio" target="_blank" rel="noopener noreferrer" class="net-link">Github</a>
                    <span class="divider">/</span>
                    <a href="https://www.linkedin.com/in/yaroslav-u/" target="_blank" rel="noopener noreferrer" class="net-link">LinkedIn</a>
                </div>
            </div>

            <a href="/blog" class="primary-btn paper-button bento-item blog-item">
                <span class="btn-text">ENTER_BLOG</span>
                <span class="btn-icon">➜</span>
            </a>
        </div>
"""

new_css = """
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
            grid-auto-rows: minmax(100px, auto);
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
            grid-column: span 2;
            grid-row: span 2;
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
            grid-column: span 2;
            grid-row: span 1;
        }

        .blog-item {
            grid-column: span 2;
            grid-row: span 1;
        }
    }

    /* Card Base Styles */
"""

content = re.sub(r'<div class="bento-grid">.*</div>\s*</div>\s*</BaseLayout>', new_bento_grid + '    </div>\n</BaseLayout>', content, flags=re.DOTALL)
content = re.sub(r'\.bento-grid \{.*?\/\* Card Base Styles \*\/', new_css, content, flags=re.DOTALL)

with open("src/pages/index.astro", "w") as f:
    f.write(content)
