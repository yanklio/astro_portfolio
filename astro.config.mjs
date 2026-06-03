// @ts-check
import { defineConfig } from "astro/config";

import icon from "astro-icon";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://yanklio.netlify.app",
  integrations: [
    icon({
      include: {
        tabler: [
          "arrow-left",
          "arrow-right",
          "article",
          "ban",
          "brand-github",
          "brand-linkedin",
          "home",
          "link",
          "menu-2",
          "moon",
          "rss",
          "sun",
          "x",
        ],
      },
    }),
    sitemap(),
  ],
});
