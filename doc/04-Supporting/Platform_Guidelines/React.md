# React.dev Documentation Site

React.dev is the official documentation website for the React JavaScript library, built with Next.js 15.1. The site provides comprehensive learning resources, API references, community pages, and a blog, all rendered from Markdown/MDX content files. It features an interactive code playground powered by Sandpack, advanced MDX processing with custom components, and a sophisticated build system that compiles markdown into optimized React components at build time.

The architecture leverages Next.js static site generation to pre-render all markdown pages, using a custom MDX compilation pipeline that transforms markdown files into serialized React trees cached on disk. The site supports multiple sections (Learn, Reference, Community, Blog) with distinct navigation structures, includes Algolia-powered search, RSS feed generation, error decoder pages, and implements hot-reloading for markdown content during development. Built with TypeScript, Tailwind CSS, and React 19, it demonstrates modern web documentation practices with accessibility, responsive design, and developer experience as priorities.

## Site Configuration

Site-wide configuration settings

```javascript
// src/siteConfig.js
const { siteConfig } = require('./src/siteConfig');

// Configuration object
const config = {
  version: '19.2',
  languageCode: 'en',
  hasLegacySite: true,
  isRTL: false,
  copyright: `Copyright © ${new Date().getFullYear()} Facebook Inc. All Rights Reserved.`,
  repoUrl: 'https://github.com/facebook/react',
  twitterUrl: 'https://twitter.com/reactjs',
  algolia: {
    appId: '1FCF9AYYAT',
    apiKey: '1b7ad4e1c89e645e351e59d40544eda1',
    indexName: 'beta-react',
  },
};

// Usage in components
import { siteConfig } from '../siteConfig';
console.log(siteConfig.version); // "19.2"
```

## MDX Content Processing

Compile markdown files to React components

```typescript
// src/utils/compileMDX.ts
import compileMDX from 'utils/compileMDX';

// Compile MDX file to serialized React tree
const mdxContent = `
---
title: Getting Started with React
description: Learn React basics
---

# Hello React

This is **bold** text.

<Note>
This is a custom MDX component
</Note>
`;

const result = await compileMDX(mdxContent, 'learn/getting-started', {});

// Returns
const output = {
  content: '["$r","wrapper",null,{"children":[...]}]', // Serialized React tree
  toc: '[{"url":"#hello-react","depth":1,"text":"Hello React"}]', // Table of contents
  meta: {
    title: 'Getting Started with React',
    description: 'Learn React basics',
  },
  languages: null,
};

// Cached to node_modules/.cache/react-docs-mdx/ for fast rebuilds
```

## Dynamic Page Routing

Next.js catch-all route for markdown pages

```javascript
// src/pages/[[...markdownPath]].js
import { Page } from 'components/Layout/Page';

// This file handles all routes like /learn/foo, /reference/bar, etc.
export async function getStaticProps(context) {
  const path = (context.params.markdownPath || []).join('/') || 'index';

  // Read markdown file
  const mdx = fs.readFileSync(`src/content/${path}.md`, 'utf8');

  // Compile MDX to JSON
  const { toc, content, meta, languages } = await compileMDX(mdx, path, {});

  return {
    props: { toc, content, meta, languages },
  };
}

export async function getStaticPaths() {
  // Find all .md files recursively in src/content/
  const files = await getFiles('src/content');

  return {
    paths: files.map(file => ({
      params: { markdownPath: getSegments(file) },
    })),
    fallback: false, // All pages pre-rendered at build time
  };
}

export default function Layout({ content, toc, meta, languages }) {
  const parsedContent = JSON.parse(content, reviveNodeOnClient);
  const parsedToc = JSON.parse(toc, reviveNodeOnClient);

  return (
    <Page toc={parsedToc} meta={meta} languages={languages}>
      {parsedContent}
    </Page>
  );
}
```

## Custom MDX Components

Rich interactive components available in markdown

```typescript
// src/components/MDX/MDXComponents.tsx
import { MDXComponents } from 'components/MDX/MDXComponents';

// Example MDX file: src/content/learn/state-management.md
`
# State Management

<Intro>
Learn how to manage state in React applications.
</Intro>

<YouWillLearn>
- How to use useState
- When to lift state up
- How to share state between components
</YouWillLearn>

<Sandpack>

\`\`\`js App.js
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
\`\`\`

</Sandpack>

<Pitfall>
Don't mutate state directly. Always use setState.
</Pitfall>

<DeepDive title="How does React track changes?" excerpt="Learn about React's reconciliation">

React uses a virtual DOM to efficiently update the UI...

</DeepDive>

<Note>
This is an important note for developers.
</Note>

<Challenges>

#### Challenge 1: Add a reset button

Add a button that resets the counter to 0.

<Hint>
You'll need to call setCount(0).
</Hint>

<Solution>

\`\`\`js
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </>
  );
}
\`\`\`

</Solution>

</Challenges>
`;

