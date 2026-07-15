import { getCollection, type CollectionEntry } from "astro:content";

export type BlogPost = CollectionEntry<"blog">;

export async function getBlogPosts(): Promise<BlogPost[]> {
    const posts = await getCollection("blog");

    return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}
