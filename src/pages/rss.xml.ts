import type { APIRoute } from "astro";
import rss from "@astrojs/rss";
import { site } from "../config/site";
import { getBlogPosts } from "../data/blog";

export const GET: APIRoute = async ({ site: siteUrl }) => {
    if (!siteUrl) throw new Error("The site URL must be configured to generate the RSS feed.");

    const posts = await getBlogPosts();

    return rss({
        customData: "<language>en-us</language>",
        description: site.description,
        items: posts.map((post) => ({
            description: post.data.description,
            link: `/blog/${post.id}/`,
            pubDate: post.data.pubDate,
            title: post.data.title,
        })),
        site: siteUrl,
        title: `${site.handle} | Notes`,
    });
};