// All components automatically available in MDX:
// Intro, YouWillLearn, Sandpack, Pitfall, DeepDive, Note,
// Challenges, Hint, Solution, Diagram, CodeDiagram, etc.
```

## Sandpack Integration

Interactive code playground in documentation

```typescript
// src/components/MDX/Sandpack/SandpackRoot.tsx
import { SandpackProvider } from '@codesandbox/sandpack-react/unstyled';

// Usage in MDX files
`
<Sandpack>

\`\`\`js App.js
import { useState } from 'react';

export default function App() {
  const [name, setName] = useState('React');

  return (
    <div>
      <input value={name} onChange={e => setName(e.target.value)} />
      <h1>Hello {name}!</h1>
    </div>
  );
}
\`\`\`

\`\`\`css styles.css
h1 {
  color: blue;
  font-family: sans-serif;
}
\`\`\`

</Sandpack>
`;

// Multi-file examples automatically detected
// Creates live-editable code sandbox with hot reload
// Supports React, CSS, and multiple JS files
```

## Page Layout System

Main layout component with navigation

```typescript
// src/components/Layout/Page.tsx
import { Page } from 'components/Layout/Page';

// Automatic section detection and routing
function MyDocPage() {
  return (
    <Page
      toc={[
        { url: '#intro', depth: 1, text: 'Introduction' },
        { url: '#usage', depth: 2, text: 'Usage' }
      ]}
      routeTree={sidebarLearn}
      meta={{
        title: 'Getting Started',
        description: 'Learn React basics',
        version: 'canary' // Optional: shows "Canary only" badge
      }}
      section="learn"
      languages={null}
    >
      <h1 id="intro">Introduction</h1>
      <p>Content here...</p>
      <h2 id="usage">Usage</h2>
      <p>More content...</p>
    </Page>
  );
}

// Renders with:
// - Top navigation with search
// - Sidebar navigation (for learn/reference/community)
// - Table of contents (right sidebar on desktop)
// - Breadcrumbs
// - Previous/Next page navigation
// - Footer
```

## RSS Feed Generation

Generate blog RSS feed

```javascript
// src/utils/rss.js - scripts/generateRss.js
const { generateRssFeed } = require('./src/utils/rss');

// Called during build in getStaticProps
generateRssFeed();

// Reads all blog posts from src/content/blog/
// Extracts frontmatter (title, author, date, description)
// Generates public/rss.xml

// Blog post frontmatter requirements:
`
---
title: "React 19 Released"
author: "React Team"
date: "2024-04-25"
description: "We're excited to announce React 19"
---

Blog content here...
`;

// Output: https://react.dev/rss.xml
// Subscribed by feed readers for React blog updates
```

## Markdown to HTML Plugin System

Remark plugins for markdown processing

```javascript
// plugins/markdownToHtml.js
const remark = require('remark');
const { remarkPlugins, markdownToHtml } = require('../plugins/markdownToHtml');

// Convert markdown to HTML (used for RSS feed descriptions)
const markdown = `
# Hello World

This is a [link](https://react.dev) to the docs.

![React Logo](/logo.png "React")
`;

const html = await markdownToHtml(markdown);

// Returns processed HTML with:
// - External links get target="_blank" and rel="noopener"
// - Custom header IDs for i18n (#hello-world)
// - Improved image syntax
// - Unwrapped images (no <p> wrapper)
// - Smart quotes and typography (curly quotes, em dashes)

console.log(html);
// Output:
// <h1 id="hello-world">Hello World</h1>
// <p>This is a <a href="https://react.dev" target="_blank" rel="noopener">link</a>...</p>
// <img src="/logo.png" alt="React Logo" title="React" />
```

## Next.js Configuration

Build configuration with webpack customization

```javascript
// next.config.js
const nextConfig = {
  pageExtensions: ['jsx', 'js', 'ts', 'tsx', 'mdx', 'md'],
  reactStrictMode: true,
  experimental: {
    scrollRestoration: true,
    reactCompiler: true, // Uses React Compiler for optimization
  },
  webpack: (config, { dev, isServer, ...options }) => {
    // Bundle analyzer for production builds
    if (process.env.ANALYZE) {
      const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
      config.plugins.push(
        new BundleAnalyzerPlugin({
          analyzerMode: 'static',
          reportFilename: options.isServer
            ? '../analyze/server.html'
            : './analyze/client.html',
        })
      );
    }

    // Custom module replacements for browser compatibility
    const { NormalModuleReplacementPlugin, IgnorePlugin } = require('webpack');
    config.resolve.alias['use-sync-external-store/shim'] = 'react';

    // Replace modules for client-side compatibility
    config.plugins.push(
      new NormalModuleReplacementPlugin(
        /^raf$/,
        require.resolve('./src/utils/rafShim.js')
      ),
      new NormalModuleReplacementPlugin(
        /^process$/,
        require.resolve('./src/utils/processShim.js')
      ),
      new IgnorePlugin({
        checkResource(resource, context) {
          // Skip ESLint built-in rules to reduce bundle size
          return (
            /\/eslint\/lib\/rules$/.test(context) &&
            /\.\/[\w-]+(\.js)?$/.test(resource)
          );
        },
      })
    );

    return config;
  },
};

