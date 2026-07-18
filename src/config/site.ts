export const site = {
    description: "Personal website and blog of Yaroslav — Full-Stack Developer working with TypeScript, React, Next.js, Node.js, and Python.",
    handle: "yanklio",
    location: "Poznan, PL",
    name: "Yaroslav",
    url: "https://yanklio.netlify.app",
} as const;

export const navigationItems = [
    { href: "/", label: "About" },
    { href: "/blog", label: "Notes" },
] as const;

export function isNavigationItemActive(pathname: string, href: string) {
    return href === "/" ? pathname === href : pathname === href || pathname.startsWith(`${href}/`);
}

export const socialLinks = [
    { href: "https://github.com/yanklio", label: "GitHub" },
    { href: "https://www.linkedin.com/in/yaroslav-u/", label: "LinkedIn" },
] as const;

export const toolboxGroups = [
    { label: "Frontend", tools: "HTML · CSS · JavaScript · TypeScript · React · Next.js · Angular" },
    { label: "Backend", tools: "Node.js · Express · NestJS · Java · Spring · SQL · PostgreSQL · MongoDB" },
    { label: "Infrastructure", tools: "Docker · CI/CD · AWS · Terraform" },
    { label: "Tools", tools: "Linux · Git · Vim · OpenCode · Codex" },
] as const;