// Run with: npm run analyze
// Generates bundle size visualization
```

## Development Workflow

Local development and content editing

```bash
# Install dependencies
yarn install

# Start development server with hot reload for markdown
yarn dev
# Opens http://localhost:3000
# Changes to src/content/*.md hot-reload automatically
# Changes to src/components/*.tsx hot-reload automatically

# Type checking
yarn tsc

# Linting and formatting
yarn lint
yarn prettier

# Fix heading IDs in markdown
yarn fix-headings

# Check all (CI validation)
yarn ci-check
# Runs: prettier, lint, tsc, lint-heading-ids, rss, deadlinks

# Build for production
yarn build
# Compiles all MDX, generates static HTML, optimizes assets, downloads fonts
# Output: .next/ directory

# Start production server
yarn start

# Generate RSS feed
yarn rss
```

## Content Structure

Organizing documentation content

```bash
src/content/
├── learn/              # Step-by-step tutorials
│   ├── index.md        # /learn landing page
│   ├── installation.md # /learn/installation
│   ├── describing-the-ui.md
│   ├── adding-interactivity.md
│   └── managing-state.md
├── reference/          # API documentation
│   ├── react/
│   │   ├── index.md    # /reference/react
│   │   ├── useState.md
│   │   └── useEffect.md
│   └── react-dom/
├── community/          # Community resources
│   ├── team.md
│   ├── conferences.md
│   └── meetups.md
├── blog/               # React blog posts
│   └── 2024/04/25/
│       └── react-19-upgrade-guide.md
├── warnings/           # Warning/error explanations
│   └── invalid-hook-call-warning.md
└── errors/             # Error code explanations
    └── *.md            # Error decoder content

# Frontmatter example:
---
title: useState
description: Add state to your components
---

# Content routing:
# src/content/learn/installation.md → https://react.dev/learn/installation
# src/content/reference/react/useState.md → https://react.dev/reference/react/useState
# src/content/errors/*.md → https://react.dev/errors/[errorCode]
```

## Error Decoder Pages

Dynamic error explanation pages

```typescript
// src/pages/errors/[errorCode].tsx
// Handles routes like /errors/418, /errors/423, etc.

// URL structure:
// https://react.dev/errors/418 → Renders error code 418 explanation
// https://react.dev/errors/423 → Renders error code 423 explanation

// Error markdown files stored in:
// src/content/errors/418.md
// src/content/errors/423.md

// Separate from main catch-all route
// Excluded from getStaticPaths in [[...markdownPath]].js (line 157)
// Uses dedicated error page component with ErrorDecoder context
```

## Sidebar Navigation

Dynamic navigation structure

```json
// src/sidebarLearn.json
{
  "title": "Learn React",
  "path": "/learn",
  "routes": [
    {
      "title": "Get Started",
      "path": "/learn",
      "routes": [
        {
          "title": "Quick Start",
          "path": "/learn",
          "description": "Learn React basics"
        },
        {
          "title": "Installation",
          "path": "/learn/installation",
          "description": "Set up your environment"
        }
      ]
    },
    {
      "title": "Describing the UI",
      "path": "/learn/describing-the-ui",
      "tags": ["components", "jsx"],
      "routes": [
        {
          "title": "Your First Component",
          "path": "/learn/your-first-component"
        }
      ]
    }
  ]
}

// Used by Page component for sidebar rendering
// Supports nested routes, descriptions, and tags
// Separate files: sidebarLearn, sidebarReference, sidebarCommunity, sidebarBlog
```

React.dev serves as both a learning platform and API reference for React developers. The main use cases include: (1) Progressive learning through the "Learn React" section, which guides developers from basics to advanced concepts with interactive examples; (2) API reference documentation providing exhaustive details on React hooks, components, and APIs; (3) Community resources including team information, conferences, and translations; (4) Blog posts announcing new features, releases, and best practices. The site architecture prioritizes performance through static generation, developer experience through hot reload, and content quality through strict linting and validation.

Integration patterns demonstrate modern documentation site architecture: MDX compilation happens at build time with aggressive caching for fast rebuilds; Sandpack provides in-browser code execution without external dependencies; the sidebar/navigation system adapts to different sections automatically; custom MDX components (Pitfall, Note, DeepDive, Challenges) create consistent, accessible UI patterns; Algolia search indexes all content for fast discovery; RSS feeds enable content syndication; and the entire codebase uses TypeScript for type safety. The system is designed to be translated (with language detection and routing), accessible (semantic HTML, ARIA labels), and maintainable (clear separation between content and presentation).
